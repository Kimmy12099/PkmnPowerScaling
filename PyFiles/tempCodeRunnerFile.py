import pandas as pd 

df = pd.read_excel("Data/PokemonCompleteStats.xlsx", sheet_name="PokemonCompleteStats")
df2 = pd.read_csv('Data/pokemon_species.csv')

df_merged = pd.merge(df,df2['evolves_from_species_id','is_baby','is_legendary','is_mythical']], on='id', how='left')

df_merged.to_csv('merged_pokemon.csv', index=False)
