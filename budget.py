'''

Program to assist Jayhawks in budgeting their dining dollars.
daysleft defaults to 114, as this is the amount of days in the semester
'''

max = 0
amount = 0

while(True):
	plan = input("Are you using the Crimson or Blue plan?: ")
	if (plan.lower() == "crimson"):
		max = 2170.00
		break
	elif (plan.lower() == "blue"):
		max = 2013.00
		break
	else:
		print('Please enter "Crimson" or "Blue". ')
spent = input("Have you spent any dining dollars yet? (Y/N)").upper
if spent == "Y" or spent == "YES":
	amount = float(input("How many dining dollars do you currently have?"))
else:
	amount = max
def_date()

