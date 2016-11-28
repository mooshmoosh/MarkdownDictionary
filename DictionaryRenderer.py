import mistune

class DictionaryRenderer(mistune.Renderer):
    def placeholder(self):
        return []

    def paragraph(self, text):
        return [{
            "type": "paragraph",
            "text": ''.join(text)
        }]

    def header(self, text, level, raw=None):
        return [{
            "type": "heading",
            "level": level,
            "text": ''.join(text)
        }]
