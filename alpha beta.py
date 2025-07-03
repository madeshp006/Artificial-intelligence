import math
def alphabeta(node, depth, alpha, beta, is_max, values, tree):
    if depth == 0 or node not in tree:
        return values[node]
    if is_max:
        max_eval = -math.inf
        for child in tree[node]:
            eval = alphabeta(child, depth-1, alpha, beta, False, values, tree)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for child in tree[node]:
            eval = alphabeta(child, depth-1, alpha, beta, True, values, tree)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}
values = {
    'D': 3,
    'E': 5,
    'F': 6,
    'G': 9
}
if __name__ == "__main__":
    result = alphabeta('A', 3, -math.inf, math.inf, True, values, tree)
    print("Optimal value:", result)
