import mistune

class DictionaryRenderer(mistune.Renderer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.children = []

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
