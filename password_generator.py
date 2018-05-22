import os
import random
import string

def pass_diff():
	print("How strong of a password do you want? 'weak', 'medium', or 'strong'?")
	return input("--> ").lower()


def generator(pass_diff):
	
	list_pass = []

	if pass_diff == "weak":
		for i in range(1,2):
			list_pass.append(random.choice(string.punctuation))
		for i in range(1,4):
			list_pass.append(random.choice(string.digits))
		for i in range(1,5):	
			list_pass.append(random.choice(string.ascii_letters))
		password = "".join(list_pass)
		print(password)

	if pass_diff == "medium":
		for i in range(1,4):
			list_pass.append(random.choice(string.punctuation))
		for i in range(1,5):
			list_pass.append(random.choice(string.digits))
		for i in range(1,6):	
			list_pass.append(random.choice(string.ascii_letters))
		password = "".join(list_pass)
		print(password)

	if pass_diff == "strong":
		for i in range(1,6):
			list_pass.append(random.choice(string.punctuation))
		for i in range(1,8):
			list_pass.append(random.choice(string.digits))
		for i in range(1,9):	
			list_pass.append(random.choice(string.ascii_letters))
		password = "".join(list_pass)

		print(password)

def main():
	play = True

	while play == True:
		strn = pass_diff()
		generator(strn)

		play_again = input('Do you want another password? "Yes" or "No": ')

		if play_again == "yes":
			play = True
			os.system('clear')
		else:

			play = False






if __name__ == "__main__":
	main()

