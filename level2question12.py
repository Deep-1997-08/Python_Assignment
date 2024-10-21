def login():
    username=input('Enter the username ')
    password= '1234'
    
    attemps=3
    while attemps>0:
        con_pass=input("Enter your password to login ")
    
        if con_pass==password:
            print("Welcome to the login page ")
            
        else:
            attemps-=1
            print("Wrong Password ")
            
login()