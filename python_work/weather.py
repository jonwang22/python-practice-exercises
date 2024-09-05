# Choose an API from RapidAPI that interests you—make sure it has a free tier and simple authentication. 
# Write a Python script that makes a request to your selected API, using the appropriate endpoint and parameters to retrieve data. 
# Save the response data to a variable, and handle it as JSON to work with nested structures. 
# Extract a specific item from the nested dictionary in the response, and print a statement that meaningfully displays this information. 
# Have fun exploring the data you retrieve!

# Importing requests module to perform API requests.
import requests

# Keeping this here in case I want to use it.
# user_city = input("What city do you want to check the weather in?")

# I want to obtain the weather information from my IP address location. Its not an exact location where I am right now but it's close enough for now.
def get_weather_now():
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":"auto:ip"}

    headers = {
	    "x-rapidapi-key": "1800a143b9msh432dfcb7125690bp1283b8jsn4ddb72f7c6b0",
	    "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()

response = get_weather_now()

# # Test json for me to validate my commands for calling the information from the dictionary and not wasting API limits
# response = {
#     'location': {
#         'name': 'Leesburg',
#         'region': 'Virginia',
#         'country': 'United States of America',
#         'lat': 39.12,
#         'lon': -77.56,
#         'tz_id': 'America/New_York',
#         'localtime_epoch': 1725488251,
#         'localtime': '2024-09-04 18:17'
#         },
#     'current': {
#         'last_updated_epoch': 1725488100,
#         'last_updated': '2024-09-04 18:15',
#         'temp_c': 23.1,
#         'temp_f': 73.6,
#         'is_day': 1,
#         'condition': {
#             'text': 'Sunny',
#             'icon': '//cdn.weatherapi.com/weather/64x64/day/113.png',
#             'code': 1000
#         },
#         'wind_mph': 6.9,
#         'wind_kph': 11.2,
#         'wind_degree': 60,
#         'wind_dir': 'ENE',
#         'pressure_mb': 1029.0,
#         'pressure_in': 30.39,
#         'precip_mm': 0.0,
#         'precip_in': 0.0,
#         'humidity': 50,
#         'cloud': 0,
#         'feelslike_c': 24.6,
#         'feelslike_f': 76.3,
#         'windchill_c': 21.6,
#         'windchill_f': 70.9,
#         'heatindex_c': 22.1,
#         'heatindex_f': 71.9,
#         'dewpoint_c': 10.1,
#         'dewpoint_f': 50.2,
#         'vis_km': 16.0,
#         'vis_miles': 9.0,
#         'uv': 5.0,
#         'gust_mph': 9.8,
#         'gust_kph': 15.8
#         }
#     }

# Based off the Json output, I have 2 keys that have dictionary values and another dictionary value in the key condition under current key.
# I want to take this output and extract the name of the city, the region (state), country and local time.
# I also want to extract the current temperature in Celsius and Fahrenheit. 
# I also want to extract the Conditions right now which is under key current, value key condition, value text
# I also want to show the Feels Like temperature in Celsius and Fahrenheit. These are straight key value pairs in the parent dictionary.

# Lets extract the City, I need to call the dictionary, and pull the location key and access the nested dictionary in the value, and pull the value stored with name key
city = response["location"]["name"]
state = response["location"]["region"]
country = response["location"]["country"]
localtime = response["location"]["localtime"]
condition = response["current"]["condition"]["text"]
current_tempf = response["current"]["temp_f"]
current_tempc = response["current"]["temp_c"]
feels_tempf = response["current"]["feelslike_f"]
feels_tempc = response["current"]["feelslike_c"]


print(f"Based off of your IP Address, it is currently {condition} in {city}, {state}, {country}.")
print(f"The time is currently {localtime}.")
print(f"The current temperature is {current_tempf}F, or {current_tempc}C.")
print(f"Factoring in other conditions, the temperature feels like {feels_tempf}F, or {feels_tempc}C.")