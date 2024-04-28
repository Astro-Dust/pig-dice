from random import randint

player_dice = randint(1, 7)
player_score = 0

pig_dice = randint(1, 7)
pig_score = 0


player_name = input('What is your name? -> ').strip().upper()

while True:

	if player_dice == 1:
		player_score = 0
	elif pig_dice == 1:
		pig_score = 0
	else:
		player_score += player_dice
		pig_score += pig_dice

		print('==========================')
		print(f'{player_name}: {player_score}')
		print(f'PIG: {pig_score}')

		if player_score >= 30:
			print(f'{player_name} WINS')
			break
		elif pig_score >= 30:
			print('PIG WINS')
			break
		elif player_score == pig_score:
			player_score = 0
			pig_score = 0
			continue

