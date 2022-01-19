import pandas as pd
from mapbox import Geocoder
import csv


# read lons and lats

path = ""
dfs = pd.read_excel(path)
reference = pd.read_excel("")

token = ""
geocoder = Geocoder(access_token=token)

lats = []
lons = []
for i in range(len(dfs)):
    response = geocoder.forward(dfs['address'][i])
    collection = response.json()
    lon, lat = collection['features'][0]['geometry']['coordinates']
    lats.append(lat)
    lons.append(lon)
    print(i)

dfs["lats"] = lats
dfs["lons"] = lons

dfs.to_csv('lon&lat.csv', index=False)


