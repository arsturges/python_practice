'''
Exercise for the Breakout
Write a program which allows the user to build up a
sentence one word at a time, stopping when they enter
a period (.), exclamation (!), or question mark (?)
example interaction:
Please enter a word in the sentence
...currently: My
Please enter a word in the sentence
...currently: My name
Please enter a word in the sentence
...currently: My name is
Please enter a word in the sentence
...currently: My name is Slim
Please enter a word in the sentence
...currently: My name is Slim Shady
Please enter a word in the sentence
--->My name is Slim Shady!
(enter . ! or ? to end.): My
(enter . ! or ? to end.): name
(enter . ! or ? to end.): is
(enter . ! or ? to end.): Slim
(enter . ! or ? to end.): Shady
(enter . ! or ? to end.): !
'''

sentence = []
def get_new_word():
	word = raw_input("Enter a word (end with ?, !, or .): ")

def is_ending(word):
	if word == ".":
		True
	elif word == "?":
		True
	elif word == "!":
		True
	else:
		False

while True:
	get_new_word()
	sentence.append(word)
	sentence.append(" ")
	if is_ending(word):
		break

for element in sentence:
	print element
