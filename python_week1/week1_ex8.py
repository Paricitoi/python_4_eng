from ciscoconfparse import CiscoConfParse

config_cfg = CiscoConfParse("cisco_ipsec.txt")

crypto_map = config_cfg.find_objects(r"^crypto map CRYPTO")

for item in crypto_map:
	print item.children


