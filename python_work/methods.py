server_config = {
    "hostname": "Kura-server",         
    "ip_address": ["192.168.1.10"],         
    "port": 8080,   
    "uptime": 99.98,              
    "ssh_enabled": True,                  
    "supported_protocols": ["HTTP", "HTTPS"]
}

# print(server_config["ip_address"])
# print(type(server_config["ip_address"]))

server_config["ip_address"].append("123.0.0.12")

print(server_config["ip_address"])

server_config["ip_address"].remove("192.168.1.10")
print(server_config["ip_address"])

print(server_config.keys())
print(server_config.values())

