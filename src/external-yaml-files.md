# External YAML files

Including external YAML files is where this feature becomes really powerful:

* Allows you to create large YAML sources, without cluttering up your `mkdocs.yml`.
* Creates the possibility of single-sourcing content: for example, you could have a YAML file containing help text that you then display both in-app and in your docs.
* And intriguing possibilities for rendering OpenAPI spec files . . . 


The plugin docs have more information on [Including external yaml files](https://mkdocs-macros-plugin.readthedocs.io/en/latest/advanced/#including-external-yaml-files).

## Example: Include a YAML file from your project

**Code:**

{% raw %}
```yaml
# In mkdocs.yml
plugins:
  - macros:
      include_yaml:
        - _yaml/simple-example.yml

# In _yaml/simple-example.yml
simpleYamlOne: 1
simpleYamlTwo: two

# In your Markdown
* Simple YAML 1: {{ simpleYamlOne }}
* Simple YAML 2: {{ simpleYamlTwo }}
```
{% endraw %}

**Output:**

* Simple YAML 1: {{ simpleYamlOne }}
* Simple YAML 2: {{ simpleYamlTwo }}

