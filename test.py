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
                "children": [
                    {
                        "type": "text",
                        "text": "This is the first paragraph"
                    }
                ]
            },
            {
                "type": "paragraph",
                "text": "This is the second paragraph",
                "children": [
                    {
                        "type": "text",
                        "text": "This is the second paragraph"
                    }
                ]
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
                "children": [
                    {
                        "type": "text",
                        "text": "This is the first paragraph"
                    }
                ]
            },
            {
                "type": "heading",
                "level": 2,
                "text": "Minor heading",
            },
            {
                "type": "paragraph",
                "text": "This is the second paragraph",
                "children": [
                    {
                        "type": "text",
                        "text": "This is the second paragraph"
                    }
                ]
            }
        ])

    def testEmphasisWithinParagraph(self):
        self.assertEqual(self.markdown(
        "# Major heading\n"
        "\n"
        "A paragraph with *emphasis* half way through\n"),
        [
            {
                "text": "Major heading",
                "level": 1,
                "type": "heading"
            },
            {
                "text": "A paragraph with emphasis half way through",
                "children": [
                    {
                        "text": "A paragraph with ",
                        "type": "text"
                    },
                    {
                        "text": "emphasis",
                        "type": "emphasis"
                    },
                    {
                        "text": " half way through",
                        "type": "text"
                    }
                ],
                "type": "paragraph"
            }
        ])

    def testList(self):
        self.assertEqual(self.markdown(
        "- item 1\n"
        "- item 2 *with emph*\n"
        "- item 3"),
        [
            {
                'type': 'list',
                'text': 'item 1\nitem 2 with emph\nitem 3',
                'children': [
                    {
                        'text': 'item 1',
                        'children': [
                            {
                                'type': 'text',
                                'text': 'item 1'
                            }
                        ],
                    },
                    {
                        'text': 'item 2 with emph',
                        'children': [
                            {
                                'type': 'text',
                                'text': 'item 2 '
                            },
                            {
                                'type': 'emphasis',
                                'text': 'with emph'
                            }
                        ],
                    },
                    {
                        'text': 'item 3',
                        'children': [
                            {
                                'type': 'text',
                                'text': 'item 3'
                            }
                        ],
                    }
                ]
            }
        ])


