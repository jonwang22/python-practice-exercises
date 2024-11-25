# Looking at statuses of services on the system
# Function to tell me what services are currently running
# make it human readable

processes = {
    "nginx": "running",
    "mysql": "stopped",
    "redis": "running",
    "mongodb": "stopped",
    "apache2": "running",
    "docker": "running",
    "kubelet": "stopped",
    "postgresql": "running",
    "elasticSearch": "running",
    "filebeat": "stopped",
    "logstash": "running",
    "grafana": "running",
    "prometheus": "stopped",
    "vault": "running",
    "jenkins": "stopped"
}

# print(processes["nginx"])

# working with dict
# iterate through dictionary - for loop
def running_services_check(dictionary):
    running_services = []
    for key, value in dictionary.items():
        if value == "running":
            # print(key)
            running_services.append(key)
    return running_services
# check value on each key if running, output key

running_services = running_services_check(processes)

# print(running_services)

for service in running_services:
    print(f"{service} is running.")