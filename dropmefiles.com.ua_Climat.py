import requests

def is_rain():

    appid = 'fd5526d430603cff50380ba1bcf3fac4'

    try:
        res = requests.get("https://api.openweathermap.org/data/2.5/weather",
                    params={'lat': 48.716385, 'lon': 21.261074, 'appid': appid})
        data = res.json()
        return(data['weather'][0]['description'] == "Rain")
        
    except Exception as e:
        print("Exception (weather):", e)
        pass