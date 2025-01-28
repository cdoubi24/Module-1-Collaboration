
# 3.1 Calculate seconds in an hour
seconds_in_hour = 60 * 60
print("Seconds in an hour:", seconds_in_hour)  # Output: 3600

# 3.2 Assign to seconds_per_hour
seconds_per_hour = seconds_in_hour
print("Seconds per hour:", seconds_per_hour)  # Output: 3600

# 3.3 Calculate seconds in a day using seconds_per_hour
seconds_in_day = seconds_per_hour * 24
print("Seconds in a day:", seconds_in_day)  # Output: 86400

# 3.4 Save the result in seconds_per_day
seconds_per_day = seconds_in_day
print("Seconds per day:", seconds_per_day)  # Output: 86400

# 3.5 Floating-point division
floating_point_division = seconds_per_day / seconds_per_hour
print("Floating-point division (seconds_per_day / seconds_per_hour):", floating_point_division)  # Output: 24.0

# 3.6 Integer division
integer_division = seconds_per_day // seconds_per_hour
print("Integer division (seconds_per_day // seconds_per_hour):", integer_division)  # Output: 24

# Confirm agreement between floating-point and integer division results
print("Does the integer division agree with the floating-point value (ignoring .0)?", integer_division == int(floating_point_division))
