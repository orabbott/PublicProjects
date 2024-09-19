'''

Program to find how many days are between two dates (inclusive)

'''
def date_dif(month1, day1, year1, month2, day2, year2):
	total = 0
	curday = day1
	curmon = month1
	curyear = year1
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
date1 = str(input("What is the start date? MM/DD/YYYY: "))
if date1[0] == "0":
	mon1 = date1[1]
else:
	mon1 = date1[0] + date1[1]
if date1[3] == "0":
	day1 = date1[4]
else:
	day1 = date1[3] + date1[4]
year1 = date1[6] + date1[7] + date1[8] + date1[9]

date2 = str(input("What is the end date? MM/DD/YYYY: "))
if date2[0] == "0":
	mon2 = date2[1]
else:
	mon2 = date2[0] + date2[1]
if date2[3] == "0":
	day2 = date2[4]
else:
	day2 = date2[3] + date2[4]
year2 = date2[6] + date2[7] + date2[8] + date2[9]

print("The difference between the two dates is " + str(date_dif(int(mon1), int(day1), int(year1), int(mon2), int(day2), int(year2))) + " days.")
