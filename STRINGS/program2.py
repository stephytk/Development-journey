"""
W.a.p to display alphabet_count,digit_count,special character count
"""

word="aman##aplan**panamawith2car1bike"

alphabet_count=0

digit_count=0

special_count=0


for ch in word:

    if ch.isalpha():

        alphabet_count=alphabet_count+1

    elif ch.isdigit():

        digit_count=digit_count+1

    elif not ch.isalnum():

        special_count=special_count+1

        

print(f"alpha count {alphabet_count}")
print(f"digit count {digit_count}")
print(f"special_count{digit_count}")



 

   