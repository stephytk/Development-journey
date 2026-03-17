"""
def 'index'(self,substr)
def 'find'(self,substr)
def 'rfind'(self,substr)
def  'count'(self,substr)

def isalpha()

def isalnum()

def isdigit()

def startswith(self,prefix)

def endsswith(self,suffix)

def strip(self)

def lstrip()
def rstrip()
"""

word="   \nLuminar technolab\t "

alpha="hello"
digit="123"
alph="hello123"
# print(word.index("ch")) #if two 'ch' in  a word =>First index will execute.

# print(word.index("lab"))

# print(word.find("labs"))

# print(word.rfind("lab"))#24

# print(word.count("Techs"))#2

# print(alpha.isalpha())#return true if str object is alphabet

# print(digit.isdigit())#return true if str object is digit

# print(alph.isalnum())#return true if str object is alphanumeric

# print(word.startswith("lu"))#Return true if str is starts with prefix

# print(word.endswith("lab"))#Return true if str is ends with suffix.

print(f"left{word.strip()}right")

word1="\nLuminar\t"

new_word=word1.lstrip("\n")

new_word=new_word.rstrip("\t")

print(new_word)

