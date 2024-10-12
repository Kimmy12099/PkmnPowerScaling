import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('Data/PokemonCompleteStats.csv')

# Function to remove duplicates within each row
def remove_duplicates(types_string):
    # Split the string by comma, strip whitespace, and convert to a set to remove duplicates
    types_list = [t.strip() for t in types_string.split(',')]
    unique_types = set(types_list)  # Remove duplicates
    # Join the unique types back into a string
    return ', '.join(unique_types)

# Apply the function to the combined_types column
df['combined_types'] = df['combined_types'].apply(remove_duplicates)

# Display the cleaned DataFrame (optional)
print("Cleaned combined_types:")
print(df[['identifier', 'combined_types']].head())  # Show the first few rows after cleaning

# Save the cleaned DataFrame back to the CSV file (overwrite the original)
df.to_csv('PokemonCompleteStats.csv', index=False)

print("Duplicates removed and changes saved to 'PokemonCompleteStats.csv'.")
