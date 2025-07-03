graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    print(start, end=' ')
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

if __name__ == "__main__":
    print("DFS Traversal:")
    dfs(graph, 'A')
