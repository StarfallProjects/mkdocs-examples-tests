# As rows in a table

This example uses the YAML in `_yaml/large-example.yml`. Refer to [External YAML files](/external-yaml-files) for guidance on including YAML files.

### Code

{% raw %}
```markdown
| Name | Color | Sweetness |
| ---- | ------ | --------- |
{% for fruit in fruits %}| {{ fruit.name }} | {{ fruit.color }} | {{ fruit.sweetness }} |
{% endfor %}
```
{% endraw %}

### Output

| Name | Color | Sweetness |
| ---- | ------ | --------- |
{% for fruit in fruits %}| {{ fruit.name }} | {{ fruit.color }} | {{ fruit.sweetness }} |
{% endfor %}

Note the positioning of the `for` syntax in the code example. This is deliberate. The following don't work:

{% raw %}
```markdown
| Name | Color | Sweetness |
| ---- | ------ | --------- |
{% for fruit in fruits %}
| {{ fruit.name }} | {{ fruit.color }} | {{ fruit.sweetness }} |
{% endfor %}

| Name | Colour | Sweetness |
| ---- | ------ | --------- |
{% for fruit in fruits %}| {{ fruit.name }} | {{ fruit.colour }} | {{ fruit.sweetness }} |{% endfor %}
```
{% endraw %}