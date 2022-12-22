import pandas as pd

import folium

map = folium.Map()

places = pd.read_xml('uwh.xml', xpath='.//item', parser='etree')

for i, r in places.iterrows():
    popup = folium.Popup(r.description, max_width=512)
    folium.CircleMarker(
        location=(r.lat, r.long),
        radius=1,
        popup=popup,
        tooltip=r.title).add_to(map)

map.save("places.html")
