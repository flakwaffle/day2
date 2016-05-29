import random

results = [
'It is certain',
'It is decidedly so',
'Without a doubt', 
'You may rely on it',
'Most likely',
'Outlook good',
'Reply hazy try again',
'Ask again later',
'Better not tell you now',
'Concentrate and ask again',
'Don\'t count on it',
'My reply is no', 
'My sources say no',
'Outlook not so good',
'Very doubtful'
]

print("You are looking at a Magic 8 Ball.")

def game():
	while True:
		answers = input("Press 'Q' to escape program.\nAsk the ball a question!\n")
		if answers.lower() != 'q':
			print(random.choice(results))
		else:
			break
			
			
game()