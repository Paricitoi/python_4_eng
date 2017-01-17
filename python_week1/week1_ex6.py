import yaml
import json

my_list = range(2)

my_list.append({})

my_list = range(2)

my_list.append({})

my_list[-1]['hostname']='Router1'

my_list[-1]['ip_addr']='10.0.0.1'

with open('file_w1_e6.yaml',"w") as f:
	f.write(yaml.dump(my_list, default_flow_style=False))


with open('file_w1_e6.json','w') as ff:
	json.dump(my_list,ff)

