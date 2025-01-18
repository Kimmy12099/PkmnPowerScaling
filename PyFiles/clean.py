# Used for data cleaning Reading all CSV files and replacing all of the blank cells with a default value of -1, 
import os
import pandas as pd

CSV_DIR = './pokeapi/data/v2/csv'  

def replace_blanks_with_default(csv_dir, default_value=-1):
    for file_name in os.listdir(csv_dir):
        if file_name.endswith('.csv'):
            file_path = os.path.join(csv_dir, file_name)
            print(f"Processing file {file_name}...")

            try:
                df = pd.read_csv(file_path, on_bad_lines='warn') 
                
                # Replace blank cells with default value
                df.fillna(str(default_value), inplace=True)
                
                modified_file_path = os.path.join(csv_dir, f"{os.path.splitext(file_name)[0]}.csv")
                df.to_csv(modified_file_path, index=False)
                print(f"File {file_name} processed and saved as {os.path.basename(modified_file_path)}.")
            except Exception as e:
                print(f"Error processing file {file_name}: {e}")

if __name__ == "__main__":
    replace_blanks_with_default(CSV_DIR)
