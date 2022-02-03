import requests
import json

def get_stryket_api():
    match_id = [0,1,2,3,4,5,6,7,8,9,10,11,12]
    api_url = 'https://api.www.svenskaspel.se/draw/stryktipset/draws'
    stryket_data = requests.get(url=api_url).json()
    home_team = []
    away_team = []
    try:
        for i in match_id:
            home_team.append(stryket_data['draws'][0]['drawEvents'][i]['match']['participants'][0]['name'])
            away_team.append(stryket_data['draws'][0]['drawEvents'][i]['match']['participants'][1]['name'])
    except:
        print('Something went wrong')

    return home_team, away_team
        