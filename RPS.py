#!usr/bin/env python

import time, random

print("Rock, Paper, Scissors, Shoot!")

def evaluate(user_choice, computer_choice):
	possible_choices=("rock", "paper", "scissors")
	usr_choice_index=possible_choices.index(user_choice)
	cpu_choice_index=possible_choices.index(computer_choice)
	
	time.sleep(.3)
	if usr_choice_index==0:
		if cpu_choice_index==0:
			print("It's a draw!")
		if cpu_choice_index==1:
			print("You lose!")
		if cpu_choice_index==2:
			print("You win!")
		
	if usr_choice_index==1:
		if cpu_choice_index==0:
			print("You win!")
		if cpu_choice_index==1:
			print("It's a draw!")
		if cpu_choice_index==2:
			print("You lose!")
		
	if usr_choice_index==2:
		if cpu_choice_index==0:
			print("You lose!")
		if cpu_choice_index==1:
			print("You win!")
		if cpu_choice_index==2:
			print("It's a draw!")
	

exit_cond= False
while exit_cond==False:
	time.sleep(.3)
	user_choice=input("Enter rock, paper, or scissors: ")
	time.sleep(.3)
	print("You chose "+ user_choice)
	choices=("rock", "paper", "scissors")
	computer_choice=random.choice(choices)
	time.sleep(.3)
	print("Computer chose "+ computer_choice)
	
	evaluate(user_choice, computer_choice)
	time.sleep(.3)
	replay=input("Play again? y/n: ")
	if replay=="N" or replay=="n":
		exit_cond= True
	elif replay=="Y" or replay=="y":
		exit_cond= False
	
