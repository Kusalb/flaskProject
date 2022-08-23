import ipaddress
import socket
from IPy import IP
import requests




# dns = socket.gethostbyname(website_name)
# print(dns)

#new:
def get_dns(website_name):
    return socket.gethostbyname(website_name)


#another tool
def check_ip(address):
    try:
        IP(address)
        return address
    except ValueError:
        return socket.gethostbyname(address)


def scan(target):
    ip_address = check_ip(target)
    print(f"\n[-_0 Scanning Target] {str(target)}")
    result=[]
    for port in range(1, 100):
        rslt = scan_port(ip_address, port)
        if rslt:
            result.append(rslt)
    print("sacn", result)
    return result


def scan_port(ipaddress_, port_):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress_, port_))
        print(f'[+] Port {str(port_)} is open')
        return f'[+] Port {str(port_)} is open'
    except:
        pass


def scan_targets(website_name):
    targets = website_name
    result=[]
    if ',' in targets:
        for target in targets.split(','):
            rs = scan(target.strip(' '))
            result.append(rs)
        print("scan targets",result)
        return result
    else:
        rs = scan(targets)
        return rs
    print("scan finished")



#another tool




def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location(website_name):
    ip_address = get_dns(website_name)
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data



#another tool




# the domain to scan for subdomains









# domain = website_name
# # read all subdomains
# file = open("subdomains.txt")
# # read all content
# content = file.read()
# # split by new lines
# subdomains = content.splitlines()
# # a list of discovered subdomains
# discovered_subdomains = []
# for subdomain in subdomains:
#     # construct the url
#     url = f"http://{subdomain}.{domain}"
#     try:
#         # if this raises an ERROR, that means the subdomain does not exist
#         requests.get(url)
#     except requests.ConnectionError:
#         # if the subdomain does not exist, just pass, print nothing
#         pass
#     else:
#         print("[+] Discovered subdomain:", url)
#         # append the discovered subdomain to our list
#         discovered_subdomains.append(url)
# 		# save the discovered subdomains into a file




def scan_sub_domains(website_name):
    domain = website_name
    # read all subdomains
    file = open("subdomains.txt")
    # read all content
    content = file.read()
    # split by new lines
    subdomains = content.splitlines()
    # a list of discovered subdomains
    discovered_subdomains = []
    for subdomain in subdomains:
        # construct the url
        url = f"http://{subdomain}.{domain}"
        try:
            # if this raises an ERROR, that means the subdomain does not exist
            requests.get(url)
        except requests.ConnectionError:
            # if the subdomain does not exist, just pass, print nothing
            pass
        else:
            print("[+] Discovered subdomain:", url)
            # append the discovered subdomain to our list
            discovered_subdomains.append(url)
            # save the discovered subdomains into a file



def run_program(url):
    website_name = url
    dns =  get_dns(website_name)
    ip_address =  get_ip()
    location =  get_location(website_name)
    print(dns,ip_address,location)
    rs = scan_targets(website_name)
    data=location
    data["dns"]=dns
    data["ipaddr"]=ip_address
    data["vunerability"]=rs
    return data
    # print(scan_sub_domains(website_name))