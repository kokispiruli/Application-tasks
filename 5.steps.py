steps = int(input("How many steps? "))


n1, n2 = 0, 1
count = 0

if steps <= 0:
	print("Please enter a positive number")
elif steps == 1:
	print(f"There is {n2} way to climb {steps} steps")
else:
	while count < steps:
		nth = n1 + n2
		n1 = n2
		n2 = nth
		count += 1
	print(f"There are {nth} ways to climb {steps} steps")

	   