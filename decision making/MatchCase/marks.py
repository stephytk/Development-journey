"""
read grade

"""
grade=(input("enter the mark :"))

match grade:
     case "A" :print ("Excellent")

     case "B" :print ("good")

     case "C" :print ("average")

     case _: print("fail")
