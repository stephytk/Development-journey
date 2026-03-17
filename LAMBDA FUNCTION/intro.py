"""
Definition : Anonymous function with single expression

Syntax : var_name= lambda p1,p2:expression


"""

#add two numbers

add=lambda n1,n2:n1+n2

print(add(100,200))

#Subtract two numbers

sub=lambda n1,n2:n1-n2

print(sub(100,20))

#Cube of a number

cube=lambda n:n**3

print(cube(3))


#odd or even

odd_even=lambda num:"even" if num%2==0 else "odd"

print(odd_even(10))

#positive 

is_positive=lambda num: num>0 

print(is_positive(10))
print(is_positive(-10))