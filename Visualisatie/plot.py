# Import libraries
# Benodigd: pandas, folium

import pandas as pd
import folium
import random

def create_plot(trajecten, df_stations, deel):
    # Create map zoomed in on the Netherlands
    m = folium.Map(location=[52.37, 4.90], zoom_start = 8)	
    folium.TileLayer('cartodbpositron').add_to(m)

    # Loop through every row to add marker per station
    for i, row in df_stations.iterrows():
        folium.CircleMarker(location = [row['y'], row['x']], radius = 3, color = 'red', popup = row['station'], ).add_to(m)

    for traject in trajecten:
        traject_index = []

        # Get a list of indexes of the stations in the right order
        for station in traject:
            for index, row in df_stations.iterrows():
                if row['station'] == station:
                    traject_index.append(row.name)
        
        # Get a Dataframe of the stations in the right order
        df_traject = df_stations.loc[traject_index]

        # Create random colour for every traject
        chars = '0123456789ABCDEF'
        r_color = ['#'+''.join(random.sample(chars,6)) for i in range(1)]
        
        # Add traject to map
        folium.PolyLine(df_traject.iloc[:, [1,2]], color= r_color, weight=2.5, opacity=1).add_to(m)
    
    # Create map, store in map.html
    m.save('Visualisatie/map{}.html'.format(deel))

    return None


