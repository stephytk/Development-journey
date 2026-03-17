"""
Mobile Unlock System
------------------------------------
Task:
- Ask for unlock pattern

If pattern is correct:
    - Ask for fingerprint
    - If fingerprint matches:
        "Phone unlocked"
    - Else:
        "Fingerprint mismatch"
Else:
    "Wrong pattern"

"""
db_pattern=1222
fin_print=12345
unlock_pattern=int(input("Enter the pattern :"))
if db_pattern==unlock_pattern:
    fingerprint=int(input("Enter the fingerprint :"))
    if fingerprint==fin_print:
        print("Phone unlocked")
    else:
        print("fingerprint is missing")
else:
    print("Wrong pattern")
