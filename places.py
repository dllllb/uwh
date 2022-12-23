import pandas as pd

import folium

map = folium.Map(location=[30, -40], zoom_start=2)

places = pd.read_xml('uwh.xml', xpath='.//row', parser='etree')

for i, r in places.iterrows():
    color = 'green' if r.category == 'Natural' else 'blue'

    popup = folium.Popup(r.short_description, max_width=512)
    folium.CircleMarker(
        location=(r.latitude, r.longitude),
        radius=1,
        popup=popup,
        color=color,
        tooltip=r.site).add_to(map)

map.save("places.html")
