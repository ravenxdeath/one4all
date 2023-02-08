 #! BARANCHING AND CONDITOANL STATEMENT

import numbers


canWatchAnime = True
if(canWatchAnime):
    print("Will watch a new anime")

canWatchAnime = False
if(canWatchAnime):
    print("Will watch a new anime") #* nothing will be shown
    
a = 16
if (a>10):
    print("a is greater")
print("code ended")

canWatchAnime = False
if(canWatchAnime):
    print("Will watch a new anime")        
else:
    print("will watch YouTube")

x = 16
if(x%2 ==0):
    print("Even number")
else:
    print("Odd Number")

WatchAnime = False
if(WatchAnime):
    print("AnimeTime")
elif(WatchAnime):   # code here did not run
    print("WatchYT")
else:
    print("RestUpSOldier")


a = 10
b = 70
if(a>b):
    print("a is greater than b")
elif(a<b):
    print("a is smaller than b")
    print("didn't expect that")
else:
    print("a and b are equal")    
print("code ended")

#! """"we can write any text expression as long as it returns boolean or integer value"""
a =11
b =23
c =["audi, bmw"]
d = "bmw"

if a < b:
    print(" a is smaller")
if d in c:
    print("d is in c")
if d == "bmw":
    print("d is equal to bmw")
if a % 2:
    print("it is an odd number") #* if it's false then the code won't be executed
    
#! and or not statements
a = 10
b = 20
if (a>15 and b<30):
    print("both conditions are true") #* did not execute cause it's false
if (a>5 or b<10):
    print("one of the conditions is true")

w = 77
print(not(w>69))

print("tahmid is good")
#! argument separate = sep
print("tahmid","is","good", sep="....")
#! argument end
print("tahmid", end=" ")
print("tamiddo-san", end="/")
print(" tahmid is good")