"""

String Palindrome 
"""

word=input("Enter the string :")#madam

word_length=len(word)-1

result="" #"m" ,#"ma" 

for i in range(word_length,-1,-1):#0-4

    result=result+word[i]# word[i]=>index position of the char

print("palindrome" if result==word else "not a palindrome")


#with function


def palindrome_string(word):


    word_len= len(word )-1
    
    result =""

    for i in range(word_len,-1,-1):

        result = result + word[i]


    return "palindrome" if result==word else "not a palindrome"
    
word = input("enter the string")   

result = palindrome_string(word)

print(result)


#with class

class Palindrome:

    def palindrome_string(word):

        word_len = len(word)-1

        result =""

        for i in range(word_len,-1,-1):

            result = result +word [i]

        return 