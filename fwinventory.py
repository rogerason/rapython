#
# redfish_get_FW_inventory.py
# Get and print the current inventory of a server's firmware
# Synopsis:
# redfish_get_FW_inventory.py <iDRAC IP addr> <user> <password>
#
import requests, json, sys, re, time, os, logging
import urllib3
urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)
from datetime import datetime
lines = []
servers = []
with open("discovery.dat","r") as discoverylist:
	for line in discoverylist:
		line = line.strip()
		if not str(line[0]) == "#":
			servers.append(line)
discoverylist.closed
print ("Servers in list:")			 
print (servers)		
for server in servers:
		print ("\n- Getting current firmware version(s) for all devices in the system iDRAC supports\n")
		req = requests.get('https://' + server.rstrip() + '/redfish/v1/UpdateService/FirmwareInventory/',verify=False,auth=('root','calvin'))
		statusCode = req.status_code
		data = req.json()
		print (req)
		number_of_devices=len(data[u'Members'])
		count = 0
		installed_devices=[]
		
		while count != len(data[u'Members']):
			a=data[u'Members'][count][u'@odata.id']
			a=a.replace("/redfish/v1/UpdateService/FirmwareInventory/","")
			if "Installed" in a:
				installed_devices.append(a)
			count +=1
		installed_devices_details=["\n--- Firmware Inventory ---"]
		a="-"*75
		installed_devices_details.append(a)
		l=[]
		ll=[]
		for i in installed_devices:
			req = requests.get('https://' + server.rstrip() + '/redfish/v1/UpdateService/FirmwareInventory/' + i + '', verify=False,auth=('root','calvin'))
			statusCode = req.status_code
			data = req.json()
			a="Name: %s" % data[u'Name']
			l.append(a.lower())
			installed_devices_details.append(a)
			a="Firmware Version: %s" % data[u'Version']
			ll.append(a.lower())
			installed_devices_details.append(a)
			a="Updateable: %s" % data[u'Updateable']
			installed_devices_details.append(a)
			a="-"*75
			installed_devices_details.append(a)
		for i in installed_devices_details:
			print (i)