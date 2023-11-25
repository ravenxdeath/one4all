class DisjoinedSetSolver:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]       # parent of each element 
        self.size = [1] * (n + 1)                     # size of each friend circle

    def find(self, x):                                #finds the rood of a circle
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            
        return self.parent[x]

    def union(self, x, y):        #merges two friend circles
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            
            if self.size[rootX] < self.size[rootY]:
                rootX, rootY = rootY, rootX
                
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]

def gimme_output_at_once(input_file_path, output_file_path):
    with open(input_file_path, 'r') as f01, open(output_file_path, 'w') as f02:
        
        n, k = map(int, f01.readline().split())
        
        dis = DisjoinedSetSolver(n)
        
        for i in range(k):
            a, b = map(int, f01.readline().split())
            dis.union(a, b)
            f02.write(str(dis.size[dis.find(a)]) + '\n')

input_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB07\\task03_input01.txt"
output_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB07\\task03_output01.txt"
input_file_path1 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB07\\task03_input02.txt"
output_file_path1 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB07\\task03_output02.txt"
gimme_output_at_once(input_file_path, output_file_path)
gimme_output_at_once(input_file_path1, output_file_path1)

