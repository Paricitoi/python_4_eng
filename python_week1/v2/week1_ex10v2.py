#!/usr/bin/env python
import sys
from ciscoconfparse import CiscoConfParse

def main():
	if len(sys.argv) == 1:
		print "You can also give a filename"
		my_file = raw_input("What is the file name? ")
	else:
		my_file = sys.argv[1]

	config_cfg = CiscoConfParse(my_file)

	cr_map_entries = config_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES")

	for item in cr_map_entries:
		print item.text
		for child in item.children:
			print child.text
if __name__ == "__main__":
	main()
