#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from utils import access_nested_map

"""
class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)


Example inputs (from the intranet o):
nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")

#Guys, for each of the input above, I'm supposed to test with assertEqual that the functions returns the expected result
#Oh and, the body of the test method shouldbe no longer than 2 lines
"""
#Task 2
class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])

    def test_access_nested_map_exception(self, nested_map, path, expected):
        with self.assertRaises(KeyError) as ctx:
            access_nested_map(nested_map, path)
        self.assertEqual(ctx.exception.args[0], expected)
