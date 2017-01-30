#!/usr/bin/env python
''' edited via notepad++'''
from snmp_helper import snmp_get_oid, snmp_extract

SNMP_COMMUNITY = 'galileo'
SNMP_PORT = 161
IP1 = '184.105.247.70'
IP2 = '184.105.247.71'
oid_sysdesc = '1.3.6.1.2.1.1.1.0'
oid_sysname = '1.3.6.1.2.1.1.5.0'


router_1 = (IP1, SNMP_COMMUNITY, SNMP_PORT)
router_2 = (IP2, SNMP_COMMUNITY, SNMP_PORT)


def main():
	sysname_1 = snmp_extract(snmp_get_oid(router_1, oid=oid_sysname))
	sysname_2 = snmp_extract(snmp_get_oid(router_2, oid=oid_sysname))
	sysdesc_1 = snmp_extract(snmp_get_oid(router_1, oid=oid_sysdesc))
	sysdesc_2 = snmp_extract(snmp_get_oid(router_2, oid=oid_sysdesc))

	print "Device 1 name is: " + sysname_1 + "\n"
	print "Device 1 desc is: " + sysdesc_1 + "\n"
	print "------------------------------"
	print "Device 2 name is: " + sysname_2 + "\n"
        print "Device 2 desc is: " + sysdesc_2 + "\n"
if __name__ == "__main__":
	main()
