import requests
import sqlite3





start_time = input('Enter the start time: ')
end_time = input('Enter the end time: ')
latitude = input('Enter the latitude: ')
longitude = input('Enter the longitude: ')
max_radius_km = input('Enter the maxradiuskm: ')
min_magnitude = input('Enter the minmagnitude: ')

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
response = requests.get(url, headers={'Accept':'application/json'}, params={
    'format':'geojson',
    'starttime': start_time,
    'endtime': end_time,
    'latitude': latitude,
    'longitude': longitude,
    'maxradiuskm': max_radius_km,
    'minmagnitude': min_magnitude
})

data = response.json()
earthquake_list = data['features']
count = 0
for earthquake in earthquake_list:
    count += 1
    print(f"{count}. Place: {earthquake['properties']['place']}. Magnitude: {earthquake['properties']['mag']}")