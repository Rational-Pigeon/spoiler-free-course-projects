import blessed
import random
term = blessed.Terminal()

# Data Types #
# ---------- #


# Racket is a list of empty spaces and '▬'s
# The ▬ entries which are all consecutive, denote the racket.
# Empty space entries denotes empty space.
# examples:
# racket_1 = create_racket(5, term_width)
# racket_2 = create_racket(8, term_width)
def create_racket(length, dimensions):
    board_width = dimensions[0]
    racket = [' '] * board_width
    if length % 2 == 1:
        for i in range(board_width//2 - length//2,
                       board_width//2 + length//2 + 1):
            racket[i] = '▬'
    else:
        for i in range(board_width//2 - length//2,
                       board_width//2 + length//2):
            racket[i] = '▬'
    return racket

# Ball is [Int, Int, int, int, str, int, float]
# intrep. first entry is X position and second entry is Y position
# the 3rd entry is x speed and the 4th entry is y speed
# the 5th entry is the state of the game
# the 6th entry is the number of remaining lives
# the 7th entry is current max speed and 8th entry is upmost limit of max speed
# example:
# newball= [0, 0, 0, 0, pre-launch, 3, 0.3, 0.8]

# Level is a text file whose contents will be rendered on screen as bricks.
# Level also determines the widht and height of the terminal.

# Board is width*height matrix of 0 and 1s.
# intrep. the 1s represent existence of a non-empty character in level
#           the 0s represent empty space in level


# Functions #
# --------- #

# Create the board based on the level file
def create_board(lvl):
    board = []
    with open(lvl, 'r') as file:
        for line in file:
            row = [0 if char == ' ' or char == '\n' else 1 for char in line]
            board.append(row)
        return board


# Get the desired terminal dimensions based on the board
def get_dimensions(board):
    height = len(board)
    row_lengths = []
    for row in board:
        row_lengths.append(len(row))

    width = max(row_lengths)

    return [width, height]


# functions for moving racket
def move_right(racket, board_width):
    if racket[board_width - 1] == ' ':
        racket.pop(board_width - 1)
        racket.insert(0, ' ')


def move_left(racket, board_width):
    if racket[0] == ' ':
        racket.pop(0)
        racket.insert(board_width - 1, ' ')


def update_ball(ball, racket, racket_length, board,
                board_width, board_height, term_height, start_pos):
    state = ball[4]

    if ball[1] >= term_height - 2:
        if ball[5] >= 0:
            state = 'pre-launch'
            ball[5] -= 1
        else:
            state = 'gameover'

    if state == 'gameover':
        newball = [0, 0, 0, 0, 'gameover', - 1, 0.0, 0.0]

    elif state == 'pre-launch':
        newball = [start_pos + racket.index('▬') + racket_length//2,
                   term_height - 4, 0, 0, 'pre-launch',
                   ball[5], ball[6], ball[7]]

    elif state == 'launch':
        newball = [ball[0], ball[1], ball[2], - 0.3, 'playing',
                   ball[5], ball[6], ball[7]]

    else:
        newball = [ball[0]+ball[2], ball[1]+ball[3], ball[2], ball[3], ball[4],
                   ball[5], ball[6], ball[7]]
        maxv = newball[6]
        minv = maxv - 0.15

        # Floating ball. No contact.
        if (newball[0] >= start_pos + board_width - 1 or
           newball[0] <= start_pos + 2):
            newball[2] = - newball[2]

        # Ball touching roof
        elif newball[1] <= 0:
            newball[3] = -newball[3]

        # Ball Touching Racket
        elif (int(newball[1]) == term_height-4
              and (racket.index('▬') <=
                   newball[0] - start_pos
                   <= racket.index('▬') + racket_length)):
            if newball[2] == 0:
                newball[3] = -newball[3]
                newball[2] = random.choice([random.uniform(-maxv, -minv),
                                            random.uniform(minv, maxv)])
                newball[1] = newball[1] - 1
            else:
                newball[3] = - newball[3]
                newball[1] = newball[1] - 1

        # Ball hitting brick
        elif (0 <= newball[0] - start_pos <=
              board_width - 1 and 0 <= newball[1] < board_height):
            if board[int(newball[1])][int(newball[0]) - start_pos] == 1:
                board[int(newball[1])][int(newball[0]) - start_pos] = 0
                if newball[6] < newball[7]:  # increasing max speed after brick hit
                    newball[6] = newball[6] + 0.01

                if newball[3] < 0:
                    newball[3] = random.uniform(minv, maxv)
                    newball[2] = random.uniform(-maxv + 0.05, maxv - 0.05)
                else:
                    newball[3] = random.uniform(-maxv, - minv)

    return newball


# render Racket on screen:
def render_racket(racket, start_pos):
    print(term.move_xy(start_pos, term.height - 3) + ''.join(racket))


# Create a fullscreen Terminal and render level
# on it and center it horizontally on the screen.
def render_level(lvl, start_pos, end_pos):
    term_height = term.height

    with open(lvl, 'r') as file:
        i = 0
        for line in file:
            print(term.move_xy(start_pos, i) + line.rstrip('\n'))
            i += 1
    for i in range(0, term_height - 2):
        print(term.move_xy(start_pos, i) +
              '|' + term.move_xy(end_pos, i) + '|')


def render_ball(ball):
    print(term.move_xy(int(ball[0]), int(ball[1])) + '▇')


def erase_ball(ball):
    print(term.move_xy(int(ball[0]), int(ball[1])) + ' ')


def render_lives(ball, start_pos):
    lives = ball[5]
    for i in range(lives + 1):
        print(term.move_xy(start_pos - 4, term.height - 4 - i) + '▇')


def erase_lives(start_pos):
    for i in range(5):
        print(term.move_xy(start_pos - 4, term.height - 4 - i) + ' ')


def render_instructions():
    print(term.move_xy(2, 6) + "← →: Move")
    print(term.move_xy(2, 8) + "Spacebar: Start")
    print(term.move_xy(2, 10) + "'r': Restart Game")
    print(term.move_xy(2, 12) + "'q': Quit Game")


def play_game(lvl='./lvls/01.txt'):
    board = create_board(lvl)
    dimensions = get_dimensions(board)
    racket_length = 11
    racket = create_racket(racket_length, dimensions)
    board_width = dimensions[0]
    board_height = dimensions[1]
    term_width = term.width
    term_height = term.height
    ball = [0, 0, 0, 0, 'pre-launch', 2, 0.275, 0.625]


# check if lvl is not too big for current terminal
    if term_width < board_width or term_height < board_height + 6:
        raise Exception("Board exceeds terminal size")
    start_pos = term_width//2 - board_width//2

    end_pos = start_pos + board_width

    # Game Loop and Render
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        render_level(lvl, start_pos, end_pos)
        key = ''
        while key != 'q':
            erase_ball(ball)
            render_racket(racket, start_pos)
            ball = update_ball(ball, racket, racket_length, board,
                               board_width, board_height,
                               term_height, start_pos)

            render_ball(ball)
            render_instructions()

            if ball[4] == "pre-launch" or ball[4] == 'gameover':
                erase_lives(start_pos)
            render_lives(ball, start_pos)

            # Handling Key events
            if key and key.is_sequence:
                if key.name == "KEY_LEFT":
                    move_left(racket, board_width)
                elif key.name == "KEY_RIGHT":
                    move_right(racket, board_width)
            elif key == " " and ball[4] == 'pre-launch':
                ball[4] = 'launch'
            elif key == "r":
                play_game(lvl='./lvls/01.txt')

            # Pause duration between each frame to listen to key events
            key = term.inkey(timeout=0.018)


play_game()
