def main_game():
    count = 0
    class Board:
        def __init__(self):
            self.board = ["-", "-", "-",
                          "-", "-", "-",
                          "-", "-", "-"]
        def displayBoard(self):
            print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
            print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
            print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    turn = 'X'
    board = Board()
    board.displayBoard()

    class Player:
        def __init__(self):
            pass

        def insertXSign(self):
            location = input('Where do you want to place your symbol? 1-9: ')
            cond_var1 = False
            while cond_var1 == False:
                if location not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    location = input('You have entered an invalid input, please try again!')
                else:
                    cond_var1 = True
                location = int(location)
                location = location - 1
                if board.board[location] == 'O':
                    location = int(input('This spot is already taken, please choose somewhere else!'))
                    location = location - 1
                    board.board[location] = 'X'
                else:
                    cond_var1 = True
            board.board[location] = 'X'

        def insertOSign(self):
            location = input('Where do you want to place your symbol? 1-9: ')
            cond_var2 = False
            while cond_var2 == False:
                if location not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    location = input('You have entered an invalid input, please try again!')
                else:
                    cond_var2 = True
                location = int(location)
                location = location - 1
                if board.board[location] == 'X':
                    location = int(input('This spot is already taken, please choose somewhere else!'))
                    location = location - 1
                    board.board[location] = 'O'
                else:
                    cond_var2 = True
            board.board[location] = 'O'

    player = Player()
    while True:
        global location
        if turn == 'X':
            print('It is X turn')
            player.insertXSign()
            turn = 'O'
            count += 1
        elif turn == 'O':
            print('It is O turn')
            player.insertOSign()
            turn = 'X'
            count += 1

        board.displayBoard()
        #Check for a win in the rows
        if board.board[0] == board.board[1] == board.board[2] != '-':
            print(board.board[0] + ' wins')
            break
        elif board.board[3] == board.board[4] == board.board[5] != '-':
            print(board.board[4] + ' wins')
            break
        elif board.board[6] == board.board[7] == board.board[8] != '-':
            print(board.board[7] + ' wins')
            break
        elif board.board[2] == board.board[4] == board.board[6] != '-':
            print(board.board[6] + ' wins')
            break
        elif board.board[0] == board.board[4] == board.board[8] != '-':
            print(board.board[8] + ' wins')
            break
        elif count == 9:
            print('This game is a tie!')
            break
        #check for win in columns
        if board.board[0] == board.board[3] == board.board[6] != '-':
            print(board.board[0] + ' wins')
            break
        elif board.board[1] == board.board[4] == board.board[7] != '-':
            print(board.board[1] + ' wins')
            break
        elif board.board[2] == board.board[5] == board.board[8] != '-':
            print(board.board[2] + ' wins')
            break
main_game()

while True:
    re_game = input('Would you like to play again? y/n')
    if re_game == 'y':
        main_game()
    elif re_game == 'n':
        print('Until next time!!')
        break