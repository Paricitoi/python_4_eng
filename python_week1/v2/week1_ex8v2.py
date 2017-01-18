#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

def main():
	cisco_cfg = CiscoConfParse("cisco_ipsec.txt")
	
	cr_map_list = cisco_cfg.find_objects(r"^crypto map CRYPTO")

	for item in cr_map_list:
		print item.text
		for child in item.children:
			print child.text


if __name__ == "__main__":
	main()

