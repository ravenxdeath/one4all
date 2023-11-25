def bfs_topoSort(n, prereqs):
    in_degree = [0] * (n + 1)   #to keep track of the incoming edges for each course
    graph = {i: [] for i in range(1, n + 1)}  #adjacency list of the courses; stores prereqs

# checks if there's any prereqs  (in_degree = 0) ; 
    for a, b in prereqs:
        graph[a].append(b)
        in_degree[b] += 1

    queue = []
    for i in range(1, n + 1):    
        if in_degree[i] == 0:
            queue.append(i)

    result = []
    while queue:
        node = queue.pop(0)
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) == n:
        return result
    else:
        return "IMPOSSIBLE"


# input_file = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task01_b_input01.txt"
# output_file = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task01_b_output01.txt"

input_file = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task01_b_input02.txt"
output_file = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task01_b_output02.txt"


# input_file = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task01_b_input03.txt"
# output_file = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task01_b_output03.txt"



with open(input_file, 'r') as f01:
    N, M = map(int, f01.readline().split())
    prereqs = [tuple(map(int, f01.readline().split())) for _ in range(M)]


res = bfs_topoSort(N, prereqs)

with open(output_file, 'w') as f02:
    if res == "IMPOSSIBLE":
        f02.write(res)
    else:
        f02.write(' '.join(map(str, res)))
