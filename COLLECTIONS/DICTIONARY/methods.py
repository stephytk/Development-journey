"""

class dict

  def keys(self)

  def values(self)

  def items(self)

  def get(self,key)

  def pop(self,key)


"""

employee={"id":123,"name":"hari","salary":50000,"dept":"qa"}

print(employee.get("name"))

print(employee.get("email","dummy@gmail.com"))

#pop method

employee.pop("dept")

print(employee)

#add bonus into the dictionary

employee["bonus"]=5000

print(employee)


#update the salary with 10000

employee["salary"]+=10000

print(employee)
# for key in employee.keys():

#     print(key)

# for val in employee.values():

#     print(val)

# for key,val in employee.items():


#     print(key,val)


