

def skill_set(skills):

    result=""

    fr=open("ERROR HANDLING\\skills.txt")

    set_skill=[line.rstrip("\n")for line in fr]

    skill_check=[s for s in skills.split(" ") if s in set_skill]

    result=" ".join(skill_check)

    return result

skill1="Git Python Angular"

skill2="Angular React Communication"

print(skill_set(skill1))

print(skill_set(skill2))


assert skill_set(skill1)=="Git Python","Test case1 failed"

assert skill_set(skill2)=="Angular React","Test case2 failed"


print("code accepted.....")












    