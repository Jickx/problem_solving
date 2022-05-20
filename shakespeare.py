import random, string

def generate(length):
	letters = string.ascii_lowercase + ' '
	return ''.join(random.choice(letters) for i in range(length))

def find_score(phrase, generated_phrase):
	score = 0
	for i in range(len(phrase)):
		if generated_phrase[i] == phrase[i]:
			score += 1
	score_percent = score * 100 / 28
	return score		

def main():
	phrase = "methi"
	best_score = 0
	while True:
		for i in range(1000000):
			generated_phrase = generate(len(phrase))
			score = find_score(phrase, generated_phrase)
			if score == len(phrase):
				print(generated_phrase)
				return "Found!"
			else:
				if best_score < score:
					best_score = score
		print(generated_phrase, best_score)

main()






