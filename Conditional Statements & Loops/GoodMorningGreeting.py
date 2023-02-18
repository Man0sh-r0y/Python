'''Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening.
Your program should use time module to get the current hour.'''

import time

currentHour = int(time.strftime("%H"))  # Hour
currentMinitue = int(time.strftime("%M"))  # Minitue
currentSecond = int(time.strftime("%S"))  # Second
# we typcasted the to int as time.strftime() gives ans as string


if(currentHour >= 6 and currentHour < 11):
    print("Current time is ", time.strftime("%H:%M:%S"))
    print("Good Morning Manash")
elif(currentHour >= 13 and currentHour <= 16):
    print("Current time is ", time.strftime("%H:%M:%S"))
    print("Good Afternoon Manash")
elif(currentHour >= 18 and currentHour <= 21):
    print("Current time is ", time.strftime("%H:%M:%S"))
    print("Good Evening Manash")
