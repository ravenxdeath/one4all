input_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB01\\task02_input01.txt"
output_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB01\\task02_outpu01.txt"
input_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB01\\task02_input02.txt"
output_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB01\\task02_output2.txt"


def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False # Flag to check if any swaps are made during the iteration
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped: # Already Sorted
            break
    return arr


# Reading input from task02_input01.txt
with open(input_file_path01, 'r') as f01:
    n = int(f01.readline().strip())
    arr = list(map(int, f01.readline().strip().split()))

# Function call for bubble sort
sorted_arr = bubbleSort(arr)

# Writing output to task02_output01.txt
with open(output_file_path01, 'w') as f02:
    f02.write(' '.join(map(str, sorted_arr)))


# Reading input from task02_input02.txt
with open(input_file_path02, 'r') as f01:
    n = int(f01.readline().strip())
    arr = list(map(int, f01.readline().strip().split()))

# Function call for bubble sort
sorted_arr = bubbleSort(arr)

# Writing output to task02_output02.txt
with open(output_file_path02, 'w') as f02:
    f02.write(' '.join(map(str, sorted_arr)))
