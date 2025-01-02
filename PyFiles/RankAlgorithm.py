import pandas as pd 

type_chart = pd.read_csv("Data/typing_chart.csv",index_col=0) #column by column is defensive, row by row is offensive
type_per_gen = pd.read_excel("Data/PokemonCompleteStats.xlsx", 2) #2 is the index of the sheet


type_per_gen = type_per_gen.drop(columns=["Unnamed: 0"],axis=1)
type_per_gen = type_per_gen.drop([0,1],axis=0)
type_per_gen.columns = type_per_gen.iloc[0]
type_per_gen = type_per_gen[1:]

print(type_chart)
# print(type_per_gen)

for i in type_chart.iterrows(): 
     print(i[1])