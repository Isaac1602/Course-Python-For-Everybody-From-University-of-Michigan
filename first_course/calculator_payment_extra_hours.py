# Second code for practicing i python 
def computepay(hrs, payRate):
    try:
        hrs = float(h)
        payRate = float(pR)
    except:
        print('Error, please enter a numeric input')
        quit()

    if hrs <= 40:
        pay =  hrs * payRate
        print (pay)
    else:
        extrahrs = hrs % 40
        # it could also be 
        #pay = (hrs + 0.5 * extrahrs) * payRate
        extrapay = extrahrs * payRate * 1.5
        pay = (hrs - extrahrs) * payRate + extrapay 
    
    return pay


    return 42.37

h = (input('Enter hours: '))
pR = (input('Enter pay rate: '))

p = computepay(h, pR)
print("Pay", p)