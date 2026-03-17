
source ="traviduxtechnology"

target ="vridautx"

present =True

for ch in target:

    if ch not  in source:

        present=False

        break
print(present)

        
#with class 

class Containerword:

    def solution(self,source:str,target:str):

        present = True

        for ch in target:

            if ch not in source:

                present =False

                break

        return present

word_instance = Containerword()

print(word_instance.solution("traviduxtechnology","vridautxz"))

#with set 

class Containerword:

    def solution(self, source: str, target: str):
        

        present = set(target).issubset(set(source))


        return present


word_instance = Containerword()

print(word_instance.solution("traviduxtechnology", "vridautxz"))




