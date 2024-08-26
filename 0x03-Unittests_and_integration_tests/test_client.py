#!/usr/bin/env python3
"""test_client"""
import unittest
from typing import Dict
from unittest.mock import (
    MagicMock,
    patch,
)
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
        mocked_fn.assert_called_once_with("https://api.github.com/orgs/{}".format(org))
