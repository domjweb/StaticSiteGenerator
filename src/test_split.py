import unittest
from textnode import TextNode, split_nodes_link, text_type_text, text_type_link

class TestSplitNodesLink(unittest.TestCase):
    
    def test_no_links(self):
        node = TextNode("This is a simple text without links.", text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "This is a simple text without links.")
        self.assertEqual(new_nodes[0].text_type, text_type_text)

    def test_single_link(self):
        node = TextNode("Here is a [link](https://example.com).", text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "Here is a ")
        self.assertEqual(new_nodes[0].text_type, text_type_text)
        self.assertEqual(new_nodes[1].text, "link")
        self.assertEqual(new_nodes[1].text_type, text_type_link)
        self.assertEqual(new_nodes[1].url, "https://example.com")
        self.assertEqual(new_nodes[2].text, ".")
        self.assertEqual(new_nodes[2].text_type, text_type_text)

    def test_multiple_links(self):
        node = TextNode("Here is a [link](https://example.com) and here is another [link](https://example.org).", text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text, "Here is a ")
        self.assertEqual(new_nodes[0].text_type, text_type_text)
        self.assertEqual(new_nodes[1].text, "link")
        self.assertEqual(new_nodes[1].text_type, text_type_link)
        self.assertEqual(new_nodes[1].url, "https://example.com")
        self.assertEqual(new_nodes[2].text, " and here is another ")
        self.assertEqual(new_nodes[2].text_type, text_type_text)
        self.assertEqual(new_nodes[3].text, "link")


if __name__ == "__main__":
    unittest.main()
