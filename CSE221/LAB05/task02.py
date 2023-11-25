def lexico_SmallerPath(N, prereqs):
    indegree = [0] * (N + 1)     # tracking incoming edges 
    adj_list = [[] for i in range(N + 1)]  #courses ls
    
    for A, B in prereqs:
        adj_list[A].append(B)
        indegree[B] += 1
    
    
    # initializing a que 
    queue = [i for i in range(1, N + 1) if indegree[i] == 0] # no prereqs 
    sequence = []   #stores the lexicographically smallest valid course sequence
    
    while queue:
        queue.sort()
        course = queue.pop(0)
        sequence.append(course)
        
        for next_course in adj_list[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)
    
    if len(sequence) != N:
        return "IMPOSSIBLE"
    else:
        return " ".join(map(str, sequence))

# The above func checks the courses that have no prerequisites and gradually adds courses with their #prerequisites fulfilled. if valid sequences = Truee then return sequence. else impossible. 

def reading_In(input_file):
    with open(input_file, 'r') as f:
        N, M = map(int, f.readline().split())
        prereqs = [tuple(map(int, f.readline().split())) for i in range(M)]
    return N, prereqs

def Writing_Out(output_file, result):
    with open(output_file, 'w') as f:
        f.write(result)

def GimmeOutputAtOnce(input_file_path, output_file_path):
    N, prereqs = reading_In(input_file_path)
    result = lexico_SmallerPath(N, prereqs)
    Writing_Out(output_file_path, result)


input_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task02_input01.txt"
output_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task02_output01.txt"
input_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task02_input02.txt"
output_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task02_output02.txt"
input_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task02_input03.txt"
output_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task02_output03.txt"

GimmeOutputAtOnce(input_file_path01, output_file_path01)
GimmeOutputAtOnce(input_file_path02, output_file_path02)
GimmeOutputAtOnce(input_file_path03, output_file_path03)

