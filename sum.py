import pandas as pd

# load data Deel 1 - Noord-Holland & Zuid-Holland
ConnectiesHolland = pd.read_csv("Data-deel1/ConnectiesHolland.csv")
StationsHolland = pd.read_csv("Data-deel1/StationsHolland.csv")

# load data deel 2 - Heel NL
ConnectiesNationaal = pd.read_csv("Data-deel2/ConnectiesNationaal.csv")
StationsNationaal = pd.read_csv("Data-deel2/StationsNationaal.csv")

# Sum up the values in a specific column (e.g., 'column_name')
sum = ConnectiesHolland['distance'].sum()
print(sum)

sum2 = ConnectiesNationaal['distance'].sum()
print(sum2)