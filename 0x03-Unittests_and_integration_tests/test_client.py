#!/usr/bin/env python3
"""A module for testing the GithubOrgClient class.
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests the GithubOrgClient class."""

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, expected_response: dict, mock_get_json: Mock) -> None:
        """Tests that GithubOrgClient.org returns the correct value."""
        # Arrange
        mock_get_json.return_value = expected_response
        client = GithubOrgClient(org_name)

        # Act
        result = client.org  # Accessing as a property, not calling it

        # Assert
        self.assertEqual(result, expected_response)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )


if __name__ == '__main__':
    unittest.main()
