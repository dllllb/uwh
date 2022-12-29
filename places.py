import pandas as pd

import folium

map = folium.Map(location=[30, -40], zoom_start=2)

places = pd.read_xml('uwh.xml', xpath='.//row', parser='etree')

for i, r in places.iterrows():
    color = 'green' if r.category == 'Natural' else 'blue'

    popup = f"""
    <div style="display: table">
        <div style="display: flex; padding: 4px; float: left; width: 15%">
            <a href="{r.http_url}">
                <img style="max-height: 100%; max-width: 100%; border: 5px" align="left" src="{r.image_url}" />
            </a>
        </div>
        <div style="display: flex; float: left; width: 85%">
            {r.short_description}
        </p>
    </div>
    """

    popup = folium.Popup(popup, max_width=512)
    folium.CircleMarker(
        location=(r.latitude, r.longitude),
        radius=1,
        popup=popup,
        color=color,
        tooltip=r.site).add_to(map)

map.save("places.html")
