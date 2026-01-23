# Import the urllib.request module
import urllib.request
import re

def main():
	u = input("Please enter a url: ")
	if not u.startswith(("http://", "https://")):
		url = "http://" + u
	else:
		url = u
	return url

def fetch(url):
	# Open a connection to google.com
	req = urllib.request.urlopen(url)

	 # Download the webpage's contents
	response = req.read().decode(errors='ignore')

	return response

u = main()
data = fetch(u)
while True:
	target = input("Please enter the word to be searched: ")

	if target in data:
		count = len(re.findall(rf"\b{re.escape(target)}\b", data, re.IGNORECASE))
		print(f"True, {count}")
	elif target == "leave":
		break
	else:
		print("False")

