# Identify blacklisted users that we don't want accessing our system
list = [
    {"name": "Laxmi", "ip": "192.168.1.1"},
    {"name": "Joe", "ip": "10.0.0.5"},
    {"name": "Kaia", "ip": "172.16.254.3"}
]

# What data type is blacklisted?
# print(type(blacklisted))
# What data type is {} within blacklisted?
# print(type(blacklisted[0]))
# How do we print the IP Addresses from blacklisted?
# print(blacklisted[0]["ip"])
# Can we automate these prints with a conditional statement?
ip_address = "172.16.254.3"

def matcher(ip_address, blacklist):
    for index in blacklist:
        #print(index["ip"])
        if ip_address == index["ip"]:
            print(f"IP Address matched {index['name']}")
        else:
            print(f"IP Address did not match",index['name'])

# Call the function
matcher("10.0.0.5",list)

