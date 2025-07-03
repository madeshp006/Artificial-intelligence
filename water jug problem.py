def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = []
    queue = []
    queue.append((0, 0, []))
    while len(queue) > 0:
        jug1, jug2, path = queue[0]
        queue = queue[1:]
        if [jug1, jug2] in visited:
            continue
        visited.append([jug1, jug2])
        current_path = path + [f"({jug1},{jug2})"]
        if jug1 == target or jug2 == target:
            print("Solution steps:")
            for step in current_path:
                print(step)
            if jug1 == target and jug2 != 0:
                print(f"({jug1},0)")
            elif jug2 == target and jug1 != 0:
                print(f"(0,{jug2})")
            return
        next_states = [
            [jug1_capacity, jug2],
            [jug1, jug2_capacity],
            [0, jug2],
            [jug1, 0],
            [jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)],
            [jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1)]
        ]
        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], current_path))
    print("No solution found.")
if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target = 2
    water_jug_bfs(jug1_capacity, jug2_capacity, target)
