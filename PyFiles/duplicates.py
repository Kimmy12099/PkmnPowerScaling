import pandas as pd

df = pd.read_csv('Data/PokemonCompleteStats.csv')

def remove_duplicates(types_string):
    types_list = [t.strip() for t in types_string.split(',')]
    unique_types = set(types_list)  
    return ', '.join(unique_types)

df['combined_types'] = df['combined_types'].apply(remove_duplicates)

print("Cleaned combined_types:")
print(df[['identifier', 'combined_types']].head())  

df.to_csv('PokemonCompleteStats.csv', index=False)

print("Duplicates removed and changes saved to 'PokemonCompleteStats.csv'.")
