# inputs taken will be called from "allin1funcforFiles"and will be written to ourput files for each given inputs file

input_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB03\\task01_input01.txt"
output_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB03\\task01_output01.txt"
input_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB03\\task01_input02.txt"
output_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB03\\task01_output02.txt"
input_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB03\\task01_input03.txt"
output_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB03\\task01_output03.txt"


def mergeCount(arr, left, mid, right):
    count = 0
    temp = []           # will strore sorted arr
    i = left            # Starting index of the left subarr
    j = mid + 1         # starting index of the righty subarr

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            count += mid - i + 1        # Counts inversions when arr[i] > arr[j]
            j += 1

    while i <= mid:                     # adds remaining elems of lft subarr
        temp.append(arr[i])
        i += 1

    while j <= right:                   # adds remaining elems of right subarr
        temp.append(arr[j])
        j += 1

    arr[left:right + 1] = temp          # transfers elems to temp 
    return count

def mergeSort_cournt(arr, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2
        count += mergeSort_cournt(arr, left, mid)
        count += mergeSort_cournt(arr, mid + 1, right)
        count += mergeCount(arr, left, mid, right)
    return count

# above func will recursively mergeSort on the input arr for left and right side.
#deviding the arr in halves then again mergesort for those halves and 
# using mergeCount returns inversion count 

def countPairsRespect2Height(arr):
    return mergeSort_cournt(arr, 0, len(arr) - 1)

def allin1funcforFiles(input_file_path, output_file_path):
    with open(input_file_path, 'r') as f01:
       
        N = int(f01.readline())
        heights = list(map(int, f01.readline().split()))

    
    result = countPairsRespect2Height(heights)

    with open(output_file_path, 'w') as f02:
    
        f02.write(str(result))

allin1funcforFiles(input_file_path01,output_file_path01)
allin1funcforFiles(input_file_path02,output_file_path02)
allin1funcforFiles(input_file_path03,output_file_path03)


