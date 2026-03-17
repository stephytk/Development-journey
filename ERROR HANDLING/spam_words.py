

def count_spam_words(message):

    count=0

    fr=open("ERROR HANDLING\\spam_words.txt")

    spam_words=[line.rstrip("\n") for line in fr]

    spam_words_count=[w for w in message.split(" ")if w in spam_words]

        

    count=len(spam_words_count)
    
    return count

message2="you win free cash"

message3="congratulations you are winner"

print(count_spam_words(message2))

print(count_spam_words(message3))


assert count_spam_words(message2)==2,"test case1 failed"

assert count_spam_words(message3)==2,"test case2 failed"

print("code accepted....")























 