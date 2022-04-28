# Mmusi Hubona
# Tic-Tac-Toe
# Week:02

# Included a menu and added three difficulty levels

def main():
    print()
    menu()
    selection = int(input("Please make a selection(1-4): "))

    while selection != 4:
        if selection == 1:
            player = next_player("")
            board = create_board()
            while not (winner(board) or game_draw(board)):
                display_board(board)
                make_move(player, board)
                player = next_player(player)
            display_board(board)
            print("Good game. Thanks for playing!") 

        elif selection == 2:
            player = next_player("")
            board = create_board_four_by_four()
            while not (winner2(board) or game_draw2(board)):
                display_board_four_by_four(board)
                make_move(player, board)
                player = next_player(player)
            display_board_four_by_four(board)
            print("Good game. Thanks for playing!")

        elif selection == 3:
            player = next_player("")
            board = create_board_five_by_five()
            while not (winner3(board) or game_draw3(board)):
                display_board_five_by_five(board)
                make_move(player, board)
                player = next_player(player)
            display_board_five_by_five(board)
            print("Good game. Thanks for playing!")

        else:
            print("Invalid selection.")

        menu()
        selection = int(input("Please make a selection(1-4): "))
    print("Goodbye.")

def menu():
        print("""
Tic tac toe: Please select difficulty level or Exit(1-4)
01.| Normal mode(3x3 grid)
02.| Medium (4x4 grid)
03.| Hard (5x5 grid)
04.| Exit

""")


def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def create_board_four_by_four():
    board = []
    for square in range(16):
        board.append(square + 1)
    return board
    
def create_board_five_by_five():
    board = []
    for square in range(25):
        board.append(square + 1)
    return board

def display_board(board):
    print(f"""
    {board[0]}|{board[1]}|{board[2]}
    -+-+-
    {board[3]}|{board[4]}|{board[5]}
    -+-+-
    {board[6]}|{board[7]}|{board[8]}
    
    """)
def display_board_four_by_four(board):
    print(f"""
    {board[0]} |{board[1]} |{board[2]} | {board[3]}
    -+-+-+-+-+-
    {board[4]} |{board[5]} |{board[6]} | {board[7]}
    -+-+-+-+-+-
    {board[8]} |{board[9]}|{board[10]}|{board[11]}
    -+-+-+-+-+-
    {board[12]}|{board[13]}|{board[14]}|{board[15]}
    
    """)    
def display_board_five_by_five(board):
    print(f"""
    {board[0]} |{board[1]} |{board[2]} |{board[3]} |{board[4]}
    -+-+-+-+-+-+-+
    {board[5]} |{board[6]} |{board[7]} |{board[8]} |{board[9]}
    -+-+-+-+-+-+-+
    {board[10]}|{board[11]}|{board[12]}|{board[13]}|{board[14]}
    -+-+-+-+-+-+-+
    {board[15]}|{board[16]}|{board[17]}|{board[18]}|{board[19]}
    -+-+-+-+-+-+-+
    {board[20]}|{board[21]}|{board[22]}|{board[23]}|{board[24]}
    
    """)     

def game_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True

def game_draw2(board):
    for square in range(16):
        if board[square] != "x" and board[square] != "o":
            return False
    return True

def game_draw3(board):
    for square in range(25):
        if board[square] != "x" and board[square] != "o":
            return False
    return True

def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def winner2(board):
    return (board[0] == board[1] == board[2] == board[3] or
            board[4] == board[5] == board[6] == board[7] or
            board[8] == board[9] == board[10] == board[11] or
            board[12] == board[13] == board[14] == board[15] or
            board[0] == board[4] == board[8] == board[12] or
            board[1] == board[5] == board[9] == board[13] or
            board[2] == board[6] == board[10] == board[14] or
            board[3] == board[7] == board[11] == board[15] or
            board[0] == board[5] == board[10] == board[15] or
            board[3] == board[6] == board[9] == board[12])

def winner3(board):
    return (board[0] == board[1] == board[2] == board[3]== board[4] or
            board[5] == board[6] == board[7] == board[8] == board[9] or
            board[10] == board[11] == board[12] == board[13] == board[14] or
            board[15] == board[16] == board[17] == board[18] == board[19] or
            board[20] == board[21] == board[22] == board[23] == board[24] or
            board[0] == board[5] == board[10] == board[15] == board[20] or
            board[1] == board[6] == board[11] == board[16] == board[21] or
            board[2] == board[7] == board[12] == board[17] == board[22] or
            board[3] == board[8] == board[13] == board[18] == board[23] or
            board[4] == board[9] == board[14] == board[19] == board[24] or
            board[0] == board[6] == board[12] == board[18] == board[24] or
            board[4] == board[8] == board[12] == board[16] == board[20])

def make_move(player, board):
    square =int(input(f"{player}'s turn to choose a square on current board e.g (1-9) or (1-16) or (1-25): "))
    board[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()