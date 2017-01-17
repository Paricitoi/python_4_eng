from ciscoconfparse import CiscoConfParse

config_cfg = CiscoConfParse("cisco_ipsec.txt")

cr_map_entries = config_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"pfs group2")

print cr_map_entries

