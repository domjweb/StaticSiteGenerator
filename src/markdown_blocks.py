import re
from htmlnode import HTMLNode

def markdown_to_blocks(markdown):
    blocks = []
    lines = markdown.split("\n")
    current_block = ""

    for line in lines:
        if line.strip():
            current_block += line + "\n"
        else:
            if current_block.strip():
                blocks.append(current_block.strip())
                current_block = ""

    if current_block.strip():
        blocks.append(current_block.strip())

    return blocks

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"
heading_pattern = re.compile(r'#{1,6} ')

def block_to_block_type(markdown):
    if heading_pattern.match(markdown):
        return block_type_heading
    elif markdown.startswith("```"):
        return block_type_code
    elif markdown.startswith(">"):
        return block_type_quote
    elif markdown.startswith("* ") or markdown.startswith("- "):
        return block_type_unordered_list
    elif re.match(r'^\d+\. ', markdown):
        return block_type_ordered_list
    else:
        return block_type_paragraph

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    root_node = HTMLNode(tag='div')

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == block_type_paragraph:
            root_node.children.append(HTMLNode(tag='p', value=block))
        elif block_type == block_type_heading:
            level = block.count("#")
            text = heading_pattern.sub("", block)
            root_node.children.append(HTMLNode(tag=f'h{level}', value=text))
        elif block_type == block_type_code:
            text = block[3:-3].strip()
            code_node = HTMLNode(tag='code', value=text)
            root_node.children.append(HTMLNode(tag='pre', children=[code_node]))
        elif block_type == block_type_quote:
            text = block[1:]
            root_node.children.append(HTMLNode(tag='blockquote', value=text))
        elif block_type == block_type_unordered_list:
            ul_node = HTMLNode(tag='ul')
            for item in block.split("\n"):
                text = item[2:]
                ul_node.children.append(HTMLNode(tag='li', value=text))
            root_node.children.append(ul_node)
        elif block_type == block_type_ordered_list:
            ol_node = HTMLNode(tag='ol')
            for item in block.split("\n"):
                text = item.split(". ")[1]
                ol_node.children.append(HTMLNode(tag='li', value=text))
            root_node.children.append(ol_node)

    return root_node
