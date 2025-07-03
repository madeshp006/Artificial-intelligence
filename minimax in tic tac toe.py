def print_board(b):
    for row in b:
        print(" | ".join(row))
        print("-" * 5)

def is_win(b, p):
    for i in range(3):
        if all(b[i][j]==p for j in range(3)) or all(b[j][i]==p for j in range(3)):
            return True
    return all(b[i][i]==p for i in range(3)) or all(b[i][2-i]==p for i in range(3))

def is_full(b):
    return all(cell != " " for row in b for cell in row)

def minimax(b, is_ai):
    if is_win(b, 'O'): return 1
    if is_win(b, 'X'): return -1
    if is_full(b): return 0

    best = -100 if is_ai else 100
    for i in range(3):
        for j in range(3):
            if b[i][j] == " ":
                b[i][j] = 'O' if is_ai else 'X'
                score = minimax(b, not is_ai)
                b[i][j] = " "
                best = max(best, score) if is_ai else min(best, score)
    return best

def best_move(b):
    best_score = -100
    move = None
    for i in range(3):
        for j in range(3):
            if b[i][j] == " ":
                b[i][j] = 'O'
                score = minimax(b, False)
                b[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play():
    board = [[" "]*3 for _ in range(3)]
    print("Tic Tac Toe: You (X) vs AI (O)")
    while True:
        print_board(board)
        try:
            r, c = map(int, input("Enter row and column (0-2): ").split())
        except: continue
        if board[r][c] != " ": print("Occupied!"); continue
        board[r][c] = 'X'
        if is_win(board, 'X'): print_board(board); print("You win!"); break
        if is_full(board): print_board(board); print("Draw!"); break
        ai_r, ai_c = best_move(board)
        board[ai_r][ai_c] = 'O'
        if is_win(board, 'O'): print_board(board); print("AI wins!"); break
        if is_full(board): print_board(board); print("Draw!"); break

play()
