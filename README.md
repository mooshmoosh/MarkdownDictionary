# MarkdownDictionary

Convert markdown to a list of python dictionaries

This is a renderer for [mistune](https://github.com/lepture/mistune). Instead of rendering html, it renders a list of dictionaries describing the elements.

Example usage

```
>>> import mistune
>>> import DictionaryRenderer
>>> renderer = DictionaryRenderer.DictionaryRenderer()
>>> markdown = mistune.Markdown(renderer=renderer)
>>> result = markdown("""# This is the first heading
...
... This is a paragraph
...
... ## This is the second heading
...
... This is another paragraph""")
>>> print(json.dumps(result, indent=4))
[
    {
        "type": "heading",
        "text": "This is the first heading",
        "level": 1
    },
    {
        "type": "paragraph",
        "text": "This is a paragraph"
    },
    {
        "type": "heading",
        "text": "This is the second heading",
        "level": 2
    },
    {
        "type": "paragraph",
        "text": "This is another paragraph"
    }
]
```
