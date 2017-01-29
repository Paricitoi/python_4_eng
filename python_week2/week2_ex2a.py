#!/usr/bin/env python
'''comment number 3'''
import telnetlib
import sys
import time
import getpass

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def send_command(remote_conn, cmd):
	time.sleep(1)
	cmd = cmd.rstrip()
	remote_conn.write(cmd + '\n')
	time.sleep(1)
	return remote_conn.read_very_eager()

def login(remote_conn, username, password):
        output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
        remote_conn.write(username + '\n')
        output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
        remote_conn.write(password + '\n')
	return output


