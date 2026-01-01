board = [' ' for _ in range(9)]

def print_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

def check_winner(player):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def play():
    current = 'X'
    for _ in range(9):
        print_board()
        move = int(input(f"Player {current}, enter position (1-9): ")) - 1
        if board[move] == ' ':
            board[move] = current
            if check_winner(current):
                print_board()
                print(f"Player {current} wins!")
                return
            current = 'O' if current == 'X' else 'X'
        else:
            print("Invalid move")
    print("Draw!")

play()
