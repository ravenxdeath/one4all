def maxCompletedTasks(tasks, M):
  
    def sort_key(task):            #sorign keys for tasks basked on end time
        return task[1]

    tasks.sort(key=sort_key)
    
    assignedTasks = [0] * M     # keeping track of assigned tasks&end times for each person
    
    completedTasks = 0

    for task in tasks:          # Iterating through each task to assign them to persons
        stTime, EndTime = task
        assigned_person = None

        for person in range(M): # availibe -> assign tasks 
            
            if assignedTasks[person] <= stTime:
                assigned_person = person
                break

        if assigned_person is not None:
            assignedTasks[assigned_person] = EndTime
            completedTasks += 1

 
    return completedTasks

 
def gimme_output_at_once(input_file_path, output_file_path):
   
    with open(input_file_path, 'r') as input_file:
        N, M = map(int, input_file.readline().split())
        tasks = []
        for i in range(N):
            stTime, EndTime = map(int, input_file.readline().split())
            tasks.append((stTime, EndTime))

    
    result = maxCompletedTasks(tasks, M)
 
    with open(output_file_path, 'w') as output_file:
        output_file.write(str(result))
 
input_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB07\\task02_input01.txt"
output_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB07\\task02_output01.txt"
gimme_output_at_once(input_file_path01, output_file_path01)

input_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB07\\task02_input02.txt"
output_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB07\\task02_output02.txt"
gimme_output_at_once(input_file_path02, output_file_path02)

input_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB07\\task02_input03.txt"
output_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB07\\task02_output03.txt"
gimme_output_at_once(input_file_path03, output_file_path03)

input_file_path04 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB07\\task02_input04.txt"
output_file_path04 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB07\\task02_output04.txt"
gimme_output_at_once(input_file_path04, output_file_path04)
