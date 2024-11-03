#!/usr/bin/env python3
"""A module for testing the GithubOrgClient class.
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests the GithubOrgClient class."""

    @parameterized.expand([
        ("google", {'login': "google", 'repos_url': "https://api.github.com/orgs/google/repos"}),
        ("abc", {'login': "abc", 'repos_url': "https://api.github.com/orgs/abc/repos"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, expected_response: dict, mock_get_json: Mock) -> None:
        """Tests that GithubOrgClient.org returns the correct value."""
        mock_get_json.return_value = expected_response
        client = GithubOrgClient(org_name)

        result = client.org
        self.assertEqual(result, expected_response)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self) -> None:
        """Tests the _public_repos_url property."""
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/orgs/google/repos"
            }
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/google/repos")
            mock_org.assert_called_once()


if __name__ == '__main__':
    unittest.main()
