board = [" "] * 9

def display():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

def check_win(p):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for w in wins:
        if all(board[i] == p for i in w):
            return True
    return False

player = "X"

for turn in range(9):
    display()
    pos = int(input(f"Player {player}, enter position (1-9): ")) - 1

    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid move!")
        continue

    board[pos] = player

    if check_win(player):
        display()
        print(player, "Wins!")
        break

    player = "O" if player == "X" else "X"

else:
    display()
    print("Draw!")