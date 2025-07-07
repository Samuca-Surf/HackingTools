#!/usr/bin/python3
import sys
import requests

host = sys.argv[1]
wordlist = sys.argv[2]

file = open(wordlist)

for i in file:
	sub = i.replace("\n", "")
	url = f"http://{sub}.{host}"

	try:
		req = requests.get(url, timeout=3)
		statusCode = req.status_code

		if statusCode != 404:
			print(f"{url}  >  {statusCode}")
	except requests.RequestException:
		pass
