# Macros for templating

If you need reusable page structure, you usually use a template. For example, a template allows you to create a single layout, then apply it to all blog pages.

Macros are useful when you don't want to create a whole new page layout template, but you still want reusable styling, structure, and so on.

## Example: Use a macro and YAML file to generate a custom-styled list

This example uses the YAML in `_yaml/large-example.yml`. Refer to [External YAML files](/external-yaml-files) for guidance on including YAML files.

### Code

Create an HTML file containing your macro:

{% raw %}
```html
{% macro prettyList(color, name, sweetness) %}
  <li class="{{ color }}">{{ name }} : {{ sweetness }}</li>
{% endmacro %}
```
{% endraw %}

Add some custom CSS:

{% raw %}
```css
.green {
  color: green;
}

.orange {
  color: orange;
}

.yellow {
  color: yellow
}
```
{% endraw %}

Refer to [MkDocs - extra_css](https://www.mkdocs.org/user-guide/configuration/#extra_css) for more information on custom CSS with MkDocs.

Import the macro and iterate over the YAML:

{% raw %}
```jinja
{% import "_macros/pretty-list.html" as list %}

<ul>
{% for fruit in fruits %}
{{ list.prettyList(fruit.color, fruit.name, fruit.sweetness) }}
{% endfor %}
</ul>
```
{% endraw %}

Refer to the [Jinja2 Import documentation](https://jinja.palletsprojects.com/en/3.1.x/templates/#import) for more information about `import`.

!!! tip "Nunjucks and Jinja2"
    The Jinja2 documentation is sometimes hard to browse. Nunjucks is a JavaScript port of Jinja2. The documentation contents are similar, but better presented, and occasionally contain more detail. [Nunjucks Templating docs](https://mozilla.github.io/nunjucks/templating.html). 

    You can also search for solutions in either templating language if you're looking for examples of how to do something.

### Output

{% import "_macros/pretty-list.html" as list %}

<ul>
{% for fruit in fruits %}
{{ list.prettyList(fruit.color, fruit.name, fruit.sweetness) }}
{% endfor %}
</ul>