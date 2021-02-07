'''
Given the below subdomain list, write a script (Using bash/Python) to read the URLs within and create an output of the 
following format (Domain | Resolved IP | HTTP Code) and generate a json response out of it.

'''
import socket
import requests 


domains=['rdandx.com','freelancer1.rdandx.com','freelancer2.rdandx.com','old.rdandx.coms']
addr=''
domain=''
response_code=''
for domain in domains:
     
    try:
        domain=domain
        response = requests.get('http://'+domain)
        if(response.status_code==200):          
            addr = socket.gethostbyname(domain)
        response_code=response.status_code
        result={'DOMAIN' : domain, 'IP_RESLOVE' : addr, 'RESPONSE_CODE': response_code}
        print(result)

    
    except :
        result={'DOMAIN' : domain, 'IP_RESLOVE' : 'Dns Not Found', 'RESPONSE_CODE': response_code}
        print(result)



    