import folium 
import pandas

data = pandas.read_csv("/home/akn29/Desktop/CaveMapping/Caves.csv")
lat = list(data[" Latitude"])
lon = list(data[" Longitude"])


map = folium.Map(location=[23.542137394,78.295198388],
                 zoom_start=6,
                 tiles="Stamen Terrain")

#print(lon)
#print(lat)
