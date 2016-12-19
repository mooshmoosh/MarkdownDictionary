import mistune

class DictionaryRenderer(mistune.Renderer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.children = []
        self.list_elements = []

    def placeholder(self):
        return []

    def paragraph(self, text):
        result = [{
            "type": "paragraph",
            "text": ''.join(text),
            "children": self.children
        }]
        self.children = []
        return result

    def header(self, text, level, raw=None):
        self.children = []
        return [{
            "type": "heading",
            "level": level,
            "text": ''.join(text)
        }]

    def text(self, text):
        self.children.append({
            "type": "text",
            "text": ''.join(text)
        })
        return text

    def emphasis(self, text):
        self.children[-1]['type'] = "emphasis"
        return text

    def list(self, body, ordered=True):
        result = [{
            "type": "list",
            "text": ''.join(body),
            "children": self.list_elements
        }]
        self.list_elements = []
        return result

    def list_item(self, text):
        self.list_elements.append({
            "text": "".join(text),
            "children": self.children
        })
        self.children = []
        if len(self.list_elements) > 1:
            return ["\n"] + text
        else:
            return text
