from collections import OrderedDict

def kosaraju_scc(graph):
    def dfs(node, stack):
        visited[node] = True
        if node in graph:
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, stack)
        stack.append(node)

    def reverse_graph():
        reversed_graph = {v: [] for v in graph.keys()}
        for u in graph:
            for v in graph[u]:
                reversed_graph[v].append(u)
        return reversed_graph

    def dfs_reverse(node, scc):
        visited[node] = True
        scc.append(node)
        for neighbor in reversed_graph[node]:
            if not visited[neighbor]:
                dfs_reverse(neighbor, scc)

    num_vertices = max(graph.keys())
    visited = [False] * (num_vertices + 1)
    stack = []

    for node in graph:
        if not visited[node]:
            dfs(node, stack)

    reversed_graph = reverse_graph()
    visited = [False] * (num_vertices + 1)
    sccs = []

    while stack:
        node = stack.pop()
        if not visited[node]:
            scc = []
            dfs_reverse(node, scc)
            sccs.append(scc)

    return sccs


def read_input(file_path):
    graph = {}
    vertices = set()  # Use a set to track vertices to preserve insertion order
    with open(file_path, 'r') as file:
        n, m = map(int, file.readline().split())
        for _ in range(m):
            u, v = map(int, file.readline().split())
            vertices.add(u)  # Track vertices in set
            vertices.add(v)
            if u not in graph:
                graph[u] = []
            graph[u].append(v)
            if v not in graph:
                graph[v] = []  # Handle isolated vertices
    # Convert vertices set to list in the order they were encountered
    graph = {v: graph[v] for v in sorted(vertices)}
    return graph


def write_output(file_path, sccs):
    with open(file_path, 'w') as file:
        for scc in sccs:
            file.write(' '.join(map(str, scc)) + '\n')


def gimme_output_at_once(input_file_path, output_file_path):
    graph = read_input(input_file_path)
    sccs = kosaraju_scc(graph)
    write_output(output_file_path, sccs)


input_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task03_input01.txt"
output_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task03_output01.txt"

input_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task03_input02.txt"
output_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task03_output02.txt"

input_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task03_input03.txt"
output_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB05\\task03_output03.txt"

gimme_output_at_once(input_file_path01, output_file_path01)

gimme_output_at_once(input_file_path02, output_file_path02)

gimme_output_at_once(input_file_path03, output_file_path03)

