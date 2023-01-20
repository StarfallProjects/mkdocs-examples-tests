# Avoid clashing with code examples

If your content contains code examples with syntax similar to Jinja2, the plugin may try and parse them as macros. This is discussed in detail in the plugin documentation: [How to prevent accidental interpretation of "Jinja-like" statements?](https://mkdocs-macros-plugin.readthedocs.io/en/latest/advanced/#how-to-prevent-accidental-interpretation-of-jinja-like-statements).

Note that this behaviour is intentional: the plugin ignores the usual code fences (backticks) so that it can support use cases where the content of code blocks is computed on the fly.

The documentation suggests four possible solutions. For this example site, I have chosen [Solution 3: Explicitly marking the snippets as 'raw' ](https://mkdocs-macros-plugin.readthedocs.io/en/latest/advanced/#solution-3-explicitly-marking-the-snippets-as-raw). If you are adding the plugin to an existing site and don't want to edit your code examples, consider [Solution 4: Altering the syntax of Jinja2 for mkdocs-macros](https://mkdocs-macros-plugin.readthedocs.io/en/latest/advanced/#solution-4-altering-the-syntax-of-jinja2-for-mkdocs-macros).