import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, markdown_to_html_node  # replace 'your_module' with the actual name of your file without .py

class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        markdown_text = """This is **bolded** paragraph
        
This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        expected_output = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"
        ]
        
        self.assertEqual(markdown_to_blocks(markdown_text), expected_output)

class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(block_to_block_type("## This is a heading"), "heading")

    def test_code_block(self):
        code_block = "```\nprint('Hello World')\n```"
        self.assertEqual(block_to_block_type(code_block), "code")

    def test_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote"), "quote")

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("* This is an unordered list item"), "unordered_list")
        self.assertEqual(block_to_block_type("- Another unordered list item"), "unordered_list")

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. This is an ordered list item"), "ordered_list")

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is a simple paragraph"), "paragraph")

import unittest

# Assuming the functions are imported or defined above, e.g.
# from markdown_blocks import markdown_to_blocks, block_to_block_type, HTMLNode, markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraph(self):
        markdown = "This is a paragraph."
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.children[0].tag, 'p')
        self.assertEqual(html_node.children[0].value, 'This is a paragraph.')

    def test_heading(self):
        markdown = "# Heading 1"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.children[0].tag, 'h1')
        self.assertEqual(html_node.children[0].value, 'Heading 1')

    def test_code_block(self):
        markdown = "```\nCode block\n```"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.children[0].tag, 'pre')
        self.assertEqual(html_node.children[0].children[0].tag, 'code')
        self.assertEqual(html_node.children[0].children[0].value, 'Code block')

    def test_quote(self):
        markdown = "> This is a quote."
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.children[0].tag, 'blockquote')
        self.assertEqual(html_node.children[0].value, ' This is a quote.')

if __name__ == "__main__":
    unittest.main()
