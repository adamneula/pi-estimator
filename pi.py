import random
from tqdm import tqdm

count: int = 0
num = int(input("How many iterations do you want?\n"))

for i in tqdm(range(num), desc="Status: "):
    x = random.random()
    y = random.random()
    if x ** 2 + y ** 2 <= 1:
        count += 1

print(4 * count / num)
