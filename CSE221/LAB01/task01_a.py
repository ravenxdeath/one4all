    
input_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB01\\task01_a_input.txt"
output_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB01\\task01_a_output.txt"

with open(input_file_path, "r") as f01, open(output_file_path, "w") as f02:

    t = int(f01.readline())
    for i in range(t):
        i = int(f01.readline())
        if i%2 == 0 :
            f02.write(f"{i} is an EVEN number.\n")
        else: 
            f02.write(f"{i} is an ODD number.\n")
    print(t)