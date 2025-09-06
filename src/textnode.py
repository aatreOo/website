from enum import Enum

class TextType(Enum):
    plain_text = "text (plain)"
    bold_text = "**Bold text**"
    italic_text = "_Italic text_"
    code_text = "´code text´"
    link_format = "[anchor text](url)"
    image_format = "![alt text](url)"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, object):
        if self.text == object.text and self.text_type == object.text_type and self.url == object.url:
            return True
        return False
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"