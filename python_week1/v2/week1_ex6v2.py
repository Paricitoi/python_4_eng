#!/usr/bin/env python
import yaml
import json
from pprint import pprint as pp

def main():
	my_list = [0, 1, 2, 3, 4, 5, 6, 7, 'Test', ['test1', 2], {'hostname': 'Router1', 'ip_addr': '10.1.1.1', 'Manufacturer': 'Cisco'}]
	
	with open("myfile.yml","w") as f:
		f.write(yaml.dump(my_list, default_flow_style=False))
	with open("myfile.json","w") as f:
		json.dump(my_list, f)

if __name__ == "__main__":
	main()

