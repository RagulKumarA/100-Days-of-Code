import requests
import datetime
MY_LAT = 51.507351
MY_LONG = -0.127758

parameter = {
    "lat": MY_LAT
    , "lng": MY_LONG

}

response = requests.get(url="https://api.sunrise-sunset.org/json")
response.raise_for_status()
data = response.json()

sunrise = int(data["result"]["sunrise"].split("T")[1].split(":"))
sunset = int(data["result"]["sunset"].split("T")[1].split(":"))
time_now = datetime.datetime.now()
    
print(sunrise)
print(sunset)
print(time_now.time())