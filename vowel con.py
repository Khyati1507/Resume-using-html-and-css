def countv_c(word):
    global v,c,s
    v,c,s=0,0,0
    for i in word:
        if i in vowel:
            v+=1
        elif i==" ":
            s+=1
        else:
            c+=1

#main
vowel=['a','e','i','o','u']
a=input("Enter any word:-")
countv_c(a)
print("total no of vowels=",v)
print("total no of consotants=",c)
