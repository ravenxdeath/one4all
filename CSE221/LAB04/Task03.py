
input_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\task03_input01.txt"
output_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\task03_output01.txt"

# input_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\task03_input02.txt"
# output_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\task03_output02.txt"

# input_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\task03_input03.txt"
# output_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\task03_output03.txt"

# input_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\task03_input04.txt"
# output_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\task03_output04.txt"

def initialize_graph(N):
    # Initializing an empty adjacency list for each vertex
    graph = [[] for i in range(N + 1)]

    return graph


def add_edge(graph, u, v):
    # Adding bidirectional edges to the graph
    graph[u].append(v)
    graph[v].append(u)


def dfs_helper(graph, u, visited, dfs_path):
    # Marking the current vertex as visited
    visited[u] = True

    # Adding the current vertex to the DFS path
    dfs_path.append(u)

    # Exploring all adjacent vertices
    for v in graph[u]:
        if not visited[v]:
            dfs_helper(graph, v, visited, dfs_path)


def dfs(graph, N):
    # Initializing the visited arr and path taking an empty arr 
    visited = [False] * (N + 1)

    dfs_path = []

    # Starting DFS from city 1
    dfs_helper(graph, 1, visited, dfs_path)

    return dfs_path #retuting


def read_input(file_path):
    with open(file_path, "r") as file:
        N, M = map(int, file.readline().split())

        edges = []
        for _ in range(M):
            u, v = map(int, file.readline().split())
            edges.append((u, v))

    return N, edges


def write_output(output_file, dfs_path):
    with open(output_file, "w") as file:
        file.write(" ".join(map(str, dfs_path)))

 
N, edges = read_input(input_file_path)

graph = initialize_graph(N)
for edge in edges:
    add_edge(graph, *edge)

dfs_path = dfs(graph, N)

write_output(output_file_path, dfs_path)
