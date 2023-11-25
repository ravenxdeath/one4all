# import heapq

# def dijkstra(graph, start):
#     n = len(graph)
#     dista = [-1] * n
#     dista[start - 1] = 0
#     heap = [(0, start)]
    
#     while heap:
#         dist, node = heapq.heappop(heap)
        
#         if dist > dista[node - 1]:
#             continue
        
#         for neighbor, weight in graph[node]:
#             new_dist = dist + weight
#             if dista[neighbor - 1] == -1 or new_dist < dista[neighbor - 1]:
#                 dista[neighbor - 1] = new_dist
#                 heapq.heappush(heap, (new_dist, neighbor))
    
#     return dista

# def gimme_output_at_once(input_file_path, output_file_path):
#     with open(input_file_path, 'r') as f:
#         N, M = map(int, f.readline().split())
#         graph = [[] for _ in range(N + 1)]
#         for i in range(M):
#             u, v, w = map(int, f.readline().split())
#             graph[u].append((v, w))
#         source = int(f.readline())
 
#     dista = dijkstra(graph, source)
    
#     with open(output_file_path, 'w') as f:
#         f.write(" ".join(str(dist) for dist in dista[0:-1]))