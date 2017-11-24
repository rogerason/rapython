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
	print ("Model: {}".format(systemData[u'Model']))
	print ("Manufacturer: {}".format(systemData[u'Manufacturer']))
	print ("Service tag {}".format(systemData[u'SKU']))
	print ("Serial number: {}".format(systemData[u'SerialNumber']))
	print ("Hostname: {}".format(systemData[u'HostName']))
	print ("Power state: {}".format(systemData[u'PowerState']))
	print ("Asset tag: {}".format(systemData[u'AssetTag']))
	print ("Memory size: {}".format(systemData[u'MemorySummary'] [u'TotalSystemMemoryGiB']))
	print ("CPU type: {}".format(systemData[u'ProcessorSummary'][u'Model']))
	print ("Number of CPUs: {}".format(systemData[u'ProcessorSummary'][u'Count']))
	print ("System status: {}".format(systemData[u'Status'][u'Health']))
	#print ("RAID health: {}".format(storageData[u'Status'][u'Health']))