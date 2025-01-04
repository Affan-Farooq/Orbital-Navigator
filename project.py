import os
import time
import smtplib
import datetime
import requests
from apiip import apiip
from dotenv import load_dotenv

load_dotenv()

def main():
    while True:
        latitude, longitude = get_geolocation()
        iss_coordinates = iss_location()

        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        print(f"{iss_coordinates}\n")

        if iss_in_vicinity(iss_coordinates[0], iss_coordinates[1], latitude, longitude) and valid_time(latitude, longitude):
            notify()

        time.sleep(60)


def get_geolocation():
    api_client = apiip(os.getenv("APIIP_KEY"))
    info = api_client.get_location({"ip": os.getenv("IP")})
    return info['latitude'], info['longitude']


def iss_location():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return float(data['iss_position']['latitude']), float(data['iss_position']['longitude'])
    else:
        return "Processing Error"


def iss_in_vicinity(iss_latitude, iss_longitude, current_latitude, current_longitude):
    if ((current_latitude - 5) <= iss_latitude <= (current_latitude + 5)) and ((current_longitude - 5) <= iss_longitude <= (current_longitude + 5)):
        return True
    return False


def valid_time(latitude, longitude):
    url = "https://sunrise-sunset-times.p.rapidapi.com/getSunriseAndSunset"
    current_date = str(datetime.datetime.today()).split()[0]
    querystring = {"date":current_date,"latitude":latitude,"longitude":longitude,"timeZoneId":"America/New_York"}

    headers = {
	    "X-RapidAPI-Key": os.getenv("RAPID_API_KEY"),
	    "X-RapidAPI-Host": "sunrise-sunset-times.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data=response.json()

    sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["sunset"].split("T")[1].split(":")[0])
    current_time = datetime.datetime.now().hour

    if current_time >= sunset or current_time <= sunrise:
        return True
    return False


def notify():
    MY_EMAIL = os.getenv("MY_EMAIL")
    MY_PASSWORD = os.getenv("MY_PASSWORD")

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject:Look Up!\n\nThe International Space Station is currently above you in the sky."
    )
    connection.quit()


if __name__ == "__main__":
    main()
