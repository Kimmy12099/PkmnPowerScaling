import pandas as pd 

#Reading in the type chart and the number of types per generation
type_chart = pd.read_csv("C:\Users\ianki\Desktop\PkmnPowerScaling\Data\typing_chart") 
type_per_gen = pd.read_excel("C:\Users\ianki\Desktop\PkmnPowerScaling\Data\PokemonCompleteStats.xlsx", 2) #2 is the index of the sheet


#1. Access type chart and # of type per gen for the rank algorithm
#2. See if you can find a way to go through each column and store each type into a variable (offensive value)
#3. See if you can find a way to go through each row and store each type into a variable (defensive value)
#4. Add up & average the offensive and defensive values to get the total value per pokemon type (But keep #2 and 3 for data visualization purposes)
#5. Rank the total value per pokemon type from highest to lowest and put values on each typing  
#6 Then go to the type per gen column, and calculate their total value per gen based on the amount of X type pokemon introduced in that gen & what value I put on that type
#7 Then go rank the generations based on #6 values from highest to lowest and put values on each generation
#8 Data visualization for #2, #3, #4, #7 (smth like matplotlib or seaborn) 