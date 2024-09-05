# Write a Python function that calculates the uptime percentage of a service based on the total number of hours and the number of hours the service was down.
# The function should take 2 parameters(total hours and down hours, inputted when the function is run).
# Lastly, the function should return the uptime percentage rounded to two decimal places.

# Setting user inputs for total hours and downtime hours
total = int(input("What is the total amount of hours your service has been available? "))
downtime = int(input("How many hours has your service been down? "))

# I need a function that takes 2 parameters
def uptime_check(total, downtime):
    # I need to figure out the uptime percentage
    # For uptime, its the amount of time that our service is up and running. 
    # I need total - downtime to get total hours uptime.
    # I need to then find the percentage of uptime over total hours times 100. 
    uptime = total - downtime
    percent_up = uptime/total * 100
    return percent_up
    # print(f"Your uptime percentage is {percent_up:.2f}%")

uptime = uptime_check(total, downtime)
print(f"Your uptime percentage is {uptime:.2f}%")