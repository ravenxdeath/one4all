#Iteration WHile Loop
count  =0
while(count<5):
    print("CS is not as awesome as I thought")
    count =count+1

#! e.g: WHile with If
count =1
while(count<=10):
    if(count%2 ==0):
        print(count)
    count= count+1
# ! break func to break the infinite looop
count =1
while True:
    print(count)
    count= count+1
    if count == 5:
        break
# ! continue
count =0
while count<5:
    count=count+1
    if count ==3:
        continue
    print("To Be Continued",count)
# !  Nested While
outer = 1
while outer<=2:
    inner =1
    while inner <=3:
        print(outer,",",inner)
        inner =inner+1
    print("inner loop terminated")
    outer =outer+1
print("outer loop terminated")

# *     Next chapter

#! List iteration
B = ["Cersei","JAIME","DANY","Jon"]
print(B[0])
print(B[3])
print(B[2])
print(len(B)) # * The lenght of  a list
#! For Loop
for count in B:
    print(count)
    
               ### WE'll use the same for while using len

a = [7,8,9,10,11]
i = 0
while i <len(a):
    print(a[i], sep=",")
    i = i+1
        
a=[1,2,3,4,5,6,7]

for  i in a:
    print(i,sep=", ")

#* sum using for
a = [22,44,555,6,457]
sum = 0
for i in a:
    sum = sum+i
print(sum)

b=[343,53563,64674]
largest = -999 #imaginary variable value
for i in b:
    if i > largest:
        largest =i
print(largest)

for i in range (0, 11, 1):
    print(i , end=" ")
print("\nfinished") 
    
for i in range (12):
    print(i , end=" ")
print("finished")


#! for loops
a = [145,256,343,475,557,5756]
sum = 0
for i in a:
    sum = sum+i
print(sum)


for i in range(12):
    print("Assignment due broo")


for i in ["lily", "buttercup", "Sunflower"]:
    if i == "Sunflower":
        break
    print(i)
for i in ["lily", "buttercup", "Sunflower"]:
    if i == "buttercup":
        continue
    print(i)

#* RANGE func
for c in range(1,8,3):
    print(c)