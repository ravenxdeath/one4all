input_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB02\\task01_2_O(n)_input.txt"
output_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB02\\task01_2_O(n)_output.txt"

def sumPair(arr, sumo):
    num_dict = {}
    for i, num in enumerate(arr):
        differ = sumo - num
        if differ in num_dict:
            return [num_dict[differ], i + 1]
        num_dict[num] = i + 1
    return "Impossible"

# Using a "sumpair" function & dictionary we get rid of the nested loops> here "sumpair" fuction iterates over teh input list "arr" only once for which the time complexity stands O(n). 

with open(input_file_path, "r") as f01, open(output_file_path, "w") as f02:
    lenArr, sumo = map(int, f01.readline().strip().split())
    arr = list(map(int, f01.readline().strip().split()))

    result = sumPair(arr, sumo)

    if result == "Impossible":
        f02.write("Impossible")
    else:
        f02.write(str(result[0]) + " " + str(result[1]))

    f02.close()
    f01.close()

