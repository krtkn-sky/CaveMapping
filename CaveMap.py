import folium 
import pandas

data = pandas.read_csv("/home/akn29/Desktop/CaveMapping/Caves.csv")
lat = list(data[" Latitude"])
lon = list(data[" Longitude"])
names = list(data[" Cave Name"])

map = folium.Map(location=[23.542137394,78.295198388],
                 zoom_start=8,
                 tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt,ln,nm in zip(lat,lon,names):
    fg.add_child(folium.Marker(location=[lt,ln],
                               popup=str(nm),
                               icon=folium.Icon(color="red")))
    
map.add_child(fg)
map.save("Caves.html")

