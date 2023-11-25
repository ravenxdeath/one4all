    
input_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB01\\task01_b_input.txt"
output_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB01\\task01_b_output.txt"

with open(input_file_path, "r") as f01, open(output_file_path, "w") as f02:

    t = int(f01.readline()) 
    
    # for i in range(t):  #can't iterate over int vals.
    
    for i in f01:  # Iterate over i in the input file
        
        if i.startswith("calculate"):
            calc = i.split("calculate ")
            calx = calc[1].strip()       
            result = eval(calx)
            f02.write(f"The result of {calx} is {result}\n")
