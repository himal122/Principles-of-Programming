#Entering and Printing months from a list using while and for 
#loops
#Practical 6, Part 4
#author your name
months = []
index = 0
while index < 12:
 m = input("Enter a month: ")
 months.append(m)
 index += 1
print("Now printing the months you entered\n")
for x in range(12):
 print(months[x])
