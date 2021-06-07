#Death Clock Calc
def main():
		
	age = float(input('Enter your current age:\n'))
	finalAge = float(input('Enter your expected final age:\n'))
	
	lifeLeft = finalAge - age
	years = lifeLeft
	months = lifeLeft * 12
	weeks = lifeLeft * 52.134
	days = lifeLeft * 365
	
	print(f'''
	
You have:
		{round(years)} years left
		{round(months)} months left to live
		{round(weeks)} weeks left to live
		{round(days)} days left to live
	
	'''
	)
	
	x = input('Try again? Type Yes or No:\n\n').lower()
	if x == 'yes':
		main()
	else:
		print('Error')


main()
