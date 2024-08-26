#!/usr/bin/env python3
"""test_client"""
import unittest
from typing import Dict
from unittest.mock import MagicMock, patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from requests import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient"""

    @parameterized.expand(
        [
            ("google", {"login": "google"}),
            ("abc", {"login": "abc"}),
        ]
    )
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, response: Dict, mocked_fn: MagicMock) -> None:
        """test_org"""
        mocked_fn.return_value = MagicMock(return_value=response)
        ghdotorg_c = GithubOrgClient(org)
        self.assertEqual(ghdotorg_c.org(), response)
        mocked_fn.assert_called_once_with("https://api.github.com/orgs/{}".format(org))

    def test_public_repos_url(self) -> None:
        """test_public_repos_url"""
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
        ) as m_o:
            m_o.return_value = {
                "repos_url": "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """test_public_repos"""
        payload = {
            "repos_url": "https://api.github.com/users/google/repos",
            "repos": [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ],
        }
        mock_get_json.return_value = payload["repos"]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "episodes.dart",
                    "kratu",
                ],
            )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "bsd-3-clause"}}, "bsd-3-clause", True),
            ({"license": {"key": "bsl-1.0"}}, "bsd-3-clause", False),
        ]
    )
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """test_has_license"""

        self.assertEqual(GithubOrgClient("google").has_license(repo, key), expected)


@parameterized_class(
    [
        {
            "org_payload": TEST_PAYLOAD[0][0],
            "repos_payload": TEST_PAYLOAD[0][1],
            "expected_repos": TEST_PAYLOAD[0][2],
            "apache2_repos": TEST_PAYLOAD[0][3],
        },
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Performs integration tests for the `GithubOrgClient` class."""

    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        payloads = {
            "https://api.github.com/orgs/google": cls.org_payload,
            "https://api.github.com/orgs/google/repos": cls.repos_payload,
        }

        def side_effect(url):
            if url in payloads:
                return Mock(**{"json.return_value": payloads[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=side_effect)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()
