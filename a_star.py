import heapq
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 3, 'E': 1, 'G': 2},
    'G': {}
}
heuristics = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 6,
    'E': 2,
    'F': 1,
    'G': 0
}
def a_star_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristics[start], 0, start, [start]))
    closed_set = set()
    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        if current == goal:
            print("Shortest path found:", " -> ".join(path))
            print("Total cost:", g)
            return
        closed_set.add(current)
        for neighbor, cost in graph[current].items():
            if neighbor not in closed_set:
                new_g = g + cost
                new_f = new_g + heuristics[neighbor]
                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    print("No path found.")
if __name__ == "__main__":
    a_star_search('A', 'G')
