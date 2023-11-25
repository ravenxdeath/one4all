input_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task04_input01.txt"
output_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task04_output01.txt"

input_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task04_input02.txt"
output_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task04_output02.txt"

input_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task04_input03.txt"
output_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task04_output03.txt"

input_file_path04 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task04_input04.txt"
output_file_path04 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task04_output04.txt"

input_file_path05 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task04_input05.txt"
output_file_path05 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task04_output05.txt"

def FindMyCycle(graph, v, visited, stack):
    visited[v] = True
    stack[v] = True

    for myNeighbor in graph[v]:
        if not visited[myNeighbor]:
            if FindMyCycle(graph, myNeighbor, visited, stack):
                return True
        elif stack[myNeighbor]:
            return True

    stack[v] = False
    return False


def is_cyclic(graph, n):
    visited = [False] * (n + 1)
    stack = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            if FindMyCycle(graph, i, visited, stack):
                return True

    return False


def GimmeOutputAtOnce(input_file_path, output_file_path):
    with open(input_file_path, "r") as input_file:
        n, m = map(int, input_file.readline().split())
        graph = {i: [] for i in range(1, n + 1)}

        for _ in range(m):
            u, v = map(int, input_file.readline().split())
            graph[u].append(v)

    has_cycle = is_cyclic(graph, n)

    with open(output_file_path, "w") as output_file:
        output_file.write("YES\n" if has_cycle else "NO\n")


# GimmeOutputAtOnce(input_file_path01,output_file_path01)
# GimmeOutputAtOnce(input_file_path02,output_file_path02)
# GimmeOutputAtOnce(input_file_path03,output_file_path03)
# GimmeOutputAtOnce(input_file_path04,output_file_path04)
GimmeOutputAtOnce(input_file_path05,output_file_path05)
