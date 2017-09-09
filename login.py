import os
import datetime

now = datetime.datetime.now()
username = ""
password = ""

#Logs it in the text file with date and time.
def log(payment):					
	file = open("log.txt", "a+")
	file.write("\n" + username + " paid Rs.%d" %payment + "\n")
	file.write("Time of payment: ")
	file.write(now.strftime("%d-%m-%Y  %H:%M:%S"))
	file.write("\n-----------------------------------------------------------")
	file.close() 

#Validates user with one more password and sends to log function.
def validate():
	print("Enter your membership code")
    	code = raw_input("Membership code: ")
	if code == "helloworld1234":
		print( username + " access granted. Enter your payment.\n")
		payment = int(raw_input("Payment: "))
		log(payment)
	elif code == "guest":
		print( "Guest "+ username + ". Enter your payment.\n")
		payment = int(raw_input("Payment: "))
		log(payment)
	else:
		print("Oops! Failed to validate.")	
 
#Takes user input and password.
while not username:
    username = raw_input("Username: ")
    password = raw_input("Password: ")
    
    if username == "Pratik" and password == "satara":
        print("Hello ") + username + (". Welcome back!")
        validate()
    elif username == "Jay" and password == "bombay":
        print("Hello ") + username + (". Welcome back!")
        validate()
    elif username == "Ashish" and password == "chandigarh":
        print("Hello ") + username + (". Welcome back!")
        validate()
    elif username == "guest" or password == "guest":
    	print("hello") + username + (". Welcome to 103!")
    	log(username)
    else: 
    	print("Enter correct Username/Password")


