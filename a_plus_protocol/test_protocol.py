import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent


class ProtocolTests(unittest.TestCase):
    def test_protocol_and_schema_are_valid_json(self):
        protocol = json.loads((ROOT / "protocol.json").read_text())
        schema = json.loads((ROOT / "protocol.schema.json").read_text())
        self.assertEqual("object", schema["type"])
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(set(schema["required"]), set(protocol))
        self.assertTrue(set(protocol).issubset(schema["properties"]))

    def test_execution_is_fail_closed(self):
        protocol = json.loads((ROOT / "protocol.json").read_text())
        self.assertFalse(protocol["live_model_execution_authorized"])
        self.assertFalse(protocol["human_participant_execution_authorized"])
        self.assertFalse(protocol["external_effects_authorized"])
        self.assertEqual("NONE", protocol["authority_delta"])

    def test_author_identity(self):
        protocol = json.loads((ROOT / "protocol.json").read_text())
        self.assertEqual("Tom Budd", protocol["author"]["name"])
        self.assertEqual("https://tombudd.com", protocol["author"]["website"])


if __name__ == "__main__":
    unittest.main()
