"""
Anagram


"""

word1  ="silent"

word2 = "listen"

is_anagram=True


for ch in word1:

    if ch not in word2:

        is_anagram=False

        break
print(is_anagram)





   