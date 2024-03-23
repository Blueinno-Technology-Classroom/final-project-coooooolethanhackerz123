from board import Board
from player import Player
from computerplayer import ComputerPlayer

board = Board()

#print(board.row1)
#board.draw()

#board.row1 = ['X', 'O', 'X']
#board.row2 = [' ', 'X', 'O']
#board.row3 = ['O', 'X', 'O']
#board.draw()

print('Select a mode:')
print()
print('1. Player vs Player')
print('2. Player vs Computer')

mode = input()

while mode not in ['1','2']:
    mode = input('invalid input, please try again')


if mode == '1':
    player1 = Player('P1','x',board)
    player2 = Player('P2','o',board)
    current_player = player1

    while True:
        not_valid = True
        while not_valid:
            board.draw()
            not_valid = not(current_player.get_input())
            if not_valid:
                print('-------------------')
                print('Invalid input, try again')
                print('-------------------------------------------------------------------------------------------------------')
            else: 
                if current_player == player1:
                    current_player = player2
                else:
                    current_player = player1

            winner = board.check_winner()
            tie = board.is_full()

            if player1.piece == winner:
                print(f'{player1.name}WINS!')
                break
            elif player2.piece == winner:
                board.draw()
                print(f'{player1.name}WINS!')
                break
            elif tie:
                board.draw()
                print('GAME TIED!')
                break

elif mode =='2':

    player1 = Player('P1','x',board)
    player2 = ComputerPlayer('AI','o',board)
    current_player = player1

    while True:
        if current_player == player1:
            not_valid = True
            while not_valid:
                board.draw()
                not_valid = not(current_player.get_input())
                if not_valid:
                    print('-------------------')
                    print('Invalid input, try again')
                    print('-------------------------------------------------------------------------------------------------------')
                else:
                    current_player = player2
        else:
            current_player.move()
            current_player = player1

        winner = board.check_winner()
        tie = board.is_full()

        if player1.piece == winner:
            print(f'{player1.name}WINS!')
            break
        elif player2.piece == winner:
                board.draw()
                print(f'{player1.name}WINS!')
                break
        elif tie:
                board.draw()
                print('GAME TIED!')
                break