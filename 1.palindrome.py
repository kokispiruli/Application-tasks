

class Words:

	def __init__(self,word):
		self.word = word

	def check(self,word):
		if word == word[::-1]:
			print(f"\n{word} is a palindrome\n")
		else:
			print(f"\n{word} is not a palindrome\n")


def menu():
	while True:
		
		n = input("How many strings would you like to check? ")
		if not n.isdigit():
			print("Enter Number!")
			continue
		else:
			n = int(n)
			for i in range(n):
				user = Words(input("Enter string: "))
				user.check(user.word)
		break

menu()