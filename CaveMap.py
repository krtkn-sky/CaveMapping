import folium 
import pandas

data = pandas.read_csv("Caves.txt")
lat = list(data["Latitude"])
lon = list(data["Longitude"])

print(lat)
print(lon)