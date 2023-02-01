# Import libraries
# Benodigd: pandas, folium, seaborn

import pandas as pd
import folium
import random
import matplotlib.pyplot as plt
import seaborn as sns

def create_plot(trajecten, df_stations, deel):
    # Maak kaart ingezoomd op Nederland
    m = folium.Map(location=[52.37, 4.90], zoom_start = 8)	
    folium.TileLayer('cartodbpositron').add_to(m)

    # Zet voor elke rij in df een marker neer
    for i, row in df_stations.iterrows():
        folium.CircleMarker(location = [row['y'], row['x']], radius = 3, color = 'red', popup = row['station'], ).add_to(m)

    for traject in trajecten:
        traject_index = []

        # Zet lijst op goede volgorde
        for station in traject:
            for index, row in df_stations.iterrows():
                if row['station'] == station:
                    traject_index.append(row.name)
        
        # Zet goede volgorde in df
        df_traject = df_stations.loc[traject_index]

        # Geef elk traject een random kleur
        chars = '0123456789ABCDEF'
        r_color = ['#'+''.join(random.sample(chars,6)) for i in range(1)]
        
        # Voeg traject toe aan kaart
        folium.PolyLine(df_traject.iloc[:, [1,2]], color= r_color, weight=2.5, opacity=1).add_to(m)
    
    # Sla kaart op
    m.save('Visualisatie/map{}.html'.format(deel))

    return None

# Maak boxplot
def create_boxplot(data_, deel, xas, x_ticklabels, title):
    bp = sns.boxplot(data = data_, width = .5, showfliers = False, linewidth = 2.5, palette = 'colorblind',  showmeans = True, meanprops = {'marker': 'o', 'markerfacecolor':'white', 'markeredgecolor':"black"})
    bp.set(title=title)
    bp.set(xlabel=xas, ylabel="Score")
    bp.set_xticklabels(x_ticklabels)
    bp= plt.savefig('Visualisatie/boxplot{}.png'.format(deel))
    plt.close()
    return bp

# Functie om data tuple op te slaan voor boxplots
def generate_data(iteraties, path):
    data_tup = tuple()
    for iteratie in iteraties:
        # data_tup = (*data_tup, pd.read_csv('experiment\SimAnnealing-random-Nederland\iteratie{}.csv'.format(iteratie)))
        data_tup = (*data_tup, pd.read_csv("{}{}.csv".format(path,iteratie))['eind_score'])
    return data_tup
