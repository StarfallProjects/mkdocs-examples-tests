# MkDocs file

mkdocs-macros-plugin automatically has access to everything in your `mkdocs.yml` file.

## Example: Access your MkDocs configuration using `config`

mkdocs-macros-plugin comes with [seven built-in objects](https://mkdocs-macros-plugin.readthedocs.io/en/latest/pages/#batteries-included-defaut-objects). `config` contains the MkDocs configuration. 

### Code

{% raw %}
```yaml
# In mkdocs.yml
site_name: MkDocs Macros YAML Examples

# In your Markdown
{{ config.site_name }}
```
{% endraw %}

### Output

{{ config.site_name }}

## Example: Add custom variables using `extra`

You can make custom variables available using the `extra` object in your `mkdocs.yml`.

### Code

{% raw %}
```yaml
# In mkdocs.yml
extra:
  extraValueOne: 1
  extraValueTwo: two

# In your Markdown
* Value 1: {{ extraValueOne }}
* Value 2: {{ extraValueTwo }}
```
{% endraw %}

### Output 

* Value 1: {{ extraValueOne }}
* Value 2: {{ extraValueTwo }}