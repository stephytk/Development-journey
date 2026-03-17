"""



If password is correct:

Ask for OTP

If OTP is correct → "Login successful"

Else → "Incorrect OTP"


Else → "Incorrect password"
"""


db_paswrd="abcdef"

otp="124"

user_paswrd=input("Enter the password :")

if db_paswrd==user_paswrd:

    user_otp=input("Enter the otp :")

    if otp==user_otp:

        print("Login sucessful")
        
    else:
        print("Incorrct otp")
else:
    print("Incorrect Password")

