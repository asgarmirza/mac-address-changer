#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest='interface_to_be_changed', help='Interface to change its MAC address')
parser.add_option("-m", "--mac", dest='mac_address_we_want', help='New MAC address')
(options, arguments) = parser.parse_args()
NoneType = type(None)

if (type(options.interface_to_be_changed)) == type(None):
    interface_to_be_changed = input("Please enter in the interface you would like to change the MAC address of: ")
else:
    interface_to_be_changed = options.interface_to_be_changed

if type(options.mac_address_we_want) == type(None):
    mac_address_we_want  = input("Please enter in the MAC address you would like to change to: ")
else:
    mac_address_we_want = options.mac_address_we_want

subprocess.call('sudo ifconfig ' + interface_to_be_changed + ' down', shell=True)
print('[+] ' + interface_to_be_changed + ' has been shut down')
print('[+] MAC address is being changed...')
subprocess.call('sudo ifconfig ' + interface_to_be_changed + ' hw ether ' + mac_address_we_want, shell=True)
print('[+] Bringing ' + interface_to_be_changed + ' back up...')
subprocess.call('sudo ifconfig ' +  interface_to_be_changed + ' up', shell=True)
print('[+] MAC address has been changed successfully')
