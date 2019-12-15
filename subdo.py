#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests

print ("""                               
 _____   _ _ _____     _     _     
|   | |_| |_|   __|_ _| |_ _| |___ 
| | | | . | |__   | | | . | . | . |
|_|___|___|_|_____|___|___|___|___|
--------------------------Tegal1337
""")

domain = input("[+] Input domain ndisit : ")
print ("[+] Sabar boss proses ... \n")

def main(domain):
	url = "https://api.indoxploit.or.id/domain/{}".format(domain)
	data = requests.get(url).json()
	ambil_data = data['data']['subdomains']
	print ("[+] Olihe kie tok : \n")
	for i in ambil_data:
		print(i)

if __name__ == '__main__':
	main(domain)