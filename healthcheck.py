import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)

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
	print()
	print ("Calling server:")
	print (server)
	system = requests.get('https://' + server.rstrip() + '/redfish/v1/Systems/System.Embedded.1',verify=False,auth=('root','calvin'))
	storage = requests.get('https://' + server.rstrip() + '/redfish/v1/Systems/System.Embedded.1/Storage/Controllers/RAID.Integrated.1-1',verify=False,auth=('root','calvin'))
	systemData = system.json()
	storageData = storage.json()
	print ("System {}: Health status: {}".format(systemData[u'SKU'],systemData[u'Status'][u'Health']))