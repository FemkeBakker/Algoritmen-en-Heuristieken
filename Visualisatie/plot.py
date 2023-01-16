# Import libraries
# Benodigd: pandas, folium

import pandas as pd
import folium


def create_plot(trajecten, df_stations, deel):
    # Creeër kaart ingezoomd op Nederland
    m = folium.Map(location=[52.37, 4.90], zoom_start = 8)	
    folium.TileLayer('cartodbpositron').add_to(m)

    # Loop door elke rij in df om markers toe te voegen
    for i, row in df_stations.iterrows():
        folium.CircleMarker(location = [row['y'], row['x']], radius = 3, color = 'red', popup = row['station'], ).add_to(m)

    for traject in trajecten:
        traject_index = []

        # get a list of indexes of the stations in the right order
        for station in traject:
            for index, row in df_stations.iterrows():
                if row['station'] == station:
                    traject_index.append(row.name)
        
        # get a Dataframe of the stations in the right order
        df_traject = df_stations.loc[traject_index]

        # add traject to map
        folium.PolyLine(df_traject.iloc[:, [1,2]], color='black', weight=2.5, opacity=1).add_to(m)
    
    # create map, store in map.html
    m.save('Visualisatie/map{}.html'.format(deel))

    return None


