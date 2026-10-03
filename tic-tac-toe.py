board = [" "] * 9

def display():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])


def winner(b):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for w in wins:
        if b[w[0]] == b[w[1]] == b[w[2]] != " ":
            return b[w[0]]

    return None


def minimax(b, is_max):
    if winner(b) == "O":
        return 1
    if winner(b) == "X":
        return -1
    if " " not in b:
        return 0

    if is_max:
        best = -100

        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, False)
                b[i] = " "
                best = max(best, score)

        return best

    else:
        best = 100

        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, True)
                b[i] = " "
                best = min(best, score)

        return best


def computer_move():
    best = -100
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best:
                best = score
                move = i

    board[move] = "O"


print("You are X, Computer is O")

while True:
    display()

    pos = int(input("Enter position (1-9): ")) - 1

    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid move!")
        continue

    board[pos] = "X"

    if winner(board) == "X":
        display()
        print("You Win!")
        break

    if " " not in board:
        display()
        print("Draw!")
        break

    computer_move()

    if winner(board) == "O":
        display()
        print("Computer Wins!")
        break

    if " " not in board:
        display()
        print("Draw!")
        break
