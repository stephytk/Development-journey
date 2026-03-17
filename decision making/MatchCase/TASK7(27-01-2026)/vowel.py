"""
Write a program that takes a character and checks whether it is a vowel or consonant using match–case.
"""

Character=input("Enter the character :") 

match Character:

    case "a":print(Character, " is a vowel")

    case "e":print(Character," is a vowel")

    case "i":print(Character," is a vowel")

    case "o":print(Character,"is a vowel")

    case "u":print(Character," is a vowel")
    
    case _: print(Character,"is a consonant")
      

    
    
    
    
    
    # case "a"| "e" |"i" |  "o" |  "u": print(Character," is a Vowel")
       
    # case _: print("Consonant")


      
          

