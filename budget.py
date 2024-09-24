'''

Program to assist Jayhawks in budgeting their dining dollars.

'''

amount = 0

while(True):
	plan = input("Are you using the Crimson or Blue plan?: ")
	if (plan.lower() == "crimson"):
		amount = 2170.00
		break
	elif (plan.lower() == "blue"):
		amount = 2013.00
		break
	else:
		print('Please enter "Crimson" or "Blue". ')
spent = input("Have you spent any dining dollars yet? (Y/N): ").upper()
if spent == "Y" or spent == "YES":
	amount = float(input("How many dining dollars do you currently have?: "))

def date_differ(month1, day1, year1, month2, day2, year2):
	total = 0
	curday = day1
	curmon = month1
	curyear = year1
	def find_day(month, year):
		if month == 4 or month == 6 or month == 9 or month == 11:
			return 30
		elif month == 2 and year % 4 == 0:
			return 29
		elif month == 2:
			return 28
		else:
			return 31

	while curday != day2 or curmon != month2 or curyear != year2:
		while curday < find_day(curmon, curyear):
			curday += 1
			total += 1
			if curday == day2 and curmon == month2 and curyear == year2:
				break
		if curday == day2 and curmon == month2 and curyear == year2:
			break
		if curmon != month2 or curyear != year2:
			curday = 1
		if curmon == 12:
			curmon = 1
			curyear += 1
			total += 1
		else:
			curmon += 1
			total += 1
	return total
date = str(input("What is the current date? MM/DD/YYYY: "))
if date[0] == "0":
	mon = date[1]
else:
	mon = date[0] + date[1]
if date[3] == "0":
	day = date[4]
else:
	day = date[3] + date[4]

days = date_differ(int(mon), int(day), int(date[6] + date[7] + date[8] + date[9]), 12, 20, 2024)

print("You should be spending about $" + str(round(amount / days, 2)) + " per day.")
