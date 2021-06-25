import requests
import urllib3

# Disable warning for unverified SSL certificates
urllib3.disable_warnings()

host = "10.10.20.48"
port = 443
username = "developer"
password = "C1sco12345"

url = f"https://{host}:{port}/restconf/data/ietf-interfaces:interfaces"

headers = {
       "Content-Type": "application/yang-data+json",
       "Accept": "application/yang-data+json",
}


def get_interfaces():
    response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    if response.status_code != 200:
        print(f"Error {response.status_code}")
    return response.json()


def show_interfaces(data):
    interface_list = data['ietf-interfaces:interfaces']['interface']
    for port in interface_list:
        #print(port)
        interface_name = port['name']
        interface_desc = port['description']
        #print(f"{interface_name}: {interface_desc}")

def config_interface(num, description, ip, mask):
    data = {"ietf-interfaces:interfaces": {
                    "name": f"GigabitEthernet{num}",
                    "description": description,
                    "type": "iana-if-type:ethernetCsmacd",
                    "enabled": true,
                    "ietf-ip:ipv4": {
                        "address": [
                            {
                                "ip": ip,
                                "netmask": mask
                            }
                        ]
                    },
                }},
    print(data)
    response = requests.put(url +f'/interface=GigabitEthernet{num}',
                          headers =headers, auth=(username, password),
                          verify=false, json=data


if __name__ == "__main__":
    data = get_interfaces()
    show_interfaces(data)

    num=int(input('geef een interface nummer: ')

    while num != 1:
        description = input('geef een omschrijving van het interface')
        ip = input('geef het ipv4 add')
        mask = input('geef het subnetmask')
        config_interface(num, description, ip, mask)
    else:


#Git comment





