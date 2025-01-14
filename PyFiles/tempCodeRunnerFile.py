print(type_chart)
# #iterrows is offensive 
# for index, row in type_chart.iterrows(): 
#     stat_calculate = 0
#     if row == 0: #Neutral atk 
#         stat_calculate += 1 
#     elif row == 0.5: #not v effective
#         stat_calculate -= 1
#     elif row == 2: #super effective
#         stat_calculate += 2 
#     else: #no effect 
#         stat_calculate -= 2
#     typing.append([index,"Offensive",stat_calculate,"Defensive",""])


# print(typing)