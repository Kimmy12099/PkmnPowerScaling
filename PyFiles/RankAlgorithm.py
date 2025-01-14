import pandas as pd 

type_chart = pd.read_csv("Data/typing_chart.csv",index_col=0) #column by column is defensive, row by row is offensive
type_per_gen = pd.read_excel("Data/PokemonCompleteStats.xlsx", 2) #2 is the index of the sheet


type_per_gen = type_per_gen.drop(columns=["Unnamed: 0"],axis=1)
type_per_gen = type_per_gen.drop([0,1],axis=0)
type_per_gen.columns = type_per_gen.iloc[0]
type_per_gen = type_per_gen[1:]

# print(type_chart)
# print(type_per_gen)

'''
Output: 
list [
     [Type, "Offensive", Offensive value, "Defensive", Defensive value, "Average Score", Average Score]
     [Type, "Offensive", Offensive value, "Defensive", Defensive value, "Average Score", Average Score]
    ... 
    ]
'''
typing = []
type_chart = type_chart.fillna(5) #ran number, no significance, just cannot be 0 cause immunity 

#iterrows is offensive 
for index, row in type_chart.iterrows(): 
    offensive_calculate = 0
    defensive_calculate = 0
    for i in range(len(row)):
        if row[i] == 5: #Neutral atk 
            offensive_calculate += 1 
        elif row[i] == 0.5: #not v effective
            offensive_calculate -= 1
        elif row[i] == 2: #super effective
            offensive_calculate += 2 
        else: #no effect 
            offensive_calculate -= 2

    #columns, defensive 
    for i in range(len(type_chart.columns)): 
        if type_chart.iloc[i][index] == 5: #neutral 
            defensive_calculate += 1
        elif type_chart.iloc[i][index] == 0.5: #not v effective
            defensive_calculate += 1
        elif type_chart.iloc[i][index] == 2: #super effective
            defensive_calculate -= 2
        else: #no effect
            defensive_calculate += 2

    typing.append([index,"Offensive",offensive_calculate,"Defensive",defensive_calculate,"Average Score", (offensive_calculate+defensive_calculate)/2])


#sort by average score 
#Weighted average per generation calculator 
#Some type of visualization 

print(typing) 
