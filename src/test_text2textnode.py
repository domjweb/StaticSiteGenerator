import unittest
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_to_textnodes
)

class TestTextToTextNodes(unittest.TestCase):

    def test_basic_text(self):
        text = "This is a simple text."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "This is a simple text.")
        self.assertEqual(nodes[0].text_type, text_type_text)

    def test_bold_text(self):
        text = "This is **bold** text."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[0].text_type, text_type_text)
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].text_type, text_type_bold)
        self.assertEqual(nodes[2].text, " text.")
        self.assertEqual(nodes[2].text_type, text_type_text)
if __name__ == "__main__":
    unittest.main()
