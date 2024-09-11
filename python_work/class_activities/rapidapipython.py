import requests

url = "https://livescore6.p.rapidapi.com/matches/v2/list-live"

querystring = {"Category":"tennis","Timezone":"-7"}

headers = {
	"x-rapidapi-key": "1800a143b9msh432dfcb7125690bp1283b8jsn4ddb72f7c6b0",
	"x-rapidapi-host": "livescore6.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

raw = response.text

jsonoutput = response.json()

# print(response)
# print(response.json())
# print(response.text)

for items in jsonoutput["Stages"]:
    print({items.get("Sid")})

# print(type(raw))
# print(jsonoutput.keys())
# print(jsonoutput.values())