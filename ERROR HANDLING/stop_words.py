




def remove_stop_words(sentence):
      
      result=""

      fr=open("ERROR HANDLING\\stop_words.txt")

      stop_words=[line.rstrip("\n") for line in fr]

      cleaned_word=[w for w in sentence.split(" ") if w not in stop_words]

      result=" ".join(cleaned_word)

      return result

sentence2="Machine learning is subset of AI"

sentence3="django is one of python framework"

print(remove_stop_words(sentence2))

assert remove_stop_words(sentence2)=="Machine learning subset AI","Test case1 failed"

assert remove_stop_words(sentence3)=="django one python framework","Test case2 failed"

print("code accepted...")














    
      

        

        


    

    
















