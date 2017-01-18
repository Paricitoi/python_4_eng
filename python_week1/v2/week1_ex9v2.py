#!/usr/bin/env python


from ciscoconfparse import CiscoConfParse

def main():

	config_cfg = CiscoConfParse("cisco_ipsec.txt")

	cr_map_entries = config_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"pfs group2")

	for item in cr_map_entries:
		print item.text
		for child in item.children:
			print child.text

if __name__ == "__main__":
	main()


