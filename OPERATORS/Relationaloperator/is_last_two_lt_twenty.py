"""
Check last two digit less than twenty
"""

number=123
last_two_digit=number%100 # 123%100 =>23
is_last_two_gt_lt_twenty=last_two_digit<20 #23<20 false
print(is_last_two_gt_lt_twenty) #false