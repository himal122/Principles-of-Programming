# Electricity bill
# Practical 6, Part 3
# author your name

previousMeterReading = int(input("\n Enter previous meter reading: "))
currentMeterReading = int(input("\n Enter current meter reading: "))
day = int(input("\n Enter the day of the meter reading: "))
month = int(input("\n Enter the month of the meter reading: "))

# Input Validation

# previous meter reading within range 0..9999
if (previousMeterReading < 0 or previousMeterReading > 9999):    
 print("Error: previous meter reading out of range \n")
      

#current meter reading within range 0..9999
if (currentMeterReading < 0 or currentMeterReading > 9999):
 print("Error: current meter reading out of range \n")

 
# previous not greater than present
if (previousMeterReading > currentMeterReading):   
 print("Error: previous reading is more than present reading \n")
        
# electricity used not more than 1000
if (currentMeterReading - previousMeterReading > 1000):  
 print("Error: electricity used more than 1000 \n")
       
# month in range 1..12
if (month < 1 or month > 12):
 print("Error: month out of range 1..12 \n")
       
#days in month must be correct (Jan, March etc)  
if ((month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) 
     and (day < 1 or day > 31)): 
 print("Error: day out of range 1..31 \n")
    
#days in month must be correct (Apr, June etc)
if ((month == 4 or month == 6 or month == 9 or month == 11) and (day < 1 or day > 30)):
 print("Error: day out of range 1..30 \n")
        
        
#days in month must be correct (Feb assuming 29 days) 
if (month == 2 and (day < 1 or day > 29)): 
 print("Error: day out of range 1..29 \n")
    
