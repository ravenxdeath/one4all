def readingInput(file_path):
    with open(file_path, 'r') as f01:
        N, M = map(int, f01.readline().split())  # Read N and M from the first line
        reqs = [tuple(map(int, f01.readline().split())) for i in range(M)]  # Read M pairs of integers as reqs
    return N, reqs

def adj_Ls(N, reqs):
    adjaList = [[] for i in range(N + 1)]  # Initialize an adjacency list with empty lists for each node
    for A, B in reqs:
        adjaList[A].append(B)  # Create adjacency list by adding B as a neighbor of node A
    return adjaList

def topoSort(adjaList):
    inDegreee = [0] * len(adjaList)  # Initialize in-degree array for each node

    # Calculate in-degrees for each node by traversing the adjacency list
    for n in adjaList:
        for neighbor in n:
            inDegreee[neighbor] += 1

    queue = []
    for i in range(1, len(adjaList)):
        if inDegreee[i] == 0:
            queue.append(i)  # Add nodes with in-degree 0 to the queue

    order = []
    while queue:
        node = queue.pop(0)  # Get a node with in-degree 0
        order.append(node)  # Add it to the sorted order

        for neighbor in adjaList[node]:
            inDegreee[neighbor] -= 1  # Decrease in-degree of neighbors
            if inDegreee[neighbor] == 0:
                queue.append(neighbor)  # Add neighbors with in-degree 0 to the queue

    if len(order) == len(adjaList) - 1:  # Check if all nodes are visited except the destination
        return order
    else:
        return None  # If there's a cycle, return None indicating no valid route

def write_output(file_path, adjaList, route):
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
    write_output(output_file_path, adjaList, route) 

# Paths for input and output files
input_file_path01 = "path_to_input_file01.txt"
output_file_path01 = "path_to_output_file01.txt"

input_file_path02 = "path_to_input_file02.txt"
output_file_path02 = "path_to_output_file02.txt"

# Generate outputs for both sets of input and output files
gimme_output_at_once(input_file_path01, output_file_path01)
gimme_output_at_once(input_file_path02, output_file_path02)
