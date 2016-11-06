def go(players):
	""" Keeps scores for a game of Sushi Go. Run a game by calling the function
	and passing in the number of players, followed by each of the players'
	names. Type in your scores carefully, as you won't be able to revise them
	afterwards.

	By Tammy Chen and Samantha Wong.
	"""
	scores = {}
	while players > 0:
		name = get_input("Input the player's name")
		scores[name] = 0
		players -= 1
	round = 1
	def play_round():
		nonlocal round
		nonlocal scores
		print("Beginning of round", round)
		for name in scores.keys():
			score = get_input("Give a score for {0}"\
				.format(name), "int")
			scores[name] = scores[name] + int(score)
		print("End of round", str(round))
		round += 1
		if round > 3:
			for name in scores.keys():
				dessert_score = get_input("Input dessert score for {0}"\
					.format(name), "int")
				scores[name] = scores[name] + int(dessert_score)
			highest_score = 0
			winner = ''
			tie = False
			for name in scores.keys():
				if scores[name] > highest_score:
					highest_score = scores[name]
					winner = name
			for name in scores.keys():
				if scores[name] == highest_score and name != winner:
					print("There is a tie score of {0} between {1} and {2}!"\
						.format(highest_score, winner, name))
					tie = True
			if not tie:
				print("The winner is {0} with a score of {1}!"\
					.format(winner, highest_score))
			for name in scores.keys():
				print("{0}:{1}".format(name, scores[name])
			return "Game finished!"
		else:
			return play_round()

	return play_round()

def get_input(prompt, value_type="str"):
	""" Gets input, and ensures it's of type `value_type`.
		Currently only supports str and int

	>>> score = get_input("Give a score", int)
	Give a score: asdf
	Give a score (must be int): 5
	>>> score
	5
	"""
	assert value_type in ["str", "int"], "{} type not supported".format(value_type)
	value = input("{0}: ".format(prompt))
	if value_type == "str":
		return value
	while True:
		try:
			return int(value)
		except:
			value = input("{0} (must be int): ".format(prompt))

# if __name__ == '__main__':

# 	go()