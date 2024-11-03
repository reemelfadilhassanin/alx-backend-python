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
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')  # Adjust the import path according to your project structure
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """Tests that GithubOrgClient.org returns the correct value."""
        # Arrange
        expected_response = {"org": org_name}  # Adjust based on the expected output structure
        mock_get_json.return_value = expected_response
        
        client = GithubOrgClient(org_name)

        # Act
        result = client.org()

        # Assert
        self.assertEqual(result, expected_response)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

if __name__ == '__main__':
    unittest.main()
