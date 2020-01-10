import folium
import pandas

data=pandas.read_csv("/home/sumit/mapping/Volcanoes_USA.txt")
City=list(data["LOCATION"])
Lat=list(data["LAT"])
log=list(data["LON"])
map=folium.Map([28.61, 77.21],zoom_starts=8,Tiles="Mapbox bright")
fg=folium.FeatureGroup(Name="My Map")
for ct, lt,ln in zip(City,Lat,log):
    fg.add_child(folium.Marker(location=[lt,ln],popup=ct,icon=folium.Icon(colour='blue')))
map.add_child(fg)
map.save("Map1.html")
