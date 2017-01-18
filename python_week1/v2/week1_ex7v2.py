#!/usr/bin/env python
import yaml
import json
from pprint import pprint as pp

def main():

	with open("myfile.json") as f:
		new_list = json.load(f)

	with open("myfile.yml") as ff:
		new_list2 = yaml.load(ff)

	print"\n"
	print"*" * 3 + "JSON" 
	pp(new_list)
	print"\n"
        print"*" * 3 + "YAML"
	pp(new_list2)

if __name__ == "__main__":
	main()

