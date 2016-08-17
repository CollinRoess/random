#!/usr/bin/env

print "Welcome to the Brainf*ck Interpreter 1.0!"
filename=raw_input("Please enter a filename.txt that you want to execute: ")
file = open(filename, 'r')
contents=file.read()

pointer=[0]*30000
index=0
for char in contents:
	if char == "+":
		pionter[index]+=1
	elif char == "-"
		pointer[index]-+1