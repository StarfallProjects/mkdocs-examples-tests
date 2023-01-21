import requests, yaml

def define_env(env):
  url = 'https://raw.githubusercontent.com/OAI/OpenAPI-Specification/main/examples/v3.0/petstore.yaml'
  r = requests.get(url, allow_redirects=True)
  content = r.content.decode()
  open('_yaml/petstore.yaml', 'wt').write(content)
  with open('_yaml/petstore.yaml') as petstore:
    env.variables['petstore'] = yaml.safe_load(petstore)