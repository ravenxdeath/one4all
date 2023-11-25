#! Creation

from array import *

arr1 = array("i", [1,2,3,4,5])

for i in arr1:
    print(i) 
    
print(arr1[len(arr1)-1])
print(arr1[4])

#! Insertion

arr1.insert(2,9)
print(arr1[2])

#! Deletion

arr1.remove(5)
print(arr1)

#! Search

print(arr1.index(9))

#! Update

arr1[3] = 69
print(arr1[3])
print(arr1)


#! circular arr
 
arr22 = [30, 40, None , 10 , 20 ]
st = 3
size = 4

last = (st+ size-1) % len(arr22)
print(last)

for i in range(len(arr22)):
    print(arr22[st])
    st = (st + 1) %(len(arr22))

