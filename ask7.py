from datetime import datetime
now = datetime.now()
today = now.day
samedates = 0
for i in range (1, 10):
		if datetime.today().day + i == today:
				samedates = samedates +1
answer = 'Same dates as today within the next 10 years:'
print(samedates, answer)
		