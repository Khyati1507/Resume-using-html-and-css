age=int(input('enetr your age:'))
if age>=110:
    print ('enter correct age')
elif age>=18:
    print('you are eligible for vote')
else:
    print ('You are not eligible to vote')
    if age<0:
        print('enter correct age')