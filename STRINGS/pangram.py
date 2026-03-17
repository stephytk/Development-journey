"""

"""

word="The quick brown for jumps over lazy dog"

# word=word.casefold()


alphabet="abcdefghijklmnopqrstuvwxyz"

is_pangram = True

for ch in alphabet:

    if ch not in alphabet:

        is_pangram = False

        break

print(is_pangram)


