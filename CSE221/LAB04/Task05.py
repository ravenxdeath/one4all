input_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task05_input01.txt"
output_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task05_output01.txt"

input_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task05_input02.txt"
output_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task05_output02.txt"

input_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task05_input03.txt"
output_file_path03 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task05_output03.txt"

input_file_path04 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task05_input04.txt"
output_file_path04 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task05_output04.txt"

input_file_path05 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task05_input05.txt"
output_file_path05 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task05_output05.txt"


from collections import defaultdict, deque

def shortest_path(N, M, D, roads):
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (N + 1)
    time2reach = [float('inf')] * (N + 1)
    path2City = [0] * (N + 1)

    queue = deque()
    queue.append(1)
    visited[1] = True
    time2reach[1] = 0

    while queue:
        current_city = queue.popleft()

        for neighbor in graph[current_city]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                time2reach[neighbor] = time2reach[current_city] + 1
                path2City[neighbor] = current_city

    mini_time_2_Des = time2reach[D]
    shortest_path_list = [D]
    city = D
    while city != 1:
        city = path2City[city]
        shortest_path_list.append(city)
    shortest_path_list.reverse()

    return mini_time_2_Des, shortest_path_list

def GimmeOutputAtOnce(input_file_path, output_file_path):
    with open(input_file_path, 'r') as f:
        N, M, D = map(int, f.readline().split())
        roads = [tuple(map(int, line.split())) for line in f]

    min_time_to_D, shortest_path_list = shortest_path(N, M, D, roads)

    output_str = f"Time: {min_time_to_D}\nShortest Path: {' '.join(map(str, shortest_path_list))}\n"

    with open(output_file_path, 'w') as f:
        f.write(output_str)


GimmeOutputAtOnce(input_file_path01,output_file_path01)
GimmeOutputAtOnce(input_file_path02,output_file_path02)
GimmeOutputAtOnce(input_file_path03,output_file_path03)
GimmeOutputAtOnce(input_file_path04,output_file_path04)
GimmeOutputAtOnce(input_file_path05,output_file_path05)
