import heapq

def finding_min_danger_path(N, edges):
    graph = [[] for i in range(N + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    min_danger = [float('inf')] * (N + 1)
    min_danger[1] = 0
    
    heap = [(0, 1)]
    
    while heap:
        danger, node = heapq.heappop(heap)
        
        if danger > min_danger[node]:
            continue
        
        for neighbor, edge_danger in graph[node]:
            new_danger = max(danger, edge_danger)
            
            if new_danger < min_danger[neighbor]:
                min_danger[neighbor] = new_danger
                heapq.heappush(heap, (new_danger, neighbor))
    
    return min_danger[N]
 
def gimme_output_at_once(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        N, M = map(int, input_file.readline().split())
        edges = []
        for i in range(M):
            u, v, w = map(int, input_file.readline().split())
            edges.append((u, v, w))
    
    result = finding_min_danger_path(N, edges)
    
    with open(output_file_path, 'w') as output_file:
        if result == float('inf'):
            output_file.write("Impossible\n")
        else:
            output_file.write(str(result) + "\n")
 
input_file_path01 = "TahmidRaven/UNI/CSE221venv/LAB06/task03_input01.txt"   
output_file_path01 = "TahmidRaven/UNI/CSE221venv/LAB06/task03_output01.txt"  

input_file_path02 = "TahmidRaven/UNI/CSE221venv/LAB06/task03_input02.txt"   
output_file_path02 = "TahmidRaven/UNI/CSE221venv/LAB06/task03_output02.txt"  
 
gimme_output_at_once(input_file_path01, output_file_path01)
gimme_output_at_once(input_file_path02, output_file_path02)
