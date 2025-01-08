#Print monthly expenditure
#Practical 6, Part 2 (c)
#author your name

foodExpenses = float(input("\n Enter food expenses: "))
leisureExpenses = float(input("\n Enter leisure expenses: "))
clothesExpenses = float(input("\n Enter clothes expenses: "))
accommodationExpenses = int(input("\n Enter accommodation expenses: "))
travelExpenses = int(input("\n Enter travel expenses: "))

totalSpent = foodExpenses + leisureExpenses + clothesExpenses + accommodationExpenses + travelExpenses

print("\n The total expenditure this month was: ", totalSpent)