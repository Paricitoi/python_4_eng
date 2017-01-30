#!/usr/bin/env python

''' comment number 666'''
import telnetlib
import sys
import time
import getpass
from week2_ex2a import login, send_command
TELNET_PORT = 23
TELNET_TIMEOUT = 6

ip_addr = '184.105.247.70'
username = "pyclass"
password = "88newclass"

def main():
	remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
	login(remote_conn, username, password)
	output = send_command(remote_conn, "terminal leng 0")
	output = send_command(remote_conn,"show ip interface br")
	print output










	remote_conn.close()
if __name__ == "__main__":
	main()

