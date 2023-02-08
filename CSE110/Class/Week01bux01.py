# floor division
from lib2to3.pgen2.token import COMMENT


print(3.6//2)
print(67//1.2)
x =3
x =x**3
print(x)

# mod operator
xy =23
yz =11
print(yz%xy)
print(23%11)
print(11%23) # if you divide something smaller with a bigger number the reminder would be the one that was supposed to get devided

# using assignment operator
x =3
print(x**3)

x +=3
x /=2
print(x) # x=3+3=6/2=3
print(x ==2)

# identity operators and mentorship operator
c =2
d =5
print(c is not d)

q =["Apple, Android, Windows, Linux"]
print("unix" not in q) # membership operator

#! INPUT FUNCTION, TYPE CONVERSION, COMMENT

s =input("Who Goes there:")
print("Name yourself:",s)

t =input("Enter a number:")
print("Your Number:", t)

#! Casting: putting int before input to make str into a int
t =int(input("Enter a number:"))
t =22+t
print(t)

print(float("2.5")) 
print(str(12.3))

#! del variable 
greet = "Ohayo!"
del greet
# print(greet)



            #* WEEK ONE COMPELTE