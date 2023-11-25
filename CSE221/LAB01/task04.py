input_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB01\\task04_input.txt"
output_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB01\\task04_output.txt"


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            merged.append(left[i])
            i += 1
        elif left[i][0] > right[j][0]:
            merged.append(right[j])
            j += 1
        else:
            if left[i][1] <= right[j][1]:  # Compare departure times in ascending order
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


input_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB01\\task04_input.txt"
output_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB01\\task04_output.txt"

# Read the input file and sort the train schedules
with open(input_file_path, 'r') as input_file:
    n = int(input_file.readline().strip())
    sorted_train_schedules = merge_sort([
        (line.split(' will departure for ')[0], line.split(' will departure for ')[1])
        for line in input_file.readlines()
    ])

# Write the sorted train schedules to the output file
with open(output_file_path, 'w') as output_file:
    for train_schedule in sorted_train_schedules:
        output_file.write(f"{train_schedule[0]} will departure for {train_schedule[1]}\n")
