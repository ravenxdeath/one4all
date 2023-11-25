input_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB01\\task03_input01.txt"
output_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB01\\task03_outpu01.txt"
input_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB01\\task03_input02.txt"
output_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB01\\task03_output2.txt"


def bubble_sort(arr, marks):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if marks[j] < marks[j+1] or (marks[j] == marks[j+1] and arr[j] > arr[j+1]):
                # Swapping marks
                marks[j], marks[j+1] = marks[j+1], marks[j]
                # Swapping IDs
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Reading input 
def read_input(file_path):
    with open(file_path, 'r') as f01:
        n = int(f01.readline())
        ids = list(map(int, f01.readline().split()))
        marks = list(map(int, f01.readline().split()))
    return n, ids, marks

# Writing output 
def write_output(file_path, n, ids, marks):
    with open(file_path, 'w') as f02:
        for i in range(n):
            f02.write(f"ID: {ids[i]} Mark: {marks[i]}\n")


# Main function
def rank_students(input_file_path, output_file_path):
    n, ids, marks = read_input(input_file_path)
    bubble_sort(ids, marks)
    write_output(output_file_path, n, ids, marks)

# Fuction calls for given input files
rank_students(input_file_path01, output_file_path01)
rank_students(input_file_path02, output_file_path02)
