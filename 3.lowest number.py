
my_list = []


n = int(input("how many numbers?"))

for i in range(n):
	user = int(input("enter number: "))
	my_list.append(user)

my_list = set(my_list) 

golden_num = 1

while True:

	if golden_num in my_list:
		golden_num += 1
	else:
		print(f"Answer is {golden_num}")
		break
