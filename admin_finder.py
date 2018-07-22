print("#####################################")
print("#   +++ Admin Panel Finder v1 +++   #")
print("#     Script by ./H9x Hacker    #")
print("#    Saudi Arabia Hackers   #")
print("#####################################")
import urllib.request
url = ''
listw = ['/admin/','/admin22/','/login.php/','/wp-login.php/','/cpanel.php/']
for i in listw:
	curl = url+i
	try:
		openurl = urllib.request.urlopen(curl)
		print("[+] Found --->"+curl)
	except urllib.error.URLError as msg:
		print("[-] Not Found --->"+curl)
