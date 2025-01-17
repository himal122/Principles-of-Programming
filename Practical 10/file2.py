f1 = open("d:\Rakib\PythonCode\Python programming\practical10\myFile.txt", "r")
f2 = open ("d:\Rakib\PythonCode\Python programming\practical10\yourFile.txt", "w")
f2.write(f1.read()) 
f2.close()