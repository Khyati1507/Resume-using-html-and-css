
# empty checking
def isempty(empty):
    if len(empty)==0:
        return True
    else:
        return False
def push(empty,a):
    
    empty.append(a)
    print()
def pop(empty):
    a=empty.pop()
    print("The deleted element is ",a)
    print()
def top(empty):
    x=len(empty)
    print("the top most element in this list is ",empty[x-1]) 
    print()
def dis(empty):
    x=len(empty)
    print("current elements in the list are-")
    for i in range(x-1,-1,-1):
        print(empty[i],end=' ')
    print()
# main coding
empty=[]
while True:
    print("Hello there!")
    print('Insert-1\nDelete-2\ndisplay-3\ntopmost-4\nexit-5')
    a=int(input('What you want to do-'))
    if a==2:
        if isempty(empty):
            print('The list is empty(Underflow)')
            
        else:
            pop(empty)
    elif a==1:
        e=input('Enter the element')
        push(empty,e)

    elif a==3:
        if isempty(empty):
            print('The list is empty(Underflow)')
            
        else:
            dis(empty)
    elif a==4:
        if isempty(empty):
            print('The list is empty(Underflow)')
            
        else:
            top(empty)
    elif a==5:
        break
    else:
        print('enter correct data')
        break