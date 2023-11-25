input_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task07_input01.txt"
output_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task07_output01.txt"

input_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task07_input02.txt"
output_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task07_output02.txt"

input_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task07_input03.txt"
output_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task07_output03.txt"

def dfs(u, graph, visited, PathLen):
    visited[u] = True
    maxPathLen = PathLen
    farthest_node = u

    for v in graph[u]:
        if not visited[v]:
            new_PathLen, new_farthest_node = dfs(v, graph, visited, PathLen + 1)
            if new_PathLen > maxPathLen:
                maxPathLen = new_PathLen
                farthest_node = new_farthest_node

    return maxPathLen, farthest_node

def GimmeOutputAtOnce(input_file_path, output_file_path):
    with open(input_file_path, 'r') as f:
        N = int(f.readline().strip())
        graph = {i: [] for i in range(1, N + 1)}

        for _ in range(N - 1):
            u, v = map(int, f.readline().strip().split())
            graph[u].append(v)
            graph[v].append(u)

    visited = [False] * (N + 1)
    maxPathLen, farthest_node = dfs(1, graph, visited, 0)

    visited = [False] * (N + 1)
    maxPathLen, second_farthest_node = dfs(farthest_node, graph, visited, 0)

    with open(output_file_path, 'w') as f:
        f.write(f"{farthest_node} {second_farthest_node}\n")


GimmeOutputAtOnce(input_file_path01, output_file_path01)
GimmeOutputAtOnce(input_file_path02, output_file_path02)
GimmeOutputAtOnce(input_file_path03,output_file_path03)
