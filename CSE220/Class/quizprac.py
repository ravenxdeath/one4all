#! circular arr
 
arr22 = [30, 40, None , 10 , 20 ]
st = 3
size = 4

last = (st+ size-1) % len(arr22)
print(last)

for i in range(len(arr22)):
    print(arr22[st])
    st = (st + 1) %(len(arr22))

#! adding 2 arrays in circular array

arr1  = [10, 15, 20, 25]
arr2 =  [60, 70, 60, 40]

sz1 = 4
sz2 = 4
cirarr = [0, 0,0, 0]
st  = 2

for i in range(len(cirarr)): 
    elem = arr1[i] + arr2[len(arr2) - 1 - i]
    cirarr[i] = elem
    print(cirarr[i])
    st = (st + 1)%(len(cirarr))
print(cirarr)
