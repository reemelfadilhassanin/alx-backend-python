#!/usr/bin/env python3
"""A module for testing the utils module.
"""
import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json

class TestAccessNestedMap(unittest.TestCase):
    """Tests the `access_nested_map` function."""
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Tests `access_nested_map`'s output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            ) -> None:
        """Tests `access_nested_map` raises KeyError."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")

class TestGetJson(unittest.TestCase):
    """Tests the `get_json` function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """Tests `get_json`'s output."""
        # Create a mock response object with a json method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        
        # Patch requests.get to return the mock response
        with patch('utils.requests.get', return_value=mock_response) as mock_get:
            # Call the function being tested
            self.assertEqual(get_json(test_url), test_payload)
            # Verify that requests.get was called once with test_url
            mock_get.assert_called_once_with(test_url)

if __name__ == '__main__':
    unittest.main()
