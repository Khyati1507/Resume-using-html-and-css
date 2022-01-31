def countv_c(word):
    global v
    v=0
    global c
    c=0
    global s
    s=0
    for i in word:
        if i in vowel:
            v+=1
        elif i==" ":
            s+=1
        else:
            c+=1
    return v,c
#main
vowel=['a','e','i','o','u']
a=input("Enter any word:-")
countv_c(a)
print("total no of vowels=",v)
print("total no of consotants=",c)