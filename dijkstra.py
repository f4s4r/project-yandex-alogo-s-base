INF = float("inf") # по сути бесконечность
costs = {}
graph = {}
parents = {}

def find_min_cost(visited):
    global costs
    min_cost = INF
    min_node = None
    for node in costs:
        if node not in visited:
            cur_value = costs[node]
            if cur_value < min_cost:
                min_cost = cur_value
                min_node = node
    # print(min_node)
    return min_node


def update_costs_neighbours(node):
    global graph
    global costs
    for neighbour_node in graph[node]:
        if costs[neighbour_node] > graph[node][neighbour_node] + costs[node]:
            costs[neighbour_node] = graph[node][neighbour_node] + costs[node]
            parents[neighbour_node] = node

def dijkstra(start, finish):
    global graph
    global costs
    global parents
    visited = {}
    costs[start] = 0
    while len(visited) < len(graph):
        min_node = find_min_cost(visited)
        update_costs_neighbours(min_node)
        visited[min_node] = True
    print(costs)

graph["start"] = {}
graph["start"]["A"] = 6
graph["start"]["B"] = 2

graph["B"] = {}
graph["B"]["A"] = 3

graph["B"]["end"] = 5

graph["A"] = {}
graph["A"]["end"] = 1

graph["end"] = {}

costs['A'] = 6
costs['B'] = 2
costs['end'] = INF

parents['A'] = "start"
parents['B'] = "start"
parents['end'] = None


print(dijkstra('start', 'end'))