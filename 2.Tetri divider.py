
class Divider:

	def __init__(self,amount):
		self.amount = amount


	def calculate(self,amount):
		step = 0
		
		while True:
			if amount >= 50:
				amount -= 50
				step += 1
			elif amount >= 20:
				amount -= 20
				step += 1
			elif amount >= 10:
				amount -= 10
				step += 1
			elif amount >= 5:
				amount -= 5
				step += 1
			elif amount >= 2:
				amount -= 2
				step += 1
			elif amount >= 1:
				amount -= 1
				step += 1

			if amount == 0:
				return step





def menu():
	
	user = Divider(int(input("Enter amount of Tetri: ")))
	answer = user.calculate(user.amount)
	print(f"For {user.amount} tetri you will get {answer} coins")





menu()



