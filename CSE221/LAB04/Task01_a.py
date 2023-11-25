
def create_adjacency_matrix(N, M, edges):
    # Initializing an (N + 1) x (N + 1) matrix with all values set to 0
    # was using it it handle the vertix zero however now it's being handled by th func call
    
    adjacency_matrix = [[0 for i in range(N)] for i in range(N)]

    # Filling the matrix with the given edges and their weights
    for edge in edges:
        u, v, w = edge
        adjacency_matrix[u][v] = w

    return adjacency_matrix


def print_adjacency_matrix(adjacency_matrix, output_file):
    # Write the adjacency matrix to the output file
    with open(output_file, "w") as file:
        for row in adjacency_matrix:
            file.write(" ".join(map(str, row)) + "\n")


def read_input(file_path):
    with open(file_path, "r") as file:
        N, M = map(int, file.readline().split())

        edges = []
        for _ in range(M):
            u, v, w = map(int, file.readline().split())
            edges.append((u, v, w))

    return N, M, edges



# input_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\task01_a_input01.txt"
# output_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\task01_a_output01.txt"
input_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\task01_a_input02.txt"
output_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\task01_a_output02.txt"


N, M, edges = read_input(input_file_path)

# Creating the adjacency matrix with an additional vertex (N+1) associated with a weight of 0
adjacency_matrix = create_adjacency_matrix(N + 1, M, edges)

print_adjacency_matrix(adjacency_matrix, output_file_path)
