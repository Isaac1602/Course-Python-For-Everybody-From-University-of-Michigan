# This code is going to retrieve grades according to a list of values 

grade = input('Enter your grade ')

try:
    gradeNum = float(grade)
except:
    print('Error, use the a numeric value')
    quit()


if gradeNum > 0.0 and gradeNum <=1.0 == True:
    pass
else:
    print('You are out of range')
    quit()

if gradeNum >= 0.9:
    print('A')
elif gradeNum >= 0.8:
    print('B')
elif gradeNum >= 0.7:
    print('C')
elif gradeNum >= 0.6:
    print('D')
elif gradeNum < 0.6:
    print('F')
