in_year = int(input("Please enter a year to check if it is a leap year: ")

if((in_year % 4) == 0):
	if((in_year % 100) == 0):
		if((in_year % 400) == 0):
			print("%d is a leap year!" %in_year)
		else:
			print("%d is not a leap year." %in_year)
	else:
		print("%d is a leap year!" %in_year)
else:
	print("%d is not a leap year." %in_year)
