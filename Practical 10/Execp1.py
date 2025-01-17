def input_numbers():

    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    
    try:
     print(f"{a} / {b} is {a/b}")

    except ZeroDivisionError as exp:
     print(exp)
     print("\nCannot divide by zero\n")
     input_numbers()

input_numbers()