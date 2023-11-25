def readingInput(file_path):
    with open(file_path, 'r') as f01:
        N, M = map(int, f01.readline().split())
        reqs = [tuple(map(int, f01.readline().split())) for i in range(M)]
    return N, reqs

def adj_Ls(N, reqs):
    # ls = []
    adjaList = [[] for i in range(N + 1)]
    for A, B in reqs:
        adjaList[A].append(B)
    return adjaList

def topoSort(adjaList):
    inDegreee = [0] * len(adjaList)
    for n in adjaList:
        for neighbor in n:
            inDegreee[neighbor] += 1

    queue = []
    for i in range(1, len(adjaList)):
        if inDegreee[i] == 0:
            queue.append(i)

    order = []
    while queue:
        node = queue.pop(0)
        order.append(node)

        for neighbor in adjaList[node]:
            inDegreee[neighbor] -= 1
            if inDegreee[neighbor] == 0:
                queue.append(neighbor)

    if len(order) == len(adjaList) - 1:  # except the destination
        return order
    else:
        return None   # no routes

def writingOutput(file_path, adjaList, route):
    with open(file_path, 'w') as f:
        f.write("Adjacency List:\n")
        for node, n in enumerate(adjaList[1:], start=1):
            f.write(f"{node} : {' '.join(map(str, n))}\n")
        
        if route is None:
            f.write("Before adding rule:\nCannot make route\n")
            f.write("After adding rule:\nCannot make route\n")
        else:
            f.write("Before adding rule:\n" + ' '.join(map(str, route)) + '\n')
            adjustRoute = route.copy()
            destination = adjustRoute.pop()
            adjustRoute.insert(-1, destination)  # Inserted destination before the last elem
            
            f.write("After adding rule:\n" + ' '.join(map(str, adjustRoute)) + '\n')

def gimme_output_at_once(input_file_path, output_file_path):
    N, reqs = readingInput(input_file_path)
    adjaList = adj_Ls(N, reqs)
    route = topoSort(adjaList)
    writingOutput(output_file_path, adjaList, route) 

input_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB_FINAL\\setB_input01.txt"
output_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB_FINAL\\setB_output01.txt"


input_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB_FINAL\\setB_input02.txt"
output_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB_FINAL\\setB_output02.txt"

gimme_output_at_once(input_file_path01, output_file_path01)
gimme_output_at_once(input_file_path02, output_file_path02)