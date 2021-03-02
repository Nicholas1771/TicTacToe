# Dictionary of game board positions and their stored values 'X' or 'O'
game_board = {}

# List of winning lines represented in tuples
winning_lines = [('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'), ('1', '4', '7'),
                 ('2', '5', '8'), ('3', '6', '9'), ('1', '5', '9'), ('3', '5', '7')]

# Represents the current player turn, player 1 = 1 player 2 = 2
player_turn = 1

# Winner of the game, 0 = game not over, 1 = player 1, 2 = player 2, 3 = draw
winner = 0

# Stores the marker for each player
markers = {'1': 'X', '2': 'O'}


def init_game():
    """
    This method is used to initialize the tic tac toe game or reset to a new game. It resets the game board, winner and player turn
    """
    global game_board, player_turn, winner
    game_board = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
    player_turn = 1
    winner = 0


def display_board():
    """
    This method displays the game board in a 3 x 3 grid. It also places lines in between game board slots to
    make the board more visually appealing
    """
    for key, value in game_board.items():
        # Prints the current value in the game board and prevents a new line after the print
        print(value, end='')

        # If the dictionary key is a multiple of 3 this means the board needs to print a new line and the border
        if int(key) % 3 == 0:
            if int(key) != 9:
                # Print the border unless the position is at the last line
                print('\n- | - | -')
        else:
            # If not at a multiple of 3 it prints a border between slots (|)
            print(' | ', end='')


def game_round():
    """
    This method performs 1 round in a tic tac toe game. It prompts the user for a position to place their marker.
    The game places a X or O depending on who's turn it is. After placing the marker on the game board the player turn
    is switched to the other player, setting them up to play the next round.
    """
    global player_turn, game_board

    # Lets the players know who's turn it is
    print(f'\nPlayer {player_turn} ({markers[str(player_turn)]}), it is your turn')

    # Loops until the user enters a valid position and input
    while True:
        # Prompts the user to enter a position and saves the value
        choice = input('Choose an empty spot to place your piece (1 - 9): ')

        # Validates the user input and breaks out of the infinite loop if successfully validated
        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and game_board[choice] == ' ':
            break
        else:
            # User has entered either an invalid input or the position already has a marker
            print('Invalid choice')

    # Places a marker on the validated chosen position
    game_board[choice] = markers[str(player_turn)]

    # Switches the player turn to the other player
    if player_turn == 1:
        player_turn = 2
    else:
        player_turn = 1


def check_winner():
    """
    This method loops through the pre-defined winning tic tac toe lines. If any line has 3 of the same markers (X or O)
    the game is won. The method gets the winner based on the marker and saves the winner value. If there is no winner,
    and throughout the loop there was no empty spot, this means the board is full and it is a draw. The method saves
    winner value as 3 to indicate a drawn game.
    """
    global winner

    # Board full starts out as true and is changed to False upon the first empty slot found
    board_full = True

    # Loops through every pre-defined winning line
    for line in winning_lines:

        # Saves the 3 values in the winning line
        spot1 = game_board[line[0]]
        spot2 = game_board[line[1]]
        spot3 = game_board[line[2]]

        # Checks if there is an empty spot in the winning line. If there is the board is not full.
        if ' ' in [spot1, spot2, spot3]:
            board_full = False
        elif spot1 == spot2 and spot1 == spot3:
            # Since none of the spots are empty, checks if they are all the same marker indicating a winner.
            if spot1 == markers['1']:
                winner = 1
            else:
                winner = 2

    # If there is no winner and the board is full, set winner to 3 indicating a drawn game
    if winner == 0 and board_full:
        winner = 3


def run_game():
    """
    This method runs the tic tac toe game. It keeps displaying the board, playing rounds, and checking winner until
    a winner is found or the game is drawn. It then allows the user to start another game or end the program.
    """
    while True:

        # Initialize game variables
        init_game()

        # Plays game until winner is found or game is drawn
        while winner == 0:
            display_board()
            game_round()
            check_winner()

        # Displays the winner to the players
        if winner == 3:
            print('\n\nNo one won')
        else:
            print(f'\n\nPlayer {winner} won the game')

        # Displays final board result
        display_board()

        # Prompts the user to play again
        if input("\nPlay again? (Y or N)") == 'N':
            break


# Run the game
run_game()
