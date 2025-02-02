import json
import re
import unittest
from sanitize_json import sanitize_json

class TestSanitizeJson(unittest.TestCase):
    def test_valid_json(self):
        json_data = {"a": 1, "b": "hello"}
        self.assertEqual(sanitize_json(json.dumps(json_data)), json_data)

    def test_invalid_json(self):
        invalid_json = "{a: 1, b: 'hello'}"
        result = sanitize_json(invalid_json)
        self.assertTrue("Expecting property name enclosed in double quotes" in result["error"])

    def test_json_with_extra_text(self):
        json_data = {"a": 1, "b": "hello"}
        llm_output = "Some text before```json" + json.dumps(json_data) + "```Some text after"
        self.assertEqual(sanitize_json(llm_output), json_data)

    def test_empty_json(self):
        self.assertEqual(sanitize_json("{}"), {})

    def test_json_with_extra_text_and_error(self):
        llm_output = "Some text before```json{a: 1, b: 'hello'}```Some text after"
        result = sanitize_json(llm_output)
        self.assertTrue("Expecting property name enclosed in double quotes" in result["error"])

    def test_only_extra_text(self):
        llm_output = "Some text before and after"
        result = sanitize_json(llm_output)
        self.assertTrue("Expecting value" in result["error"])

if __name__ == "__main__":
    unittest.main()