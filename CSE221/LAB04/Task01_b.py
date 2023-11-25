def adj_matrix(N, M, edges):
    
    adjacency_list = [[] for i in range(N)]

 
    for u, v, w in edges:
        adjacency_list[u].append((v, w))

    return adjacency_list

 
input_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\task01_b_input02.txt"
output_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\task01_b_output02.txt"

with open(input_file_path, 'r') as F01:
    N, M = map(int, F01.readline().split())
    edges = []
    for i in range(M):
        u, v, w = map(int, F01.readline().split())
        edges.append((u, v, w))

 
adjacency_list = adj_matrix(N + 1, M, edges)
 
with open(output_file_path, 'w') as F02:
    for i, n in enumerate(adjacency_list):
        F02.write(f"{i} : ")
        if n:
            for x, w in n:
                F02.write(f"({x},{w}) ")
        F02.write("\n")
