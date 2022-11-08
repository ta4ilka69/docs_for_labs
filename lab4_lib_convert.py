import json, yaml
js = json.loads(open('./Monday.json',encoding='utf8').read())
s = yaml.safe_dump(js, default_flow_style=False, allow_unicode=True, sort_keys=False)
open('./Monday_lib.yaml', 'w', encoding='utf8').write(s)