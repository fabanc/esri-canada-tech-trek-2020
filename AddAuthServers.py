
from arcgis.gis import GIS
import requests
import json
import getpass

USER = "user_name"
PASS = getpass.getpass()

g = GIS("https://www.arcgis.com", USER, PASS)

# Grab the token from the ArcGIS Python API connection
token = g._con.token

# Common URL and request parameters
url = "https://esrica-ncr.maps.arcgis.com/sharing/rest/portals/self"
payload = {"f":"json",
			"token": token}

# List out all the current Authorized Servers
u = url + "/settings"
response = requests.post(u + "/query", data = payload)
r = json.loads(response.text)

AuthServers = r['authorizedCrossOriginDomains']
print("Authorized Servers:")
for c in AuthServers:
	print(c)

# Update the list with our server
AuthServers.append("https://www.KevinsArcGISServer.com")

# This particular workflow wants the request send as a form-body
u = url + "/update"
p = {**payload, **{"authorizedCrossOriginDomains": json.dumps(AuthServers)}}
headers = {**payload,
			'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
			"authorizedCrossOriginDomains": json.dumps(AuthServers)
			}

session = requests.Session()
response = session.post(u + "/query", headers=headers, data=p)
r = json.loads(response.text)

print("Update status: \n {}".format(r))

