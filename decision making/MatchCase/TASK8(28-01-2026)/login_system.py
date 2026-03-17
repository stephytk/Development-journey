"""

Task:
- Ask for username
- Ask for password

If username and password are correct:
    "Login successful"
Else:
    "Invalid credentials"
"""


db_name="abcd"

db_paswrd="1234#"

user_name=input("Enter the username :")

user_password=input("Enter the password :")

if db_name==user_name and db_paswrd==user_password:
    print("Login successful")

else:
    print("invalid Credentials")