def countuandl(b):
    global u,l
    u,l=0,0
    for i in b:
        c=ord(i)
        if c >=65 and c<=90:
            u+=1
        elif c>=97 and c<=122:
            l+=1
    return u,l
#main
a=input("enter any string ")
countuandl(a)
print("Total no of upper case letter are",u)
print("Total no of lower case letter are",l)


