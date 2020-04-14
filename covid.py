import http
import json
import requests

conn = http.client.HTTPSConnection('api.covid19api.com')
conn.request('GET', '/live/country/united-kingdom/status/deaths')
    
response = conn.getresponse()
myJson = json.load(response)

province_list = []
deaths = 0

# Add all items from JSON to an array
for item in myJson:
    province_details = {"province": None, "deaths": None}
    province_details['province'] = item['Province']
    province_details['deaths'] = item['Deaths']
    province_list.append(province_details)

# Filter the array to find numbers for the whole of the UK
# Also for the latest day
for province in province_list:
    if province['province'] == "" and province['deaths'] > deaths:
        deaths = province['deaths']

##################################### POST TO DISCORD ############################################

message = "As of today, in the UK, " + str(deaths) + " people have died of coronavirus 🦠 RIP ⛪"       

url = '/api/channels/CHANNEL/messages'
params = {'content': message}
headers = {
    'Authorization': 'Bot SECRET',
    'Content-Type': 'application/json',
    'User-Agent': 'DiscordBot (FERST, 1.0)'
}

conn = http.client.HTTPSConnection('discordapp.com')
conn.request('POST', url, json.dumps(params), headers)

response = conn.getresponse()