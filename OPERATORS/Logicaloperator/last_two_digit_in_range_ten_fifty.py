"""

Check last two digit of number is in range of 10 to 50
"""

number=127
last_two_digit=number%100 # #127%100 =>27
number_in_range=last_two_digit>=10 and last_two_digit<=50 #27>=10 and 27<=50
print(number_in_range) #True