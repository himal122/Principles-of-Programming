# match two DNA profiles represented using two one-dimensional arrays
# Practical 6, Part 4
# author R Abdur

size = 10
suspect = []  # declaring suspect list
criminal = []  # declaring criminal list

# read 10 input values into the suspect list from the keyboard

print("\n Enter the 10 gene chromosomes of the suspect one at a time and press Enter\n")
for i in range(size):
    element = float(input("Enter a real number: "))
    suspect.append(element)


# read 10 input values into the criminal list from the keyboard

print("\n Enter the 10 gene chromosomes of the criminal one at a time and press Enter\n")
for i in range(size):
    element = float(input("Enter a real number: "))
    criminal.append(element)

# match two profiles
def matchingProfiles(suspect,criminal):
    match = True    
    for i in range(size):
       if (suspect[i] != criminal[i]):
         match = False
    
    return match
# display matching result

if (matchingProfiles(suspect,criminal)):
    print("\n The two profiles match! \n")
else:
    print("\n The two profiles don't match! \n")
