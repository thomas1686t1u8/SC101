"""
File: weather_master.py
Name: Thomas
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


EXIT = -100  # Exit number, to end the program.


def main():
	"""
	This program calculate the
	1. Highest temperature.
	2. Lowest temperature.
	3. Average temperature.
	4. Days that temperature is lower than 16.
	within a given set of temperature data.
	"""
	print("stanCode \"Weather Master 4.0\"")
	maximum = 0  # Store the max Temp.
	minimum = 0  # Store the min Temp.
	total = 0  # Calculate the total Temp.
	count = 0  # Calculate the total days.
	cold_count = 0  # Calculate the total cold days.
	while True:
		temp = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
		if temp == EXIT:  # If Temp = exit, end the program.
			break
		if count == 0:  # Assign data to max Temp and min Temp after entering the first data.
			maximum = temp
			minimum = temp
		if temp > maximum:  # If the new entered data > max, assign to max Temp.
			maximum = temp
		if temp < minimum:  # If the new entered data < min, assign to min Temp.
			minimum = temp
		if temp < 16:  # If Temp < 16, indicates cold day.
			cold_count += 1
		total = total + temp  # The sum of all data.
		count += 1  # How many days were given.
	if count == 0:
		print('No temperatures were entered.')
	else:
		avg = total / count  # Calculate the average Temp.
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(avg))
		print(str(cold_count) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
