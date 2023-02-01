# Import libraries
# Benodigd: pandas, folium, seaborn

import pandas as pd
import folium
import random
import matplotlib.pyplot as plt
import seaborn as sns
import ast
import os

def create_plot(trajecten, df_stations, deel, naam):
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
    path = "Visualisatie/kaarten/{}".format(deel)
    if not os.path.exists(path):
        os.makedirs(path)

    m.save('{}/{}.html'.format(path, naam))

    return None

# Maak boxplot
def create_boxplot(data_, deel, xas, x_ticklabels, title, map):
    bp = sns.boxplot(data = data_, width = .5, showfliers = False, linewidth = 2.5, palette = 'colorblind',  showmeans = True, meanprops = {'marker': 'o', 'markerfacecolor':'white', 'markeredgecolor':"black"})
    bp.set(title=title)
    bp.set(xlabel=xas, ylabel="Score")
    bp.set_xticklabels(x_ticklabels)

    path = "Visualisatie/{}".format(map)
    if not os.path.exists(path):
        os.makedirs(path)

    bp= plt.savefig('{}/boxplot{}.png'.format(path, deel))
    plt.close()
    return bp

# Functie om data tuple op te slaan voor boxplots
def generate_data(iteraties, path):
    data_tup = tuple()
    for iteratie in iteraties:
        data_tup = (*data_tup, pd.read_csv("{}{}.csv".format(path,iteratie))['eind_score'])
    return data_tup

# Functie returnt de data en labels van de optimale versies van alle algoritmes in Holland
def generate_data_vergelijking_holland():
    HC_7 = pd.read_csv("experiment/HillClimber-7langste-Holland/iteratie10000.csv")['eind_score']
    HC_random = pd.read_csv("experiment/HillClimber-random-Holland/iteratie8000.csv")['eind_score']
    HC_greedy = pd.read_csv("experiment/HillClimber-Greedy_con-Holland/iteratie200.csv")['eind_score']
    Greedy_con = pd.read_csv("experiment/greedy/Holland.csv")['eind_score']
    random_baseline = pd.read_csv("experiment/Random_baseline/Holland.csv")['eind_score']
    SA = pd.read_csv("experiment/SimAnnealing-random-Holland, temp30/iteratie20000+temp30.csv")['eind_score']

    # maak tuple van alle data
    data = (HC_7, HC_random, HC_greedy, Greedy_con, SA, random_baseline)
    
    labels = ['HC_7', "HC_random", "HC_greedy", "Greedy_con", "SA", "Random"]
    return data, labels

# Functie returnt de data en labels van de optimale versies van alle algoritmes in Nederland
def generate_data_vergelijking_nl():
    HC_7 = pd.read_csv("experiment/HillClimber-7langste-Nederland/iteratie15000.csv")['eind_score']
    HC_random = pd.read_csv("experiment/HillClimber-random-Nederland/iteratie15000.csv")['eind_score']
    HC_greedy = pd.read_csv("experiment/HillClimber-Greedy_con-Nederland/iteratie200.csv")['eind_score']
    Greedy_con  = pd.read_csv("experiment/greedy/Nederland.csv")["eind_score"]
    SA = pd.read_csv("experiment/SimAnnealing-random-temptest/iteratie20000+temp30.csv")['eind_score']

    # maak tuple van alle data 
    data = (HC_7, HC_random, HC_greedy, Greedy_con, SA)

    labels = ['HC_7', "HC_random", "HC_greedy", "Greedy_con", "SA"]

    return data, labels

# Functie maakt de kaart van de meegegeven oplossing
def best_solution_map(data, stations, iteratie, deel, naam):

    # selecteer de beste oplossing
    best = data[data['iteratie']==iteratie]['best_solution'].values[0]

    # zet de oplossing van string om naar list
    best = ast.literal_eval(best)

    create_plot(best, stations, deel, naam)
