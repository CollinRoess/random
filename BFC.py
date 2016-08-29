#!/usr/bin/python3

print ("Welcome to the Brainf*ck Interpreter 1.0!")
filename=input("Please enter a filename.txt that you want to execute: ")



file = open(filename, 'r')
contents=file.read()
content_list=list(contents)
print (content_list)

pointer=[0]*30000
index=0

for char in content_list:
	if char == "+":
		pointer[index]+=1
	elif char == "-":
		pointer[index]-+1
	elif char == ".":
		#print (chr(int(char))) syntax error here. Fix later
	elif char == ",":
		pointer[index]=ord(char)
		
		
		

print( "done")
