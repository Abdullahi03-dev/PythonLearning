import requests

apiKey = 'bec2caaeeb1f2422770f48f49e975a86'
apiUrl = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params={
        'q':city,
        'appid':apiKey,
        'units':'metric'
    }
    response=requests.get(apiUrl,params=params)
    data=response.json()
    
    if response.status_code==200:
        city_name=data['name']
        country=data['sys']['country']
        temp=data['main']['temp']
        desc=data['weather'][0]['description']
        
        return f"{city_name},{country}\n Temp: {temp}c\n weather: {desc}"
    else:
        return f"Error:{data['message']}"
    

print(get_weather('adamawa'))
        