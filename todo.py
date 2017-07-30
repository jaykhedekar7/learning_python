#TODO app using python
#https://etherpad.openstack.or/p/python
import sys
import os

if len(sys.argv)>1:

#Condition to display list
    if sys.argv[1] == "-v":
        file = open("todo.txt","r")
        print(file.read())

#Condition to append the todo item
    elif sys.argv[1] == "-a":
        f = open("todo.txt", "a")
        f.write(sys.argv[2]+"\n")
        f.close()

#if invalid parameter passed
    else:
        print("Invalid Parameter")

#if no parameter passed
    else:
        print("No args specified")

if __name__=="__main__":
    todo_list()




     
