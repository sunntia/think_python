
#If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)?

miles = 10 / 1.61
seconds = 42 + (42 * 60)
mil_per_sec = seconds / miles
mil_per_min = mil_per_sec / 60
mil_per_sec2 = (mil_per_min - 6) * 60
print('Time per mile in seconds', mil_per_sec)
print('Time per mile in minutes', mil_per_min)
print('Time per mile in minutes and seconds:', int(mil_per_min),'minutes', int(mil_per_sec2), 'seconds')


#What is your average speed in miles per hour?

miles = 10 / 1.61
seconds = 42 + (42 * 60)
hours = seconds / 3600
mil_per_hour = miles / hours
print(mil_per_hour)
