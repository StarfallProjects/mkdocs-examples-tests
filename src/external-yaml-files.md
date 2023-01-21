# External YAML files

Including external YAML files is where this feature becomes really powerful:

* Allows you to create large YAML sources, without cluttering up your `mkdocs.yml`.
* Creates the possibility of single-sourcing content: for example, you could have a YAML file containing help text that you then display both in-app and in your docs.
* And intriguing possibilities for rendering OpenAPI spec files . . . 

The plugin docs have more information on [Including external yaml files](https://mkdocs-macros-plugin.readthedocs.io/en/latest/advanced/#including-external-yaml-files).

## Example: Include a YAML file from your project

### Code

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

### Output

* Simple YAML 1: {{ simpleYamlOne }}
* Simple YAML 2: {{ simpleYamlTwo }}

## Example: Include a YAML file from an external URL

You can load YAML from files hosted outside your project using [modules](https://mkdocs-macros-plugin.readthedocs.io/en/latest/macros/).

This example loads an OpenAPI example, [petstore.yaml](https://raw.githubusercontent.com/OAI/OpenAPI-Specification/main/examples/v3.0/petstore.yaml).

### Code

Create a file, `main.py`, at the root of your project:

{% raw %}
```python
import requests, yaml

def define_env(env):
  url = 'https://raw.githubusercontent.com/OAI/OpenAPI-Specification/main/examples/v3.0/petstore.yaml'
  r = requests.get(url, allow_redirects=True)
  content = r.content.decode()
  open('_yaml/petstore.yaml', 'wt').write(content)
  with open('_yaml/petstore.yaml') as petstore:
    env.variables['petstore'] = yaml.safe_load(petstore)
```
{% endraw %}

Access the petstore YAML in your Markdown:

{% raw %}
```markdown
**Petstore version:**
{{ petstore.info.version }}

**Summary of the `/pets` endpoint `get` operation:**
{{ petstore.paths['/pets']['get'].summary }}

**Summary of the `/pets` endpoint `post` operation:**
{{ petstore.paths['/pets'].post.summary }}
```
{% endraw %}

### Output

**Petstore version:**

{{ petstore.info.version }}

**Summary of the `/pets` endpoint `get` operation:**

{{ petstore.paths['/pets']['get'].summary }}

**Summary of the `/pets` endpoint `post` operation:**

{{ petstore.paths['/pets'].post.summary }}

!!! note "Special characters and keywords"
    You need to wrap your YAML keys in `['']` if you YAML key:

     * Starts with a special character, such as `/`
     * Clashes with an operation, such as `dict.get()`
