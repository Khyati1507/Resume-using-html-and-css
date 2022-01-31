name=[]
marks=[]
def entry():
    
    for c in range(0,2):
        a=input("enter your name:")
        name.append(a)
        mak=[]
        
        for i in range(0,5):
            b=int(input("enter the marks of subject:"))
            mak.append(b)       
        marks.append(mak)
    

def display():
    a=0
    while a<len(name):
        print(name[a])
        print("your marks in all the subjects are:",marks[a])
        a+=1    
#main
entry()
display()
