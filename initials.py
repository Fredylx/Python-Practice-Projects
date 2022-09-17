# Project made in IOT class
# Spring 2020
'''
Author:         Fredy Lopez
Type:           Python


---------------------------------------------- Purpose --------------------------------------------------
this script opens a window that has a turtle run in the shape of my initials and read the temperature of a simulated thermomitor
this is also protected with a password, missing is the encryption needed for a truly secure process & the password is visable in the code.

used as one example of my coding skills

'''
import turtle
import sys


#for i>3:


PASS_CODE=qwerty404
incorrectPassword= True
while incorrectPassword:
    password = input("type in your password")
    if len(password < 8):
        print("your password must be 8 characters long")
    elif noNum(password == False):
        print("you need a number in your password")
    elif noCap(password == False):
        print("you need a capital letter in your password")
    #elif NoLow(password == False
temp=int(input("Enter temperature:"))

FL= turtle.Pen()
FL.speed(3)
FL.shape("arrow")


if temp < 25:
    FL.color("black", "#00ff00") #Green fill
elif temp >=25 and temp <= 30:
    FL.color("black", "#8B008B") #Purple fill  
else:
    FL.color("black", "#ff0000") #Red fill
    
FL.begin_fill()
FL.forward(50)
FL.left(90)
FL.forward(150)
FL.right(90)
FL.forward(100)
FL.left(90)
FL.forward(50)
FL.left(90)
FL.forward(100)
FL.right(90)
FL.forward(50)
FL.right(90)
FL.forward(150)
FL.left(90)
FL.forward(50)
FL.left(90)
FL.forward(200)
FL.left(90)
FL.forward(300)
FL.end_fill()
FL.penup()
FL.left(90)
FL.forward(230)
FL.pendown()
FL.begin_fill()
FL.forward(200)
FL.left(90)
FL.forward(50)
FL.left(90)
FL.forward(150)
FL.right(90)
FL.forward(250)
FL.left(90)
FL.forward(50)
FL.left(90)
FL.forward(300)
FL.penup()
FL.end_fill()
FL.forward(100)
sys.exit()
