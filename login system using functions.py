# FUNCTIONS

# write a program to build a login system using functions. The function name should be login and register.
# -It should ask the user to enter the details for registration and out of all the details only username and password should be stored.
# -Now this function should ask the user to enter username and password. If these match with the registered details then login success.
# -Otherwise repeat login process saving invalid credentials.

'''
def loginandreg():
    d={}
    print("Welcome to registration")
    uname=input("Enter name: ")
    upass=input("Enter password: ")
    unum=input("Enter phoneno: ")

    d[uname]=upass
    while True:
        print("Welcome to login")
        
        lname=input("Enter login username: ")
        lpass=input("Enter login user password: ")
        
        #if user exists or not
        
        if lname in d:
            if d[lname] in lpass:
                print("login success")
            else:
                print("Enter valid passcode")
        else:
            print("Invalid user")
            break
loginandreg()

'''