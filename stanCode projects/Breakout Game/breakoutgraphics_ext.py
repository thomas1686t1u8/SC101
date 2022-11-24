"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

The coder page of the basic breakout game!
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50     # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 5   # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
NUM_LIVES = 3			# Number of attempts
SUP_RECT_SIZE = 10      # The size of the bonus rect.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle.
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0
        # Setup switch.
        self.switch = False
        # Create bricks.
        self.brick = GRect(width=brick_width, height=brick_height)
        self.sup1 = GRect(SUP_RECT_SIZE, SUP_RECT_SIZE)
        self.sup1.filled = True
        self.sup1.fill_color = 'black'
        self.sup2 = GRect(SUP_RECT_SIZE, SUP_RECT_SIZE)
        self.sup2.filled = True
        self.sup2.fill_color = 'purple'
        self.sup3 = GRect(SUP_RECT_SIZE, SUP_RECT_SIZE)
        self.sup3.filled = True
        self.sup3.fill_color = 'pink'
        # Create laser.
        self.laser = GRect(width=10, height=50)
        self.laser.filled = True
        self.laser.fill_color = 'red'
        # Create labels.
        self.label = GLabel('Welcome to the Breakout Game!')  # Welcome label
        self.label.font = '-20'
        # Score label.
        self.score = 0
        self.label_score = GLabel('Score: ' + str(self.score))
        self.label_score.font = '-15'
        self.window.add(self.label, x=(self.window.width - self.label.width) / 2,
                        y=(self.window.height - self.label.height) / 2)
        # Lives count label.
        self.live_count = 0
        self.lives = NUM_LIVES
        self.label_live = GLabel('Lives: ' + str(NUM_LIVES - self.live_count))
        self.label_live.font = '-15'
        # Win label.
        self.label_win = GLabel('You win!')
        self.label_win.font = '-30'
        # Lose label.
        self.label_lose = GLabel('You lose QQ')
        self.label_lose.font = '-30'
        # Replay label.
        self.label_replay = GLabel('Replay?')
        self.label_replay.font = '-20'
        # Start label.
        self.label_start = GLabel('Start')
        self.label_start.font = '-20'
        self.window.add(self.label_start, x=(self.window.width - self.label_start.width)/2, y=(self.window.height*3/4))
        # Score board.
        self.h_score1 = 0
        self.h_score2 = 0
        self.h_score3 = 0
        self.label_scoreboard = GLabel('Ranking')
        self.label_scoreboard.font = '-25'
        self.label_score1 = GLabel('1: ' + str(self.h_score1))
        self.label_score1.font = '-15'
        self.label_score2 = GLabel('1: ' + str(self.h_score2))
        self.label_score2.font = '-15'
        self.label_score3 = GLabel('1: ' + str(self.h_score3))
        self.label_score3.font = '-15'
        # Create variables.
        self.po = paddle_offset
        self.br_r = brick_rows
        self.br_c = brick_cols
        self.bs = brick_spacing
        self.bo = brick_offset
        self.total_bricks = brick_cols * brick_rows
        self.srs = SUP_RECT_SIZE
        self.pw = paddle_width
        self.ph = paddle_height
        self.br = ball_radius
        # Initialize mouse click.
        onmouseclicked(self.set_environment)

    def initialize_game(self):
        """
        This function initialize the game by adding elements on the screen
        and also initialize the mouse listeners
        """
        # Add paddle, ball, and labels.
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2,
                        y=self.window.height-self.po-self.paddle.height)
        self.window.add(self.ball, x=self.window.width/2-self.ball.width, y=self.window.height/2-self.ball.height)
        self.window.add(self.label_score, x=10, y=self.window.height-self.label_score.height)
        self.window.add(self.label_live, x=self.window.width-self.label_live.width-10,
                        y=self.window.height - self.label_live.height)
        # Initialize our mouse listeners.
        onmousemoved(self.change_position)
        onmouseclicked(self.game_start)
        # Add bricks.
        for i in range(self.br_r):
            for j in range(self.br_c):
                self.brick = GRect(width=self.brick.width, height=self.brick.height)
                self.brick.filled = True
                if j < 2:
                    self.brick.fill_color = 'red'
                elif 2 <= j < 4:
                    self.brick.fill_color = 'orange'
                elif 4 <= j < 6:
                    self.brick.fill_color = 'yellow'
                elif 6 <= j < 8:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=i*(self.brick.width+self.bs), y=self.bo+j*(self.brick.height+self.bs))
        self.score = 0
        self.label_score.text = 'Score: ' + str(self.score)

    def change_position(self, event):
        # Control the movement of the paddle.
        if self.paddle.width/2 < event.x < self.window.width - self.paddle.width/2:
            self.paddle.x = event.x - self.paddle.width/2
        elif event.x < self.paddle.width/2:
            self.paddle.x = 0
        else:
            self.paddle.x = self.window.width - self.paddle.width

    def game_start(self, event):
        # Start moving the ball.
        self.switch = True
        if self.__dx == self.__dy == 0:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def set_environment(self, event):
        # Controls when to start or restart the game.
        if self.window.get_object_at(event.x, event.y) is self.label_start:
            self.window.clear()
            self.initialize_game()
        elif self.window.get_object_at(event.x, event.y) is self.label_replay:
            self.window.clear()
            self.initialize_game()

    def get_dx(self):
        # Get the value of __dx.
        return self.__dx

    def get_dy(self):
        # Get the value of __dy.
        return self.__dy

    def set_ball_position(self):
        # If you die, reset the position of the ball.
        self.window.remove(self.ball)
        self.ball = GOval(self.br*2, self.br*2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=self.window.width / 2 - self.br, y=self.window.height / 2 - self.br)
        self.switch = False

    def calculate_score(self, y):
        # Calculate the total score and update.
        if 0 < y < self.bo + 2*(self.brick.height+self.bs):
            self.score += 50  # red bricks = 50pt.
        elif self.bo + 2*(self.brick.height+self.bs) < y < self.bo + 4*(self.brick.height+self.bs):
            self.score += 40  # orange bricks = 40pt.
        elif self.bo + 4*(self.brick.height+self.bs) < y < self.bo + 6*(self.brick.height+self.bs):
            self.score += 30  # yellow bricks = 50pt.
        elif self.bo + 6*(self.brick.height+self.bs) < y < self.bo + 8*(self.brick.height+self.bs):
            self.score += 20  # green bricks = 50pt.
        else:
            self.score += 10  # blue bricks = 50pt.
        self.label_score.text = 'Score: ' + str(self.score)

    def you_win(self):
        # Clear the screen after removing all of the bricks, and show the win page.
        self.window.clear()
        self.window.add(self.label_win, x=(self.window.width-self.label_win.width)/2,
                        y=(self.window.height-self.label_win.height)/2)
        self.window.add(self.label_replay, x=(self.window.width - self.label_replay.width)/2,
                        y=(self.window.height*3/4))
        self.window.add(self.label_score, x=(self.window.width - self.label_score.width) / 2,
                        y=self.label_score.height + 20)
        self.window.add(self.label_scoreboard, x=(self.window.width - self.label_scoreboard.width) / 2,
                        y=self.label_score.height + self.label_scoreboard.height + 40)
        self.window.add(self.label_score1, x=(self.window.width - self.label_score1.width) / 2,
                        y=self.label_score.height + self.label_scoreboard.height + self.label_score1.height + 60)
        self.window.add(self.label_score2, x=(self.window.width - self.label_score2.width) / 2,
                        y=self.label_score.height + self.label_scoreboard.height * 2 + self.label_score2.height + 70)
        self.window.add(self.label_score3, x=(self.window.width - self.label_score3.width) / 2,
                        y=self.label_score.height + self.label_scoreboard.height * 3 + self.label_score3.height + 80)
        self.reset()

    def you_lose(self):
        # Clear the screen after losing all lives, and show the lose page.
        self.window.clear()
        self.window.add(self.label_lose, x=(self.window.width-self.label_lose.width)/2,
                        y=(self.window.height - self.label_lose.height)/2)
        self.window.add(self.label_replay, x=(self.window.width-self.label_replay.width)/2,
                        y=(self.window.height*3/4))
        self.window.add(self.label_score, x=(self.window.width - self.label_score.width) / 2,
                        y=self.label_score.height + 20)
        self.window.add(self.label_scoreboard, x=(self.window.width - self.label_scoreboard.width) / 2,
                        y=self.label_score.height + self.label_scoreboard.height+40)
        self.window.add(self.label_score1, x=(self.window.width - self.label_score1.width) / 2,
                        y=self.label_score.height + self.label_scoreboard.height + self.label_score1.height + 60)
        self.window.add(self.label_score2, x=(self.window.width - self.label_score2.width) / 2,
                        y=self.label_score.height + self.label_scoreboard.height*2 + self.label_score2.height + 70)
        self.window.add(self.label_score3, x=(self.window.width - self.label_score3.width) / 2,
                        y=self.label_score.height + self.label_scoreboard.height*3 + self.label_score3.height + 80)
        self.reset()

    def bonus(self, ram, width, height, sup_x):
        """
        This function creates a bonus event!
        Event 1 : The width of the paddle will increase.
        Event 2 : The ball will randomly changes color and size.
        Event 3 : Create a laser beam to clean up all the bricks in a single column.
        """
        count = 0
        if ram == 1:
            x = self.paddle.x
            y = self.paddle.y
            self.window.remove(self.paddle)
            self.paddle = GRect(width=width+10, height=height)  # Increase the width of the paddle by 10.
            self.paddle.filled = True
            self.paddle.fill_color = 'black'
            self.window.add(self.paddle, x-5, y)
        if ram == 2:
            x = self.ball.x
            y = self.ball.y
            self.window.remove(self.ball)
            random_size = random.randint(10, 40)  # Randomly changes the size of the ball.
            self.ball = GOval(random_size, random_size)
            self.ball.filled = True
            random_color = random.randint(1, 6)  # Randomly changes the color of the ball.
            if random_color == 1:
                self.ball.fill_color = "coral"
            elif random_color == 2:
                self.ball.fill_color = "wheat"
            elif random_color == 3:
                self.ball.fill_color = "olive"
            elif random_color == 4:
                self.ball.fill_color = "magenta"
            elif random_color == 5:
                self.ball.fill_color = "rosybrown"
            else:
                self.ball.fill_color = "firebrick"
            self.window.add(self.ball, x, y)
        if ram == 3:
            for i in range(int(self.paddle.y)):
                self.window.add(self.laser, x=sup_x, y=self.paddle.y-(i+1)*1)  # Creates a laser beam!
                pause(0.2)
                self.window.remove(self.laser)
                if self.window.get_object_at(self.laser.x, self.laser.y) is not None \
                        and self.window.get_object_at(self.laser.x, self.laser.y) is not self.ball:
                    obj = self.window.get_object_at(self.laser.x, self.laser.y)
                    self.window.remove(obj)
                    self.calculate_score(self.laser.y)
                    self.label_score.text = 'Score: ' + str(self.score)
                    count += 1
        return count  # Return the numbers of the cancelled bricks.

    def reset(self):  # Resets the conditions after winning or losing.
        self.paddle = GRect(width=self.pw, height=self.ph)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        # Center a filled ball in the graphical window.
        self.ball = GOval(self.br * 2, self.br * 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx
        onmouseclicked(self.set_environment)
        self.switch = False
        self.live_count = 0
        self.label_live.text = 'Lives: ' + str(self.lives - self.live_count)
        self.label_score.text = 'Score: ' + str(self.score)

    def score_count(self):  # Processes the score ranking.
        if self.score > self.h_score1:
            self.h_score3 = self.h_score2
            self.h_score2 = self.h_score1
            self.h_score1 = self.score
            self.label_score1.text = '1: ' + str(self.h_score1)
            self.label_score2.text = '2: ' + str(self.h_score2)
            self.label_score3.text = '3: ' + str(self.h_score3)
        elif self.h_score1 > self.score > self.h_score2:
            self.h_score3 = self.h_score2
            self.h_score2 = self.score
            self.label_score2.text = '2: ' + str(self.h_score2)
            self.label_score3.text = '3: ' + str(self.h_score3)
        elif self.h_score2 > self.score > self.h_score3:
            self.h_score3 = self.score
            self.label_score3.text = '3: ' + str(self.h_score3)
