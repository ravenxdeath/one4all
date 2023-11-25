# inputs taken will be called from "allin1funcforFiles"and will be written to ourput files for each given inputs file

input_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB03\\task02_input01.txt"
output_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB03\\task02_output01.txt"
input_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB03\\task02_input02.txt"
output_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB03\\task02_output02.txt"
input_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB03\\task02_input03.txt"
output_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB03\\task02_output03.txt"

def find_max_sum(input_ls):
    max_sum = float('-inf')
    max_elem = float('-inf')  # both are initialized with negative infinity values

    for num in input_ls:
        max_sum = max(max_sum, max_elem + num**2)
        max_elem = max(max_elem, num)
    
    return max_sum

#this func has a time complexity of "O(n)" as it takes input list of n mumber elms.
#The fuction iterates over the input ls only once

def allin1funcforFiles(input_file_path, output_file_path):
    with open(input_file_path, 'r') as f01:
        n = int(f01.readline())
        input_ls = list(map(int, f01.readline().split()))

    max_sum = find_max_sum(input_ls)

    with open(output_file_path, 'w') as f02:
        f02.write(str(max_sum))

# writng the output takes on constant time for which time complexity is O(1)

allin1funcforFiles(input_file_path01, output_file_path01)
allin1funcforFiles(input_file_path02, output_file_path02)
allin1funcforFiles(input_file_path03, output_file_path03)

# this function call was doen trice so the tc is O(3n)  ### we can also ignore this as
# it was created for the eficiency of taking and creating output files easily

#Total time complexity O(n)+O(1)+o(3n) = "O(n)"