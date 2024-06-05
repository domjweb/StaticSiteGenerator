import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):

    def test_equal_textnodes(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node1, node2)

    def test_unequal_textnodes_different_text(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a different text node", "bold")
        self.assertNotEqual(node1, node2)

    def test_unequal_textnodes_different_text_type(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node1, node2)

    def test_textnode_with_url(self):
        node1 = TextNode("This is a text node", "bold", url="https://example.com")
        node2 = TextNode("This is a text node", "bold", url="https://example.com")
        self.assertEqual(node1, node2)

    def test_textnode_with_none_url(self):
        node1 = TextNode("This is a text node", "bold", url=None)
        node2 = TextNode("This is a text node", "bold", url=None)
        self.assertEqual(node1, node2)

    def test_textnode_with_different_urls(self):
        node1 = TextNode("This is a text node", "bold", url="https://example.com")
        node2 = TextNode("This is a text node", "bold", url="https://another-example.com")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
