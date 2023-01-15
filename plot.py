# Import libraries
# Benodigd: pandas, folium

import pandas as pd
import folium

# Import csv naar dataframe
StationsHolland = pd.read_csv("Data-deel1/StationsHolland.csv")
# print(StationsHolland.head()) check

# Creeër kaart ingezoomd op Nederland
m = folium.Map(location=[52.37, 4.90], zoom_start = 8)	
folium.TileLayer('cartodbpositron').add_to(m)


# Loop door elke rij in df om markers toe te voegen
for i, row in StationsHolland.iterrows():
    folium.CircleMarker(location = [row['y'], row['x']], radius = 3, color = 'red', popup = row['station'], ).add_to(m)

#[Castricum = 7, Zaandam = 21, Hoorn = 15, Alkmaar = 0]
selected_rows = [7, 21, 15, 0]
df_traject1 = StationsHolland.loc[selected_rows]
# print(df_traject1.head(4)) # check

# Voeg verbindingen toe
folium.PolyLine(df_traject1.iloc[:, [1,2]], color='black', weight=2.5, opacity=1).add_to(m)

# Map opslaan in aparte file (VScode weigert iets te plotten)
m.save('map.html')

