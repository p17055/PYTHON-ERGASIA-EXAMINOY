for i in range (1, 30000):
	symbol = input('Enter a symbol')
	while (symbol!='+' &  symbol!='-' & symbol!='.' & symbol!=',' & symbol!='[' & symbol!=']' & symbol!='<' & symbol!='>'):
		print('Not valid input')
		symbol = input('Enter abother symbol')
	bf[i] = symbol
for i in range (1, 30000):
	c[i] = 0
for i in range (1,30000):
	if  bf[i] == '<':
		i = i + 1
	elif bf[i] == '<':
		i = i -1 
	elif bf[i] == '+':
		c[i] = c[i] + 1
	elif bf[i] == '-':
		c[i] = c[i] - 1
	elif bf[i] == '.':
		print(c[i])
	elif bf[i] == ',':
		bf[i] = bf[i+1]
	elif bf[i] == '[':
		if c[i] == 0:
			x = 0 
			while (i <= 30000):
				i = i + 1 
				if bf[i-1] == ']':
					x = i
					break
			c[i] = x 
	else:
		x = 0 
		while (i <= 30000):
			i = i - 1
			if bf[i] == '[':
				x = i-1
				break
			c[i] = x

			