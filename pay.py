import os
import datetime

now = datetime.datetime.now()
 
username = ""
password = ""
product = ""


def scan():
    exit = ""
    while exit != "exit":

        file = open ("Payment.txt", "a+")
        file.write(now.strftime("%d-%m-%Y  %H:%M:%S"))
        product = raw_input("Product: ")
        price = int(raw_input("Price: "))
        file.write("       %d" %price + "              " + product + "\n")
        file.write("-----------------------------------------------------------\n")
        exit = raw_input("\n")
        if exit == "exit":
            file.close()
        else:
            pass    

 
#Takes user input and password.
while not username:
    username = raw_input("Username: ")
    password = raw_input("Password: ")
    
    if username == "Pratik" and password == "satara":
        print("Hello ") + username + (". Welcome back!")
        scan()
    elif username == "Jay" and password == "bombay":
        print("Hello ") + username + (". Welcome back!")
        scan()
    elif username == "Ashish" and password == "chandigarh":
        print("Hello ") + username + (". Welcome back!")
        scan()
    else: 
        print("Enter correct Username/Password")


