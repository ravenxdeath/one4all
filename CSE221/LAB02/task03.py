# As it is performing the merge sort, so the time complexity would b O(nlogn).

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        leftSide = mergeSort(arr[:mid])
        rightSide = mergeSort(arr[mid:])
        return merge(leftSide, rightSide)
    
# Takes and array recursively divides it into chunks until base case len(arr)<= 1 
# and it calls the merge function below which sorts the array recursively. 

def merge(a, b):
    merged = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):    #loop checks which is greater and appends that elem
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    while i < len(a):                   #merges the remaining elements of the a subarr 
        merged.append(a[i])
        i += 1

    while j < len(b):                   #merges the remaining elements of the b subarr 
        merged.append(b[j])
        j += 1

    return merged


with open("C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB02\\task03_input.txt", "r") as f01, \
     open("C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB02\\task03_output.txt", "w") as f02:

    n = int(f01.readline().strip())
    arr = list(map(int, f01.readline().split()))

    sorted_arr = mergeSort(arr)

    f02.write(" ".join(map(str, sorted_arr)))

# time complexity of the merge sort algo is O(nlogn). 