import unittest
import mistune
from DictionaryRenderer import DictionaryRenderer

class MarkdownParsingTests(unittest.TestCase):
    def setUp(self):
        self.renderer = DictionaryRenderer()
        self.markdown = mistune.Markdown(renderer=self.renderer)

    def testParagraphs(self):
        self.assertEqual(self.markdown(
        "This is the first paragraph\n"
        "\n"
        "This is the second paragraph\n"),
        [
            {
                "type": "paragraph",
                "text": "This is the first paragraph",
            },
            {
                "type": "paragraph",
                "text": "This is the second paragraph",
            }
        ])

    def testHeading(self):
        self.assertEqual(self.markdown(
        "# Major heading\n"
        "\n"
        "This is the first paragraph\n"
        "## Minor heading\n"
        "\n"
        "This is the second paragraph\n"),
        [
            {
                "type": "heading",
                "level": 1,
                "text": "Major heading",
            },
            {
                "type": "paragraph",
                "text": "This is the first paragraph",
            },
            {
                "type": "heading",
                "level": 2,
                "text": "Minor heading",
            },
            {
                "type": "paragraph",
                "text": "This is the second paragraph",
            }
        ])

