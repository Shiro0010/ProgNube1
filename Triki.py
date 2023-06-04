# Define una función que dibuje el tablero
def draw_board(board):
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print("_________________")
 
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print("_________________")
 
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print("     |     |")
 
# Define una función que verifique si alguien ha ganado
def check_win(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False
 
# Define la función principal del juego
def play_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player = "X"
    game_over = False
 
    while not game_over:
        draw_board(board)
        print("Es el turno del jugador " + player)
        move = input("Ingresa una posición del 1 al 9: ")
 
        if board[int(move)-1] == " ":
            board[int(move)-1] = player
            if check_win(board, player):
                draw_board(board)
                print("¡El jugador " + player + " ha ganado!")
                game_over = True
            elif " " not in board:
                draw_board(board)
                print("¡Es un empate!")
                game_over = True
            else:
                if player == "X":
                    player = "O"
                else:
                    player = "X"
        else:
            print("Esa posición ya ha sido ocupada. Inténtalo de nuevo.")
 
# Llamar la función principal para jugar
play_game()
