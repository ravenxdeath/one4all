def WaysCounted(n):
    if n <= 1:
        return n
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b

def processInputAndOutput(input_path, output_path):
    with open(input_path, 'r') as f01:
        lines = f01.readlines()
    
    results = []
    for line in lines:
        n = int(line.strip())
        ways = WaysCounted(n)
        results.append(ways)
    
    with open(output_path, 'w') as f02:
        for result in results:
            f02.write(str(result) + '\n')

input_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB08\\task02_input01.txt"
output_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB08\\task02_output01.txt"
input_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB08\\task02_input02.txt"
output_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB08\\task02_output02.txt"

input_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB08\\task02_input03.txt"
output_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB08\\task02_output03.txt"

input_file_path04 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB08\\task02_input04.txt"
output_file_path04 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB08\\task02_output04.txt"

processInputAndOutput(input_file_path01, output_file_path01)
processInputAndOutput(input_file_path02, output_file_path02)
processInputAndOutput(input_file_path03, output_file_path03)
processInputAndOutput(input_file_path04, output_file_path04)


