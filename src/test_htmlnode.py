import unittest
from .htmlnode import ParentNode, LeafNode  # Adjust the import path based on your project structure

class TestHTMLNode(unittest.TestCase):
    def test_simple_parent_node(self):
        simple_node = ParentNode("div", [LeafNode(None, "Simple content")])
        self.assertEqual(simple_node.to_html(), "<div>Simple content</div>")

    def test_multiple_children(self):
        multi_child_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text")
            ]
        )
        self.assertEqual(multi_child_node.to_html(), "<p><b>Bold text</b>Normal text<i>Italic text</i></p>")
    
    def test_nested_parent_nodes(self):
        nested_node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "Italic text")
                    ]
                )
            ]
        )
        self.assertEqual(nested_node.to_html(), "<div><p><b>Bold text</b>Normal text<i>Italic text</i></p></div>")
    
    def test_parent_node_with_props(self):
        props_node = ParentNode(
            "div",
            [
                LeafNode(None, "Content with props")
            ],
            props={"class": "container", "id": "main-container"}
        )
        self.assertEqual(props_node.to_html(), '<div class="container" id="main-container">Content with props</div>')

if __name__ == '__main__':
    unittest.main()
def test_text_node_to_html_node():
    class TextNode:
        def __init__(self, type, text="", href="", src="", alt=""):
            self.type = type
            self.text = text
            self.href = href
            self.src = src
            self.alt = alt

    # Test for "text"
    text_node = TextNode(type="text", text="Hello")
    result = text_node_to_html_node(text_node)
    assert result.value == "Hello"
    assert result.tag is None

    # Test for "bold"
    bold_node = TextNode(type="bold", text="Bold Text")
    result = text_node_to_html_node(bold_node)
    assert result.value == "Bold Text"
    assert result.tag == "b"

    # Test for "italic"
    italic_node = TextNode(type="italic", text="Italic Text")
    result = text_node_to_html_node(italic_node)
    assert result.value == "Italic Text"
    assert result.tag == "i"

    # Test for "code"
    code_node = TextNode(type="code", text="Code Text")
    result = text_node_to_html_node(code_node)
    assert result.value == "Code Text"
    assert result.tag == "code"

    # Test for "link"
    link_node = TextNode(type="link", text="Link Text", href="http://example.com")
    result = text_node_to_html_node(link_node)
    assert result.value == "Link Text"
    assert result.tag == "a"
    assert result.props["href"] == "http://example.com"

    # Test for "image"
    image_node = TextNode(type="image", src="http://example.com/image.png", alt="Sample Image")
    result = text_node_to_html_node(image_node)
    assert result.value == ""
    assert result.tag == "img"
    assert result.props["src"] == "http://example.com/image.png"
    assert result.props["alt"] == "Sample Image"

    # Test for unknown type (we expect an exception here)
try:
    unknown_node = TextNode(type="unknown")
    text_node_to_html_node(unknown_node)
    assert False, "Expected an exception to be raised for an unknown type"
except Exception as e:
    assert str(e) == "Unknown text type"

