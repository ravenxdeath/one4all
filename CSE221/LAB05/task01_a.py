def dfs(node, graph, visited, result):
    if visited[node] == 1:
        return False
    if visited[node] == 2:
        return True
    
    visited[node] = 1
    
    for neighbor in graph[node]:
        if not dfs(neighbor, graph, visited, result):
            return False
        
    visited[node] = 2
    result.append(node)
    return True

#using dfs to explore the graph and find the topological order  of athe courses 

# As MENTIONED in the question "Please note,
# there could be multiple correct sequences" My solution is different then the given output

def find_order_dfs(num_courses, prerequisites):
    graph = {i: [] for i in range(1, num_courses + 1)}  #initializes an empty graph dictionary 
    for prerequisite in prerequisites:                  # KEYS ---> COURSES; VALUES ---> PREREQ 
        graph[prerequisite[0]].append(prerequisite[1])

    visited = [0] * (num_courses + 1)
    result = []

    for i in range(1, num_courses + 1):
        if not dfs(i, graph, visited, result):
            return "IMPOSSIBLE"

    return result[::-1]

# input_file = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task01_a_input01.txt"
# output_file = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task01_a_output01.txt"

# input_file = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task01_a_input02.txt"
# output_file = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task01_a_output02.txt"


input_file = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task01_a_input03.txt"
output_file = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task01_a_output03.txt"

with open(input_file, 'r') as f01:
    N, M = map(int, f01.readline().split())
    prerequisites = [tuple(map(int, f01.readline().split())) for _ in range(M)]


result_dfs = find_order_dfs(N, prerequisites)

with open(output_file, 'w') as f02:
    if result_dfs == "IMPOSSIBLE":
        f02.write(result_dfs + "\n")
    else:
        f02.write(" ".join(map(str, result_dfs)) + "\n")
