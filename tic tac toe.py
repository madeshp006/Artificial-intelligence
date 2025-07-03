board = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]
def show_board():
    for i in range(3):
        print(board[i][0] + " | " + board[i][1] + " | " + board[i][2])
        if i < 2:
            print("--+---+--")
def check_win(p):
    for i in range(3):
        if board[i][0] == p and board[i][1] == p and board[i][2] == p:
            return True
        if board[0][i] == p and board[1][i] == p and board[2][i] == p:
            return True
    if board[0][0] == p and board[1][1] == p and board[2][2] == p:
        return True
    if board[0][2] == p and board[1][1] == p and board[2][0] == p:
        return True
    return False
def play():
    turn = 0
    while turn < 9:
        show_board()
        if turn % 2 == 0:
            player = "X"
        else:
            player = "O"
        move = input("Player " + player + ", enter (1-9): ")
        for i in range(3):
            for j in range(3):
                if board[i][j] == move:
                    board[i][j] = player
                    turn += 1
                    if check_win(player):
                        show_board()
                        print("Player " + player + " wins!")
                        return
        else:
            continue
    show_board()
    print("It's a draw!")

play()
