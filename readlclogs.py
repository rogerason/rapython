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
	lclog = requests.get('https://' + server.rstrip() + '/redfish/v1/Managers/iDRAC.Embedded.1/Logs/Lclog',verify=False,auth=('root','calvin'))
	systemData = lclog.json()
	
	for logEntry in systemData[u'Members']:
		print ("{}: {}".format(logEntry[u'Name'],logEntry[u'Created']))
		print (" {}\n".format(logEntry[u'Message']))