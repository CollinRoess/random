""" Checking for connectivity to Google.com"""

import requests


r= requests.get('https://www.google.com/')

if r.status_code!=200:
	print("There was an error."+str(r.status_code))
else:
	print("All good.")