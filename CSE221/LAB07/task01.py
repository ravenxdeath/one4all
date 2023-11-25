def solve_task(tasks):
    
    for i in range(len(tasks)):              # selection sort --> end time
        min_idx = i
        for j in range(i + 1, len(tasks)):
            if tasks[j][1] < tasks[min_idx][1]:
                min_idx = j
        tasks[i], tasks[min_idx] = tasks[min_idx], tasks[i]
    
    
    given_tasks = []
    prev_end_time = -1
    
    for task in tasks:                                 # iteration through sorted tasks 
        if task[0] >= prev_end_time:
            given_tasks.append(task)
            prev_end_time = task[1]
    
    return given_tasks

def gimme_output_at_once(input_file_path, output_file_path):
    # Read input from input file
    with open(input_file_path, 'r') as input_file:
        N = int(input_file.readline())
        tasks = []
        for i in range(N):
            start, end = map(int, input_file.readline().split())
            tasks.append((start, end))
    
    given_tasks = solve_task(tasks)

    with open(output_file_path, 'w') as output_file:
        output_file.write(str(len(given_tasks)) + '\n')
        for task in given_tasks:
            output_file.write(str(task[0]) + ' ' + str(task[1]) + '\n')

input_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB07\\task01_input01.txt"
output_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB07\\task01_output01.txt"


input_file_path02= "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB07\\task01_input02.txt"
output_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB07\\task01_output02.txt"


input_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB07\\task01_input03.txt"
output_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB07\\task01_output03.txt"


gimme_output_at_once(input_file_path01, output_file_path01)
gimme_output_at_once(input_file_path02, output_file_path02)
gimme_output_at_once(input_file_path03, output_file_path03)

