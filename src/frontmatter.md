---
title: Frontmatter
description: How to include YAML frontmatter in your Markdown in an MkDocs site.
docsLink: https://mkdocs-macros-plugin.readthedocs.io/en/latest/pages/#in-the-yaml-header-of-the-page
tags:
  - mkdocs
  - jinja2
  - examples
---

# {{ title }}

{{ description }}

[Relevant plugin docs]({{ docsLink }})

List of tags:
{% for tag in tags %}
* {{ tag }}
{% endfor %}

## Use frontmatter variables in your Markdown

This page has the following frontmatter:

```yaml
title: Frontmatter
description: How to display YAML frontmatter in an MkDocs site.
docsLink: https://mkdocs-macros-plugin.readthedocs.io/en/latest/pages/#in-the-yaml-header-of-the-page
tags:
  - mkdocs
  - jinja2
  - examples
```

It then uses that frontmatter to create the title and introduction:

{% raw %}
```markdown
# {{ title }}

{{ description }}

[Relevant plugin docs]({{ docsLink }})

List of tags:
{% for tag in tags %}
* {{ tag }}
{% endfor %}
```
{% endraw %}