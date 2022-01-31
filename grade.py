total=float(input('Enter your total marks out of 500: '))
perc=total/500*100
if perc>=90:
    grade='A'
elif perc>=80:
    grade='B'
elif perc>=70:
    grade='C'
elif perc>=60:
    grade='D'
else :
    grade='E'
print('Percentage=', perc)
print('Grade=', grade)