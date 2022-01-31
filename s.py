
n=int(input('enter the first number of range number'))
y=int(input('enter the second number of range number'))
print('Number\tsquare\tcube')
for i in range(n,(y+1)):
    square=i**2
    cube=i**3
    print(' ',i,'\t', square,'\t', cube)