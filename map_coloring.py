colors = ['Red', 'Green', 'Blue']
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}
def is_valid(state, region, color):
    for neighbor in neighbors[region]:
        if neighbor in state and state[neighbor] == color:
            return False
    return True
def backtrack(state):
    if len(state) == len(neighbors):
        return state
    unassigned = [r for r in neighbors if r not in state]
    region = unassigned[0]
    for color in colors:
        if is_valid(state, region, color):
            state[region] = color
            result = backtrack(state)
            if result:
                return result
            del state[region] 
if __name__ == "__main__":
    solution = backtrack({})
    if solution:
        print("Map Coloring Solution:")
        for region in sorted(solution):
            print(f"{region}: {solution[region]}")
    else:
        print("No solution found.")
