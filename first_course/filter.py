clause = True
max = None 
min = None

while clause == True:
    num = input ("Enter your value")
    if num == 'done':
        clause = False
        break
    try:
        number = float(num)
    except:
        print("Invalid input")
        continue

    if max == None and min == None:
        max = number 
        min = number
    
    if max < number:
        max = number 
    
    if min > number:
        min = number 

print("Maximum is", max)
print("Minimun is", min) 