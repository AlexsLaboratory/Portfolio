import time, datetime, sys
from subprocess import call

"""
Specify the date that you want to countdown to
"""
Year = 2018
Month = 9
Day = 30
Hour = 23
Minute = 0
Second = 0

target_date = datetime.datetime(Year, Month, Day, Hour, Minute, Second) # Formats the date entered
timedelta_zero = datetime.timedelta(0) # Sets time delta to 0:00:00
while True: # Runs the code with in the while statement infinitely until broken out of
  time.sleep(1) # Loops every second
  if sys.platform.startswith('linux') or sys.platform.startswith('darwin'): # Runs code below only if this script is running on Linux or Darwin
    call('clear', shell=True) # Clears terminal
  elif sys.platform.startswith('win32') or sys.platform.startswith('cygwin'): # Runs code below only if this script is running on Win32 or Cygwin
    call('cls', shell=True) # Clears terminal
  diff = target_date - datetime.datetime.now() # Displays the difference between the target date and the current date
  if (diff <= timedelta_zero): # Breaks out of the while loop if time delta is less than or equal to 0:00:00
    break
  if (len(str(diff)) >= int(21)): # Checks if there are still days left
    identification = int(1) # This is set to detect if there are still days left
    day, _, time_dec = str(diff).split() # Splits diff into days and time_dec
    hour_final, minute_final, second = time_dec.split(":") # Splits the time_dec into hours, minutes, and seconds
    second_final, _ = second.split(".") # Removes microseconds from the second string
  else:
    identification = int(2) # This is set to detect if there are only time left
    hour_final, minute_final, second = str(diff).split(":") # Splits the time_dec into hours, minutes, and seconds
    second_final, _ = second.split(".") # Removes microseconds from the second string

  if identification == int(1): # If there are days
    get_year = int(day) / float(365) # This is used to get the year in a decimal format
    year_final, year_fraction = divmod(get_year, 1) # Does floor division and the modulus operator and crates a tuple
    day_final = round(year_fraction * 365.25) # Gets the rounded days

    if int(year_final) != int(0): # Checks to make sure that year_final is not equal to 0 before it runs
      if int(year_final) == int(1): # The code in this if statement will only run if the year_final is equal to 1
        outline = "-" * 10 # This is for the box around the year
        years = "| {x} Year |".format(x = int(year_final)) # Stores the data for years
        print(outline) # Prints the outline
        print(years) # Prints the years
        print(outline) # Prints the outline
      else:
        years = "| {x} Years |".format(x = int(year_final)) # Stores the data for years
        outline = "-" * len(years) # Creates the outline dynamically with the number of characters
        print(outline) # Prints the outline
        print(years) # Prints the years
        print(outline) # Prints the outline

    if int(day_final) != int(0): # Checks to make sure that day_final is not equal to 0 before it runs
      if int(day_final) == int(1): # The code in this if statement will only run if the day_final is equal to 1
        outline = "-" * 9 # This is for the box around the day
        days = "| {x} Day |".format(x = int(day_final)) # Stores data for days
        print(outline) # Prints the outline
        print(days) # Prints the days
        print(outline) # Prints the outline
      else:
        days = "| {x} Days |".format(x = int(day_final)) # Stores data for days
        outline = "-" * len(days) # Creates the outline dynamically with the number of characters
        print(outline) # Prints the outline
        print(days) # Prints the days
        print(outline) # Prints the outline

    if int(hour_final) != int(0): # Checks to make sure that hour_final is not equal to 0 before it runs
      if int(hour_final) == int(1): # The code in this if statement will only run if the hour_final is equal to 1
        outline = "-" * 10 # This is for the box around the hour
        hours = "| {x} Hour |".format(x = int(hour_final)) # Stores data for hours
        print(outline) # Prints the outline
        print(hours) # Prints the hours
        print(outline) # Prints the outline
      else:
        hours = "| {x} Hours |".format(x = int(hour_final)) # Stores data for hours
        outline = "-" * len(hours) # Creates the outline dynamically with the number of characters
        print(outline) # Prints the outline
        print(hours) # Prints the hours
        print(outline) # Prints the outline

    if int(minute_final) != int(0): # Checks to make sure that minute_final is not equal to 0 before it runs
      if int(minute_final) == int(1): # The code in this if statement will only run if the minute_final is equal to 1
        outline = "-" * 12 # This is for the box around the minute
        minutes = "| {x} Minute |".format(x = int(minute_final)) # Stores data for minutes
        print(outline) # Prints the outline
        print(minutes) # Prints the minutes
        print(outline) # Prints the outline
      else:
        minutes = "| {x} Minutes |".format(x = int(minute_final)) # Stores data for minutes
        outline = "-" * len(minutes) # Creates the outline dynamically with the number of characters
        print(outline) # Prints the outline
        print(minutes) # Prints the minutes
        print(outline) # Prints the outline

    if int(second_final) == int(1): # Checks to make sure that second_final is not equal to 0 before it runs
      outline = "-" * 12 # This is for the box around the second
      seconds = "| {x} Second |".format(x = int(second_final)) # Stores data for seconds
      print(outline) # Prints the outline
      print(seconds) # Prints the seconds
      print(outline) # Prints the outline
    else:
      seconds = "| {x} Seconds |".format(x = int(second_final)) # Stores data for seconds
      outline = "-" * len(seconds) # Creates the outline dynamically with the number of characters
      print(outline) # Prints the outline
      print(seconds) # Prints the seconds
      print(outline) # Prints the outline

  elif identification == int(2): # Sets the identification
    if int(hour_final) != int(0): # Checks to make sure that hour_final is not equal to 0 before it runs
      if int(hour_final) == int(1): # The code in this if statement will only run if the hour_final is equal to 1
        outline = "-" * 10 # This is for the box around the hour
        hours = "| {x} Hour |".format(x = int(hour_final)) # Stores data for hours
        print(outline) # Prints the outline
        print(hours) # Prints the hours
        print(outline) # Prints the outline
      else:
        hours = "| {x} Hours |".format(x = int(hour_final)) # Stores data for hours
        outline = "-" * len(hours) # Creates the outline dynamically with the number of characters
        print(outline) # Prints the outline
        print(hours) # Prints the hours
        print(outline) # Prints the outline

    if int(minute_final) != int(0): # Checks to make sure that minute_final is not equal to 0 before it runs
      if int(minute_final) == int(1): # The code in this if statement will only run if the minute_final is equal to 1
        outline = "-" * 12 # This is for the box around the minute
        minutes = "| {x} Minute |".format(x = int(minute_final)) # Stores data for minutes
        print(outline) # Prints the outline
        print(minutes) # Prints the minute
        print(outline) # Prints the outline
      else:
        minutes = "| {x} Minutes |".format(x = int(minute_final)) # Stores data for minutes
        outline = "-" * len(minutes) # Creates the outline dynamically with the number of characters
        print(outline) # Prints the outline
        print(minutes) # Prints the minutes
        print(outline) # Prints the outline

    if int(second_final) == int(1): # The code in this if statement will only run if the second_final is equal to 1
      outline = "-" * 12 # This is for the box around the second
      seconds = "| {x} Second |".format(x = int(second_final)) # Stores data for seconds
      print(outline) # Prints the outline
      print(seconds) # Prints the seconds
      print(outline) # Prints the outline
    else:
      seconds = "| {x} Seconds |".format(x = int(second_final)) # Stores data for seconds
      outline = "-" * len(seconds) # Creates the outline dynamically with the number of characters
      print(outline) # Prints the outline
      print(seconds) # Prints the seconds
      print(outline) # Prints the outline
print("Time is up") # Prints when broken out of loop
