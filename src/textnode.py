class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (self.text == other.text and
                    self.text_type == other.text_type and
                    self.url == other.url)
        return False
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'

def split_nodes_delimiter(old_nodes, delimiter, text_type):
     new_nodes = []
    for node in old_nodes:
        if isinstance(node, TextNode):
            parts = node.text.split(delimiter) 

            if len(parts) % 2 == 0:
                raise ValueError("Mismatched delimiter in text: {}".format(node.text>

            for i, part in enumerate(parts): 
                if i % 2 == 0: 
                    if part:
                        new_nodes.append(TextNode(part, node.text_type))

                else: 
                    new_nodes.append(TextNode(part, text_type)) 
        else: 
            new_nodes.append(node) 
return new_nodes 
