from random import randint
import os
from time import sleep

player_score = 0
pig_score = 0

player_name = input('What is your name? -> ').strip().capitalize()
os.system('cls || clear')

while True:

	player_dice = randint(1, 7)
	pig_dice = randint(1, 7)

	print('-----------------------')
	print(f'{player_name} rolls a {player_dice}')
	if player_dice == 1:
		print(f"{player_name} rolled a 1. Score reset to 0")
		player_score = 0
	else:
		player_score += player_dice

	print(f'Pig rolls a {pig_dice}')
	if pig_dice == 1:
		print(f"Pig rolled a 1. Score reset to 0")
		pig_score = 0
	else:
		pig_score += pig_dice

	print('-----------------------')
	print(f"{player_name}'s Score: {player_score}")
	print(f"Pig's Score: {pig_score}")

	sleep(2)

	if player_score >= 30:
		print()
		print(f'{player_name.upper()} WINS'
			   f'\nScore: {player_score}')
		break
	elif pig_score >= 30:
		print()
		print(f'PIG WINS!'
			f'\nScore: {pig_score}')
		break
	elif player_score == pig_score:
		player_score = 0
		pig_score = 0
		continue

