def count(ec):
    global e,c
    e,c=0,0
    for i in ec:
        if i=="e":
            e+=1
        elif i=="c":
            c+=1
        
    return e,c
#main
a=input('enter any string:-')
count(a)
print("Total no. of e and c in the string is",e,"and",c )