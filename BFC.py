#!/usr/bin/env

"""The following is commented out simply because
I'm not sure I want to keep it yet"""

'''print "Welcome to the Brainf*ck Interpreter 1.0!"
filename=raw_input("Please enter a filename.txt that you want to execute: ")
file = open(filename, 'r')
contents=file.read()

pointer=[0]*30000
index=0
for char in contents:
	if char == "+":
		pointer[index]+=1
	elif char == "-":
		pointer[index]-+1'''
		
		
class Pointer:
	def __init__(self, index, value):
		self.index=index
		self.value=value

	def add(self):
		self.value +=1
	
	def sub(self):
		self.value -=1
		
	def inc(self):
		self.index +=1
	
	def dec(self):
		self.index -=1
	
	def out(self):
		print(self.value)
		
	def inp(self):
		self.value=value
		
		
"""Test of Pointer class methods
head=Pointer(0,0)
head.add()
print head.value
head.sub()
print head.value
head.inc()
print head.index
head.dec()
print head.index
head.out()
"""
