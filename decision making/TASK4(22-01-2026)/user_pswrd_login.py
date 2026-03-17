"""
Write a Python program to check username and password and display login success or failure.
"""
username=input("Enter the username :")
password=int(input("Enter the password:"))
if (username=="admin") and (password==1234):
    print("Login success")
else:
    print("Login Failed")