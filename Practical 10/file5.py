#Copying only the second line from source to destination
try:
    f1 = open("d:\Rakib\PythonCode\Python programming\practical10\myFile1.txt", "r")
except FileNotFoundError as exp:
    print("Source file Not found")
    print(exp)
else:
    content = f1.readlines() 


f2 = open ("d:\Rakib\PythonCode\Python programming\practical10\yourFile.txt", "w")
count = 0
for line in content:
     if count == 2:
         f2.write(line)
     count = count + 1
f2.close()
f2 = open ("d:\Rakib\PythonCode\Python programming\practical10\yourFile.txt")
print(f2.read())