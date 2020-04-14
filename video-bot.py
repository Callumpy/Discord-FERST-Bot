import datetime
import requests
import http
import json

now = datetime.datetime.now()

def select_video():
    if now.day == 31 and now.month == 3:
        return "https://www.youtube.com/watch?v=nLck4R3BcyM"

    if now.day != 1:
        return hmmgif()

    if now.month == 1:
        return "It's JANNUUARRRYYYYYYY FERRRSST\nHAPPY NEW YEAR " + now.year + "\nhttps://www.youtube.com/watch?v=dxwF1oFRUmg"
    elif now.month == 2:
        return "FEBRUARY FEEEEEEEEEEEEEERRRSTT https://www.youtube.com/watch?v=QLe0mdHZmIY"
    elif now.month == 3:
        return "MARCH FERST https://www.youtube.com/watch?v=D2-dDC3Qjl0"
    elif now.month == 4:
        return "APRIL FOOL, don't listen to other people https://www.youtube.com/watch?v=OqjEipldpFc"
    elif now.month == 5:
        return "MAY SOMETHINGH https://www.youtube.com/watch?v=jqAaJHP3GQE"
    elif now.month == 6:
        return "JUNE FEEEEEEEEEEEEEEEEEEEEEEEEEEERST https://www.youtube.com/watch?v=YarUmcSSmjM"
    elif now.month == 7:
        return "JULY https://www.youtube.com/watch?v=7J5QzqiKymI"
    elif now.month == 8:
        return "AUGUST FEEEEEERST https://www.youtube.com/watch?v=hkCADaZDpwY"
    elif now.month == 9:
        return "IT'S CALLUMS BIRTHDAY TOMORROW https://www.youtube.com/watch?v=DUogXC_Ec40"
    elif now.month == 10:
        return "OCTOBER FEST https://www.youtube.com/watch?v=J8f7oKeMstQ"
    elif now.month == 11:
        return "NOVENMBERRER FIRSST https://www.youtube.com/watch?v=BCGlmoEKcag"
    elif now.month == 12:
        return "CHRISTMAS THE FIRST https://www.youtube.com/watch?v=vZewrglKXHE"

def hmmgif():
    conn = http.client.HTTPSConnection('www.reddit.com')
    conn.request('GET', '/r/hmmmgifs/hot.json?limit=1')
    
    response = conn.getresponse()
    myJson = json.load(response)

    return myJson['data']['children'][0]['data']['url']

message = select_video()

url = '/api/channels/CHANNEL ID HERE/messages'
params = {'content': message}
headers = {
    'Authorization': 'Bot AUTH TOKEN HERE',
    'Content-Type': 'application/json',
    'User-Agent': 'DiscordBot (FERST, 1.0)'
}

conn = http.client.HTTPSConnection('discordapp.com')
conn.request('POST', url, json.dumps(params), headers)

response = conn.getresponse()
print(response.read())