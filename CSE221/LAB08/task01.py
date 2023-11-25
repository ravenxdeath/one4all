import heapq

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False

        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            self.rank[y] += 1

        return True

def min_maintain(N, roads):
    graph = [[] for i in range(N)]        # adj ls 
    for u, v, cost in roads:
        graph[u - 1].append((v - 1, cost))
        graph[v - 1].append((u - 1, cost))

    visited = [False] * N
    pq = [(0, 0)]            # Priority queue to store (cost, node) pairs --> st, node 
    total_cost = 0

    while pq:                # iterating till there's no nodes
        cost, node = heapq.heappop(pq)
        if visited[node]:
            continue

        visited[node] = True
        total_cost += cost

        for neighbor, edge_cost in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(pq, (edge_cost, neighbor))

    return total_cost

def gimmeMyoutput():
    input_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB08\\task01_input01.txt"
    output_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB08\\task01_output01.txt"

    with open(input_file_path, "r") as f01:
        N, M = map(int, f01.readline().split())
        roads = [tuple(map(int, f01.readline().split())) for i in range(M)]

    result = min_maintain(N, roads)

    with open(output_file_path, "w") as f02:
        f02.write(str(result) + "\n")

    print(output_file_path)


gimmeMyoutput()
