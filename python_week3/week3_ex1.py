#!/usr/bin/env python

import snmp_helper
import time

SNMP_COMMUNITY = 'galileo'
SNMP_PORT = 161
IP1 = '184.105.247.70'
IP2 = '184.105.247.71'
oid_ccmHistoryRunningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'
oid_ccmHistoryRunningLastSaved = '1.3.6.1.4.1.9.9.43.1.1.2.0'
oid_ccmHistoryStartupLastChanged = '1.3.6.1.4.1.9.9.43.1.1.3.0'
a_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
snmp_user = (a_user, auth_key, encrypt_key)
pynet_rtr1 = (IP1, SNMP_PORT)
pynet_rtr2 = (IP2, SNMP_PORT)
saved_value = 0
def main():
	global saved_value
	while True:
		snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, oid=oid_ccmHistoryRunningLastChanged)
		ccmHistoryRunningLastChanged = snmp_helper.snmp_extract(snmp_data)
		if saved_value != ccmHistoryRunningLastChanged:
			print "Uptime when running config last changed: " + ccmHistoryRunningLastChanged + "\n"
		time.sleep(10)
		saved_value = ccmHistoryRunningLastChanged 
		

if __name__ == "__main__":
	main()

