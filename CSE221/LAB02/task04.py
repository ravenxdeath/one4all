# This code performs merge sort algorithm for which the time complexity would be O(nlogn). 

input_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB02\\task04_input.txt"
output_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB02\\task04_output.txt"

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftSide = merge_sort(arr[:mid])
    rightSide = merge_sort(arr[mid:])

    return merge(leftSide, rightSide)

# merfe_sort func takes and array recursively divides it into chunks until base case len(arr)<= 1 
# and it calls the merge function below which sorts the array recursively. 

def merge(left, right):
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right): # loop checks which si greater and appends
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):                 #merges the remaining elements of the subarr 
        merged.append(left[i])
        i += 1

    while j < len(right):                #does the same thing as above when right arr has elems
        merged.append(right[j])
        j += 1

    return merged

with open(input_file_path, 'r') as f01:
    n = int(f01.readline().strip())
    arr = list(map(int, f01.readline().strip().split()))

sortedArr = merge_sort(arr)

max_value = sortedArr[-1]  #as it's the max value and it's at the end 

with open(output_file_path, 'w') as f02:
    f02.write(str(max_value))

