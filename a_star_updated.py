graph = {
    'A': ({'B': 3, 'C': 1}, 3),  # {'B': 3, 'C': 1} are the neighbors with the costs, 3 is the heuristic value for A
    'B': ({'A': 3, 'D': 2, 'E': 4}, 2),
    'C': ({'A': 1, 'F': 5}, 1),
    'D': ({'B': 2}, 6),
    'E': ({'B': 4, 'F': 1}, 1),
    'F': ({'C': 5, 'E': 1}, 0)
}

def get_min(q):
    # Find the node with the minimum f(n) = h(n) + g(n)
    mn = (None, float("inf"))
    for i in q:
        # Sum of heuristic (h(n)) + path cost (g(n))
        total_cost = q[i][0] + q[i][1]
        if total_cost < mn[1]:
            mn = (i, total_cost)
    return mn[0]

def a_star(graph, prev, dst, path, pcost, q):
    print("Connected nodes of current node", prev, "with h(n) values: ")

    # Get the neighbors and costs from the graph
    neighbors, heuristic = graph[prev]

    for n in neighbors:  # neighbors with their costs
        if n not in path:
            cost = neighbors[n]  # cost to travel to neighbor n
            # Store (heuristic, path cost) for each neighbor
            q[n] = (graph[n][1], cost)
            print(f"{n} -> (h(n): {q[n][0]}, g(n): {q[n][1]})")
            
            # Path cost for the neighbor
            path_cost = pcost + q[n][1]
            print(f"A* value for {n} is: {path_cost}")
    
    while q:
        # Get the node with the minimum f(n) = h(n) + g(n)
        mn = get_min(q)
        print(f"Selecting Minimum vertex: {mn}")
        print("__________________________________________________")
        
        if dst == mn:
            return path + [dst]
        
        # Update path cost with the selected node's path cost (g(n))
        pc = pcost + q[mn][1]
        print(f"Previous path cost: {pc}")
        
        # Remove the node with the minimum f(n) from the queue
        del q[mn]
        
        # Recursive call to explore the next node
        new_path = a_star(graph, mn, dst, path + [mn], pc, q)
        if new_path:
            return new_path
    
    return []

# Input section
source = input("Enter Source vertex: ")
dest = input("Enter destination vertex: ")
heuristic = int(input("Enter given heuristic value for source: "))

# Starting the A* search algorithm
path = a_star(graph, source, dest, [], 0, {source: (heuristic, 0)})

if path:
    print("Path found:", path)
else:
    print("Path not found")
