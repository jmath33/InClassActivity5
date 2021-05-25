def leap(in_year):

#in_year = int(input("Please enter a year to check if it is a leap year: ")

	if((in_year % 4) == 0):
		if((in_year % 100) == 0):
			if((in_year % 400) == 0):
				print("%d is a leap year!" %in_year)
				return 0
			else:
				print("%d is not a leap year." %in_year)
				return 1
		else:
			print("%d is a leap year!" %in_year)
			return 0
	else:
		print("%d is not a leap year." %in_year)
		return 1

try: input = raw_input
except NameError: pass
inp = input("Enter a year to check if it is a leap year: ")
inp = int(inp)
leap(inp)
