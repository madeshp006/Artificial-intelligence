import itertools
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = [0, 1, 2, 3]  

def total_distance(path):
    distance = 0
    for i in range(len(path) - 1):
        distance += distances[path[i]][path[i+1]]
    distance += distances[path[-1]][path[0]] 
    return distance

def tsp():
    min_path = None
    min_cost = float('inf')

    for perm in itertools.permutations(cities):
        cost = total_distance(perm)
        if cost < min_cost:
            min_cost = cost
            min_path = perm

    print("Minimum path (by city index):", min_path)
    print("Minimum cost:", min_cost)

    city_names = ['A', 'B', 'C', 'D']
    named_path = [city_names[i] for i in min_path]
    print("Minimum path (named):", " -> ".join(named_path + [named_path[0]]))
if __name__ == "__main__":
    tsp()
