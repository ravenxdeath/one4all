def QuickSort(A, low, high):
    if low < high:
        q = Partition(A, low, high)
        QuickSort(A, low, q - 1)
        QuickSort(A, q + 1, high)

def Partition(A, low, high):
    x = A[high]
    i = low - 1
    for j in range(low, high):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[high] = A[high], A[i + 1]
    return i + 1

input_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB03\\task03_input01.txt"
output_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB03\\task03_output01.txt"
input_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB03\\task03_input02.txt"
output_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB03\\task03_output02.txt"

with open(input_file_path01, 'r') as f01:
    N = int(f01.readline())
    ls = list(map(int, f01.readline().split()))
    
QuickSort(ls, 0, N - 1)

with open(output_file_path01, 'w') as f02:
    f02.write(' '.join(map(str, ls)))
