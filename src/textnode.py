from markdown_extractor import extract_markdown_links, extract_markdown_images


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
    
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_image = "image"
text_type_link = "link"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if isinstance(node, TextNode):
            parts = node.text.split(delimiter) 

            if len(parts) % 2 == 0:
               raise ValueError("Mismatched delimiter in text: {}".format(node.text))

            for i, part in enumerate(parts): 
                if i % 2 == 0: 
                    if part:
                        new_nodes.append(TextNode(part, node.text_type))

                else: 
                    new_nodes.append(TextNode(part, text_type)) 
        else: 
            new_nodes.append(node) 
    return new_nodes 

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if "!" in node.text:
            images = extract_markdown_images(node.text)
            current_text = node.text

            while images:
                image_tup = images.pop(0)
                parts = current_text.split(f"![{image_tup[0]}]({image_tup[1]})", 1)

                if parts[0]:
                    new_nodes.append(TextNode(parts[0], text_type_text))

                new_nodes.append(TextNode(image_tup[0], text_type_image, image_tup[1]))
                current_text = parts[1]

            if current_text:
                new_nodes.append(TextNode(current_text, text_type_text))

        else:
            new_nodes.append(node)

    return [node for node in new_nodes if node.text]


def split_nodes_link(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if "[" in node.text:  # Preliminary check for possible links
            links = extract_markdown_links(node.text)
            current_text = node.text

            while links:
                link_tup = links.pop(0)
                parts = current_text.split(f"[{link_tup[0]}]({link_tup[1]})", 1)

                # Add the leading text part if not empty
                if parts[0]:
                    new_nodes.append(TextNode(parts[0], text_type_text))
                
                # Add the link node
                new_nodes.append(TextNode(link_tup[0], text_type_link, link_tup[1]))

                # Update current_text to remaining part
                current_text = parts[1]
            
            # Add any remaining text part after the last link
            if current_text:
                new_nodes.append(TextNode(current_text, text_type_text))
        else:
            new_nodes.append(node)

    return [node for node in new_nodes if node.text]  # Exclude empty text nodes

def text_to_textnodes(text):
    # Step 1: Start with a single TextNode
    nodes = [TextNode(text, text_type_text)]
    
    # Step 2: Apply split functions for different markdown
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    # Step 3: Return the final list of TextNode objects
    return nodes