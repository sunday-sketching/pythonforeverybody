largest = None
smallest = None 
while True:
    num = input("Enter a number: ")
    if num == "done": 
        break
    try:
       fnum = float(num)     
    except ValueError: 
        print("Invalid input")
        continue 
    else:
        if smallest is None: 
            largest = num
            smallest = num
        elif num > smallest:
            smallest = num
        elif num < smallest:
            largest = num  

print("Maximum is", largest)
print("Minimum is", smallest)
