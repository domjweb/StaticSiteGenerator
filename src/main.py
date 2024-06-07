import shutil
import os
from markdown_blocks import markdown_to_html_node
from htmlnode import MarkdownToHtmlNode

def copy_static(static_dir, public_dir):
    if os.path.exists(static_dir):
        for item in os.listdir(static_dir):
            s = os.path.join(static_dir, item)
            d = os.path.join(public_dir, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
    else:
        print(f"Static directory {static_dir} does not exist. Skipping static files copy.")

def extract_title(markdown_content):
    split_lines = markdown_content.splitlines()
    for line in split_lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception("All pages need a single h1 header")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown content
    with open(from_path, "r") as file:
        markdown_content = file.read()

    # Read the template content
    with open(template_path, "r") as file:
        template_content = file.read()

    # Convert the markdown to HTML
    html_node = MarkdownToHtmlNode(markdown_content)
    html_content = html_node.to_html()

    # Extract the title from the markdown content
    title = extract_title(markdown_content)

    # Replace placeholders in the template with the title and HTML content
    final_content = template_content.replace("{{ Title }}", title)
    final_content = final_content.replace("{{ Content }}", html_content)

    # Ensure the directory to the dest_path exists
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Write the final content to the destination path
    with open(dest_path, 'w') as file:
        file.write(final_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)

    for entry in os.listdir(dir_path_content):
        full_entry_path = os.path.join(dir_path_content, entry)
        
        if os.path.isfile(full_entry_path) and full_entry_path.endswith('.md'):
            # Compute relative path and corresponding HTML path
            rel_path = os.path.relpath(full_entry_path, dir_path_content)
            html_file = os.path.splitext(rel_path)[0] + '.html'
            dest_path = os.path.join(dest_dir_path, html_file)

            # Ensure directory structure
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            print(f"Generating page from {full_entry_path} to {dest_path} using {template_path}")
            generate_page(
                from_path=full_entry_path,
                template_path=template_path,
                dest_path=dest_path
            )

        elif os.path.isdir(full_entry_path):
            print(f"Entering directory: {full_entry_path}")
            # Recursively process the directory
            new_dest_dir_path = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(full_entry_path, template_path, new_dest_dir_path)


def main():
    content_dir = 'content'
    from_path = 'content/index.md'
    template_path = 'template.html'
    dest_path = 'public/index.html'
    static_dir = 'static'  # Define the static directory
    public_dir = 'public'  # Define the public directory

    # Copy static files
    copy_static(static_dir, public_dir)
    
    # Generate webpage
    generate_pages_recursive(
        dir_path_content=content_dir,
        template_path=template_path,
        dest_dir_path=public_dir
    )

if __name__ == "__main__":
    main()



