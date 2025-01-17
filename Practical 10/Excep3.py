try:  
    a = ['a', 'b', 'c']  
    print (a[2])  
except LookupError:  
    print ("Index Error Exception: list index out of range")
else:  
    print ("No error!")