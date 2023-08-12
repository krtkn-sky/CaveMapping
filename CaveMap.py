import folium 
import pandas

data = pandas.read_csv("/home/akn29/Desktop/CaveMapping/Caves.csv")
lat = list(data[" Latitude"])
lon = list(data[" Longitude"])
names = list(data[" Cave Name"])
elev = list(data[" Elevation (m)"])

map = folium.Map(location=[23.542137394,78.295198388],
                 zoom_start=4,
                 tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt,ln,nm,el in zip(lat,lon,names,elev):
    fg.add_child(folium.Marker(location=[lt,ln],
                               popup=str(nm)+" "+str(el)+"m",
                               icon=folium.Icon(color="red")))
    
map.add_child(fg)
map.save("Caves.html")

