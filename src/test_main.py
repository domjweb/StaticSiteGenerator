from main import extract_title

def test_extract_title():
    markdown_text = """
Some introduction text

# The Title of the Document

Some more text
"""
    expected_output = "The Title of the Document"
    
    result = extract_title(markdown_text)
    assert result == expected_output, f'Expected "{expected_output}", but got "{result}"'

if __name__ == "__main__":
    test_extract_title()
    print("All tests passed!")
