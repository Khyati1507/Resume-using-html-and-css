c = 0
User_ID = "swapnil"
Passcode = "swap"
def login():
    Username = input("Enter your username: ")
    Password = input("Enter your password: ")
    if (Username == User_ID and Password == Passcode):
        print("Login Successful")
        b=input("press SPACE and hit Enter")
        if ord(b)==32:
            print("Now you got access to the SWISS Bank account.")
        return
    else:
        global c
        c=c+1
        if(c<=2):
            print("Try Again")
    if(c<=2):
        login()
        return
    if(c>2):
        print("Account Blocked")

login()
    