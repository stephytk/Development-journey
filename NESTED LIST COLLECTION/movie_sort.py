""""""
languages=["thamil","malayalam","kannada","telungu","kannada","telungu","thamil","malayalam","thamil","malayalam"]

language_count={lang:languages.count(lang) for  lang in languages }

language_list=[[v,k] for k,v in language_count.items()]

print(sorted(language_list,reverse=True))

