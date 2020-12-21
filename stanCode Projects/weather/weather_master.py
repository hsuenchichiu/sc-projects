"""
File: weather_master.py
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT=-100

def main():
	"""
	This program demonstrates the highest, the lowest and the mean of the temperatures based on the
	numbers the user entered.
	The program also indicates the number of cold days with the cold-day standard at 16.
	"""
	print('stanCode "Weather Master 4.0"!')
	new_temp = int(input('Next Temperature:(or -100 to quit)? '))
	cold_days = 0


	if new_temp == EXIT:
		print('No temperatures are entered')

	else:
		max_temp = new_temp
		min_temp = new_temp
		sum_temp = new_temp
		days = 1
		#count the days to calculate the average.

		if new_temp < 16:
			cold_days = cold_days + 1
			#count the cold days.
		while True:
			new_temp = int(input('Next Temperature:(or -100 to quit)? '))
			if new_temp == EXIT:
				break

			else:
				sum_temp = sum_temp + new_temp
				days = days + 1
				#count the days for calculate the average

				if new_temp < 16:
					cold_days = cold_days+1
					#count the cold days

				if new_temp > max_temp:
					max_temp = new_temp
				if new_temp < min_temp:
					min_temp = new_temp
				# compared the temperature

		mean_temp = sum_temp / days
		#calculate the average temperature.

		print('Highest Temperature = '+ str(max_temp))
		print('Lowest Temperature = '+ str(min_temp))
		print('Average = ' + str(mean_temp))
		print(str(cold_days) + ' cold day(s)')










###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
