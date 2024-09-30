import requests
import math
import json

def filter_names(cond) -> str: 
    switch = {
        "Drizzle" : "Rain",
        "Haze" : "Mist",
        "Fog" : "Mist",   
    }.get(cond)

    return cond if switch is None else switch

def weather() -> tuple:
    API = 'c0ecc18fdeb54628f312943586f2c573'
    try:
        res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Мариуполь&appid={API}')
        data = json.loads(res.text)

        temp_raw = math.floor(data["main"]["temp"] - 273.15)
        temp = f"+{temp_raw}" if temp_raw > 0 else temp_raw
        
        description = filter_names(str(data["weather"][0]["main"]))
        return (temp, description)

    except Exception as error:
        print(error) 
        return ('error', 'error') 
