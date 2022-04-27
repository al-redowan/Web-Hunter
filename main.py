import socket
import requests
import sys
file = open('wp-contentthemessitein.txt').read().split()
for url in file:
    domain = url.split('//')[1].replace('www.', '').replace('/', '')
    try :
        ipadrre = socket.gethostbyname(domain)
        response = requests.get(f"https://sonar.omnisint.io/reverse/{ipadrre}").txt
        for urldata in response:
            a=open('core/wordpress.py','a').write(urldata+"\n")
            a.close()
    except:
        pass    
