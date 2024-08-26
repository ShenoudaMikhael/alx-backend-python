#!/usr/bin/env python3
"""test_client"""
import unittest
from typing import Dict
from unittest.mock import MagicMock, patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


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
        mocked_fn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org))

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
