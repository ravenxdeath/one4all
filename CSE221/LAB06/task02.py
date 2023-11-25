from queue import PriorityQueue

def dijkstra(graph, start, n):
    inf = float("inf")
    q = PriorityQueue()

    dist = [inf] * (n + 1)
    visited = [False for _ in range(n + 1)]

    dist[start] = 0
    q.put((0, start))

    while not q.empty():
        node = q.get()

        visited[node[1]] = True

        if node[0] < dist[node[1]]:
            dist[node[1]] = node[0]

        for i in graph[node[1]]:
            w = node[0] + i[0]
            if not visited[i[1]]:
                q.put((w, i[1]))

    return dist

 
# input_file_path1 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB06\\task02_input01.txt"
# output_file_path1 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB06\\task02_output01.txt"

# input_file_path3 = "C:/CODE/TahmidRaven/UNI/CSE221venv/LAB06/task02_input02.txt"
# output_file_path3 = "C:/CODE/TahmidRaven/UNI/CSE221venv/LAB06/task02_output02.txt"

input_file_path3 = "C:/CODE/TahmidRaven/UNI/CSE221venv/LAB06/task02_input03.txt"
output_file_path3 = "C:/CODE/TahmidRaven/UNI/CSE221venv/LAB06/task02_output03.txt"

with open(input_file_path3, "r") as f01:
    n, m = map(int, f01.readline().split())
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v, w = map(int, f01.readline().split())
        graph[u].append((w, v))
    start1, start2 = map(int, f01.readline().split())

    list1 = dijkstra(graph, start1, n)
    list2 = dijkstra(graph, start2, n)

    new = []
    for i in range(len(list1)):
        new.append(max(list1[i], list2[i]))

    a = min(new)

    meeting_nodes = []
    for i in range(len(new)):
        if new[i] == a:
            meeting_nodes.append(i)
    
    with open(output_file_path3, "w") as f02:
        if a == float("inf"):
            f02.write("Impossible\n")
        else:
            f02.write(f"Time: {a}\n")
            f02.write("Node:")
            for node in meeting_nodes:
                f02.write(f" {node}\n")


 