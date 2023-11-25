# as shown in theory classes 

import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = [-1] * n        # to get desired outputs we use -1 instead infiniy. 
    parents = [-1] * n
    colors = ['white'] * n
    
    distances[start - 1] = 0
    heap = [(0, start)]
    
    while heap:
        dist, cur_node = heapq.heappop(heap)
        
        if colors[cur_node - 1] == 'black':
            continue
        
        for u, weight in graph[cur_node]:
            if colors[u - 1] == 'white':
                new_dist = dist + weight
                if new_dist < distances[u - 1] or distances[u - 1] == -1:
                    distances[u - 1] = new_dist
                    parents[u - 1] = cur_node
                    heapq.heappush(heap, (distances[u - 1], u))
        
        colors[cur_node - 1] = 'black'
    
    return distances, parents

def gimme_output_at_once(input_file_path, output_file_path):
    with open(input_file_path, 'r') as f:
        N, M = map(int, f.readline().split())
        graph = [[] for _ in range(N + 1)]
        for i in range(M):
            u, v, w = map(int, f.readline().split())
            graph[u].append((v, w))
        source = int(f.readline())

    distances, parents = dijkstra(graph, source)
    
    with open(output_file_path, 'w') as f:
        f.write(" ".join(str(dist) if dist != -1 else "-1" for dist in distances[0:-1]))

input_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB06\\task01_input01.txt"
output_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB06\\task01_output01.txt"

input_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB06\\task01_input02.txt"
output_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB06\\task01_output02.txt"

gimme_output_at_once(input_file_path01, output_file_path01)
gimme_output_at_once(input_file_path02, output_file_path02)
