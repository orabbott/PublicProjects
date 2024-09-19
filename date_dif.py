'''

Program to find how many days are between two dates (inclusive)

'''
def date_dif():
	date1 = str(input("What is the start date? MM/DD/YYYY: "))
	if date1[0] == "0":
		curmon = int(date1[1])
	else:
		curmon = int(date1[0] + date1[1])
	if date1[3] == "0":
		curday = int(date1[4])
	else:
		curday = int(date1[3] + date1[4])
	curyear = int(date1[6] + date1[7] + date1[8] + date1[9])

	date2 = str(input("What is the end date? MM/DD/YYYY: "))
	if date2[0] == "0":
		month2 = int(date2[1])
	else:
		month2 = int(date2[0] + date2[1])
	if date2[3] == "0":
		day2 = int(date2[4])
	else:
		day2 = int(date2[3] + date2[4])
	year2 = int(date2[6] + date2[7] + date2[8] + date2[9])
	total = 0
	def find_days(month, year):
		if month == 4 or month == 6 or month == 9 or month == 11:
			return 30
		elif month == 2 and year % 4 == 0:
			return 29
		elif month == 2:
			return 28
		else:
			return 31

	while curday != day2 or curmon != month2 or curyear != year2:
		while curday < find_days(curmon, curyear):
			curday += 1
			total += 1
			if curday == day2 and curmon == month2 and curyear == year2:
				break
		if curday == day2 and curmon == month2 and curyear == year2:
			total += 1
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
print(date_dif())
