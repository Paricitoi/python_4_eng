from ciscoconfparse import CiscoConfParse

with open("cisco_ipsec.txt") as f:
	config_cfg = CiscoConfParse(f)

cr_map_entries = config_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES")

for item in cr_map_entries:
	print item.text
	child = item.children
	for c in child:
		print c.text
f.close()

