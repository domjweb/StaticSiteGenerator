import sys
import os

# Helper function to add a directory to sys.path
def add_to_sys_path(directory_name):
    current_dir = os.path.dirname(__file__)
    module_path = os.path.join(current_dir, directory_name)
    sys.path.append(module_path)

# Add the 'src' directory to sys.path
add_to_sys_path('src')

import unittest
from markdown_extractor import extract_markdown_images

class TestMarkdownExtractor(unittest.TestCase):
    
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        expected_output = [
            ("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")
        ]
        self.assertEqual(extract_markdown_images(text), expected_output)

    # You can add more test cases to cover different scenarios

if __name__ == '__main__':
    unittest.main()
