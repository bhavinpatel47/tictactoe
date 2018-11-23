print('')

state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
demo_state = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
mapping = {7: (0, 0), 8: (0, 1), 9: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 1: (2, 0), 2: (2, 1), 3: (2, 2)}
available = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
winner = ({1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7})
chosen1 = set()
chosen2 = set()


def init():
    global state
    global available
    global chosen1
    global chosen2
    global player
    state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    available = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    chosen1 = set()
    chosen2 = set()
    player = 1
    draw_board(demo_state)


def draw_board(updated_state):
    for each_row in updated_state:
        print('')
        print('-------------')
        for column in each_row:
            print('|', column, '', end="")
        print('|', end='')
    print()
    print('-------------')


def check_win(chosen):
    for win_set in winner:
        if set(win_set).issubset(chosen):
            return True
    return False


init()

while True:
    """ game-loop """
    if len(available) > 1:
        try:
            choice = int(input('Enter your choice for player {}. type 0 to end game: '.format(player)))
        except ValueError as e:
            draw_board(state)
            print('Error: Enter a number')
            continue
        if choice in available:
            if choice == 0:
                print('ending game')
                break
            if player == 1:
                row, col = mapping[choice]
                state[row][col] = 'X'
                available.remove(choice)
                chosen1.add(choice)
                player = 2
                draw_board(state)
                if check_win(chosen1):
                    print("\t**************\n\tPlayer 1 wins!\n\t**************")
                    print('Want to play again? yes or no: ')
                    again = input()
                    if again == 'yes':
                        init()
                    else:
                        break
            elif player == 2:
                row, col = mapping[choice]
                state[row][col] = 'O'
                available.remove(choice)
                chosen2.add(choice)
                player = 1
                draw_board(state)
                if check_win(chosen2):
                    print("\t***************\n\tPlayer 2 wins!\n\t***************")
                    print('Want to play again? yes or no: ')
                    again = input()
                    if again == 'yes':
                        init()
                    else:
                        break
        else:
            draw_board(state)
            print('Error: try again')
            continue
    else:
        print("It's a TIE!")
        print('Want to play again? yes or no: ')
        again = input()
        if again == 'yes':
            init()
        else:
            break
