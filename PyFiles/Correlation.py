import pandas as pd 

df = pd.read_excel('Data/PokemonCompleteStats.xlsx', sheet_name='PokemonCompleteStats')

 
correlation = round(df[['Evo_stage','basestattotal']].corr().iloc[0,1],3)

print("Correlation between Evolution Stage and Base Stat Total:")
print(correlation)
print("")

correlation2 = round(df[['Gen ID','basestattotal']].corr().iloc[0,1],3)

print("Correlation between Generation ID and Base Stat Total:")
print(correlation2)