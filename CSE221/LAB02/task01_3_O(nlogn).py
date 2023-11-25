# we  can easily achieve O(nlogn) time complexity by utilizing the merge sortt algo.
#  Modified the previous code. 

input_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB02\\task01_3_O(nlogn)_input.txt"
output_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB02\\task01_3_O(nlogn)_output.txt"

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

# Merge_sort func takes and array recursively divides it into chunks until base case len(arr)<= 1 satisfied. 

def merge(left, right):
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):            #merges the remaining elements of the left subarr 
        merged.append(left[i])
        i += 1

    while j < len(right):           #merges the remaining elements of the right subarr 
        merged.append(right[j])
        j += 1

    return merged

def sumoPair(arr, targetSumo):
    sorted_arr = merge_sort(arr)  # Sort the array using merge sort
    left = 0
    right = len(sorted_arr) - 1

    while left < right:
        current_sumo = sorted_arr[left] + sorted_arr[right]

        if current_sumo == targetSumo:
            return [arr.index(sorted_arr[left]) + 1, arr.index(sorted_arr[right]) + 1]  # Return indices (1-based)
        elif current_sumo < targetSumo:
            left += 1
        else:
            right -= 1

    return "Impossible"


with open(input_file_path, "r") as f01, open(output_file_path, "w") as f02:
    lenArr, sumo = map(int, f01.readline().strip().split())
    arr = list(map(int, f01.readline().strip().split()))

    result = sumoPair(arr, sumo)

    if result == "Impossible":
        f02.write("Impossible")
    else:
        f02.write(str(result[0]) + " " + str(result[1]))

    f02.close()
    f01.close()





