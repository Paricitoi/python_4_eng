import yaml
import json
from pprint import pprint as pp
with open("file_w1_e6.json") as f:
	new_list = json.load(f)
pp(new_list)

with open("file_w1_e6.yaml") as ff:
	new_list2 = yaml.load(ff)
pp(new_list2)

f.close()
ff.close()
