import pandas as pd 
import plotly.express as px

type_chart = pd.read_csv("Data/typing_chart.csv",index_col=0) #column by column is defensive, row by row is offensive
type_per_gen = pd.read_excel("Data/PokemonCompleteStats.xlsx", 2) #2 is the index of the sheet
count_of_gen = pd.read_excel("Data/PokemonCompleteStats.xlsx")

type_per_gen = type_per_gen.drop(columns=["Unnamed: 0"],axis=1)
type_per_gen = type_per_gen.drop([0,1],axis=0)
type_per_gen.columns = type_per_gen.iloc[0]
type_per_gen = type_per_gen[1:]


count_dict = {i:0 for i in range(1,10)}

#num of Pokemon in each gen 
for value in count_of_gen['Gen ID']: 
    if value in count_dict:
        count_dict[value] += 1

'''
Ideal Output: 
list = { 
    Type1: {
        Offensive:, value, Defensive: value, Average Score: value
        }
    Type2: {
        Offensive:, value, Defensive: value, Average Score: value
        } 
    }

'''
typing = {}
type_chart = type_chart.fillna(5) #ran number, no significance, just cannot be 0 cause immunity 

#rows, offensive 
for index, row in type_chart.iterrows(): 
    offensive_calculate = 0
    defensive_calculate = 0
    for i in range(len(row)):
        if row.iloc[i] == 5: #Neutral atk 
            offensive_calculate += 1 
        elif row.iloc[i] == 0.5: #not very effective
            offensive_calculate -= 1
        elif row.iloc[i] == 2: #super effective
            offensive_calculate += 2 
        else: #no effect 
            offensive_calculate -= 2

    #columns, defensive 
    for i in range(len(type_chart.columns)): 
        if type_chart.iloc[i][index] == 5: #neutral 
            defensive_calculate += 1
        elif type_chart.iloc[i][index] == 0.5: #not very effective
            defensive_calculate += 1
        elif type_chart.iloc[i][index] == 2: #super effective
            defensive_calculate -= 2
        else: #no effect
            defensive_calculate += 2

    typing[index] = {
        "Offensive": offensive_calculate,
        "Defensive": defensive_calculate,
        "Average Score": (offensive_calculate + defensive_calculate)/2
    }

#sort types by average score (Lowest score --> highest score)
raw_stats_sort = sorted(typing.items(), key=lambda x: x[1]['Average Score'])



'''
Generation ideal output: 
    {
    Generation 1: {Type, #Types in gen}, {Type, #Types in gen}...
}
    Generation 2: {Type, #Types in gen}, {Type, #Types in gen}...
}
'''
generation = {}

for index, row in type_per_gen.iterrows():
    gen = row.iloc[0]
    types = row.index[1:]
    count = row.values[1:]
    generation[gen] = {t: c for t, c in zip(types, count)}

weighted_scores_by_gen = {}

for gen, data in generation.items():
    weighted_scores_by_gen[gen] = {}

    for type_name, type_count in data.items():
        avg_score = None

        for entry in raw_stats_sort:
            if entry[0] == type_name:
                avg_score = entry[1]['Average Score']
                break

        if avg_score is not None:
            weighted_score = avg_score * type_count 
            weighted_scores_by_gen[gen][type_name] = weighted_score


          
weighted_average_per_gen = {}

for gen, types in weighted_scores_by_gen.items():
    gen_num = int(gen.split(" ")[1])
    total_sum = sum(types.values())

    pokemon_count = count_dict[gen_num]
    weighted_average_per_gen[gen] = round(total_sum / pokemon_count,4)

print(weighted_average_per_gen)

type_avg_scores = [(type_name, data['Average Score']) for type_name, data in typing.items()]
type_avg_scores_df = pd.DataFrame(type_avg_scores, columns=['Type', 'Average Score'])

type_avg_scores_df = type_avg_scores_df.sort_values(by='Average Score', ascending=True)

fig_type_avg_score = px.bar(type_avg_scores_df, 
                            x='Type', 
                            y='Average Score', 
                            title="Ranking of Types by Average Score",
                            labels={'Average Score': 'Average Score', 'Type': 'Pokemon Type'},
                            color='Average Score',
                            color_continuous_scale='Viridis')
fig_type_avg_score.show()

weighted_avg_per_gen_df = pd.DataFrame(list(weighted_average_per_gen.items()), columns=['Generation', 'Weighted Average'])
weighted_avg_per_gen_df = weighted_avg_per_gen_df.sort_values(by='Weighted Average', ascending=False)

fig_weighted_avg_gen = px.bar(weighted_avg_per_gen_df, 
                               x='Generation', 
                               y='Weighted Average', 
                               title="Weighted Average per Generation For Types",
                               labels={'Weighted Average': 'Weighted Average', 'Generation': 'Generation'},
                               color='Weighted Average',
                               color_continuous_scale='Viridis')
fig_weighted_avg_gen.show()