import random

count: int = 0
num = int(input("How many iterations do you want\n"))
for _ in range(num):
	x = random.random()
	y = random.random()
	if x ** 2 + y ** 2 <= 1:
		count += 1
print(4*count/num)	
