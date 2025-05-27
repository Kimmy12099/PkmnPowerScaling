import pandas as pd
import numpy as np

df = pd.read_excel("Data/PokemonCompleteStats.xlsx", sheet_name="PokemonCompleteStats")

df.columns = df.columns.str.strip()

# Create a dictionary from pokemon_id to evolves_from_species_id
id_to_evolves_from = dict(zip(df['pokemon_id'], df['evolves_from_species_id']))

def get_evo_stage(row):
    evolves_from = row['evolves_from_species_id']
    if pd.isna(evolves_from):
        return 1  # Base form
    parent_evolves_from = id_to_evolves_from.get(evolves_from, np.nan)
    if pd.isna(parent_evolves_from):
        return 2  # Evolves from a base form
    else:
        return 3  # Evolves from a Pokémon that itself evolves

df['Evo_stage'] = df.apply(get_evo_stage, axis=1)

df.to_excel("Data/PokemonCompleteStats_with_EvoStage.xlsx", index=False)
