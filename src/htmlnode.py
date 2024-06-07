from markdown import markdown

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

class MarkdownToHtmlNode(HTMLNode):
    def __init__(self, markdown_content):
        self.markdown_content = markdown_content
        super().__init__()

    def to_html(self):
        return markdown(self.markdown_content)

    def props_to_html(self):
        if not self.props:
            return ''
        return ' ' + ' '.join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return (f'HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, '
                f'props={self.props})')
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag, value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value.") 
        
        if self.tag is None:
            return self.value
        
        props_html = self.props_to_html() # handle props formatting
        return f'<{self.tag}{props_html}>{self.value}</{self.tag}>'
    
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if children is None:
            raise ValueError("ParentNode must have children.")
        super().__init__(tag, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag must be provided for ParentNode.")
        if not self.children:
            raise ValueError("ParentNode must have children.")

        html = f"<{self.tag}"
        if self.props:
            for key, value in self.props.items():
                html += f' {key}="{value}"'
        html += ">"

        for child in self.children:
            html += child.to_html()

        html += f"</{self.tag}>"

        return html
    
def text_node_to_html_node(text_node):
    if text_node.type == "text":
        return LeafNode(value=text_node.text, tag=None)
    elif text_node.type == "bold":
        return LeafNode(value=text_node.text, tag="b")
    elif text_node.type == "italic":
        return LeafNode(value=text_node.text, tag="i")
    elif text_node.type == "code":
        return LeafNode(value=text_node.text, tag="code")
    elif text_node.type == "link":
        return LeafNode(value=text_node.text, tag="a", props={"href": text_node.href})
    elif text_node.type == "image":
        return LeafNode(value="", tag="img", props={"src": text_node.src, "alt": text_node.alt})
    else:
        raise Exception("Unknown text type")
    
