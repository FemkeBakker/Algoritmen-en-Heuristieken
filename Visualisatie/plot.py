# Import libraries
# Benodigd: pandas, folium, seaborn

import pandas as pd
import folium
import random
import matplotlib.pyplot as plt
import seaborn as sns

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

# maak boxplot
def create_boxplot(data_, deel, xas, x_ticklabels, title):
    bp = sns.boxplot(data = data_, width = .5, showfliers = False, linewidth = 2.5, palette = 'colorblind',  showmeans = True, meanprops = {'marker': 'o', 'markerfacecolor':'white', 'markeredgecolor':"black"})
    bp.set(title=title)
    bp.set(xlabel=xas, ylabel="Score")
    bp.set_xticklabels(x_ticklabels)
    bp= plt.savefig('Visualisatie/boxplot{}.png'.format(deel))
    return bp

def generate_data(iteraties, path):
    data_tup = tuple()
    for iteratie in iteraties:
        # data_tup = (*data_tup, pd.read_csv('experiment\SimAnnealing-random-Nederland\iteratie{}.csv'.format(iteratie)))
        data_tup = (*data_tup, pd.read_csv("{}{}.csv".format(path,iteratie))['eind_score'])


    return data_tup
