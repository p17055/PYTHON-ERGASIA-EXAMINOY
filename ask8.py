import random
from random import randint
number1 = [randint(-30, 30) i for i in range (1,10)]
number2 = [randint(-30, 30) i for i in range (1,10)]
number3 = [randint(-30, 30) i for i in range (1,10)]
zeroes = 0
for i in number1 :
	for j in number2 :
		for k in number3 :
			sum = i + j + k
			if sum == 0 :
				zeroes = zeroes + 1
print(zeroes)
