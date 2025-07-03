goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def manhattan(puzzle):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = puzzle[i][j]
            if val != 0:
                x, y = divmod(val - 1, 3)
                dist += abs(x - i) + abs(y - j)
    return dist
def find_blank(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j
def puzzle_to_tuple(puzzle):
    return tuple(tuple(row) for row in puzzle)
def insert_with_priority(queue, item):
    index = 0
    while index < len(queue) and queue[index][0] <= item[0]:
        index += 1
    queue.insert(index, item)
def A_star(start):
    visited = []
    queue = []
    insert_with_priority(queue, (manhattan(start), 0, start, []))
    while len(queue) > 0:
        est_cost, cost, puzzle, path = queue[0]
        queue = queue[1:]
k-p553
if puzzle == goal_state:
            return path + [puzzle]
        visited.append(puzzle_to_tuple(puzzle))
        x, y = find_blank(puzzle)
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_puzzle = [row[:] for row in puzzle]
                new_puzzle[x][y], new_puzzle[nx][ny] = new_puzzle[nx][ny], new_puzzle[x][y]
                t_puzzle = puzzle_to_tuple(new_puzzle)
                if t_puzzle not in visited:
                    new_cost = cost + 1
                    est_total = new_cost + manhattan(new_puzzle)
                    insert_with_priority(queue, (est_total, new_cost, new_puzzle, path + [puzzle]))
start_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
solution = A_star(start_state)
for step in solution:
    for row in step:
        print(row)
    print("-----")
 
