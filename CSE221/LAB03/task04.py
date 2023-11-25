def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# this fuction basically works just like the partiion of the quichsort algorithm. 
# takes arr and sel last elem as the pivot

def quickselect(arr, low, high, k):         # finds the kth smallest elem
    if low <= high:
        indexOfourPivot = partition(arr, low, high)
        if k - 1 == indexOfourPivot:
            return arr[indexOfourPivot]
        elif k - 1 < indexOfourPivot:
            return quickselect(arr, low, indexOfourPivot - 1, k)
        else:
            return quickselect(arr, indexOfourPivot + 1, high, k)
    return -1

input_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB03\\task04_input01.txt"
output_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB03\\task04_output01.txt"

with open(input_file_path01, 'r') as f01:
    N = int(f01.readline())                          # length of the list
    arr = list(map(int, f01.readline().split()))    # list of numbers
    Q = int(f01.readline())                         # number of queries
    queries = [int(f01.readline()) for _ in range(Q)]   # list of queries

results = []
for k in queries:
    kth_smallest = quickselect(arr, 0, N - 1, k)
    results.append(kth_smallest)

with open(output_file_path01, 'w') as f02:
    for result in results:
        f02.write(str(result) + '\n')
