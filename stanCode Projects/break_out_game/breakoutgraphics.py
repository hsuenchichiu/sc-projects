"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10    # Number of rows of bricks.
BRICK_COLS = 10   # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING, lives = 0,
                 title='Breakout'):
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_rows = brick_rows
        self.brick_offset = brick_offset
        self.brick_cols = brick_cols
        self.brick_spacing = brick_spacing
        self.lives = lives
        self.bricks_total=brick_cols*brick_rows
        self.winning_label = GLabel('You Win')


        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.window_height = window_height
        self.window_width = window_width
        self.paddle_offset = paddle_offset

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'darkgray'
        self.paddle.color = 'darkgray'
        self.window.add(self.paddle, (window_width-self.paddle.width)/2, window_height-paddle_offset)

        # Center a filled ball in the graphical window.
        self.ball = GOval(2*ball_radius, 2*ball_radius)
        self.ball.filled = True
        self.window.add(self.ball, (self.window_width-self.ball.width)/2, (self.window_height-self.ball.width)/2)

        self.set_bricks()
        self.start_x = (self.window_width - self.ball.width) / 2
        self.start_y = (self.window_height - self.ball.width) / 2


        # Default initial velocity for the ball.
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx


        # Initialize our mouse listeners.
        onmousemoved(self.moving_paddle)
        onmouseclicked(self.handle_click)
        self.start_the_game = False

        # Draw bricks.
    def set_bricks(self):
        for i in range(self.brick_rows):
            for j in range(self.brick_cols):
                self.brick = GRect(self.brick_width, self.brick_height)
                self.brick.filled = True
                if i % 2 != 0:
                    self.brick.fill_color = 'rosybrown'
                    self.brick.color = 'rosybrown'
                else:
                    self.brick.fill_color = 'steelblue'
                    self.brick.color = 'steelblue'

                self.window.add(self.brick, self.brick_spacing*(j-1)+self.brick.width*j,
                                self.brick_offset+self.brick.height*(i-1)+self.brick_spacing*(i-1))

    #move the paddle
    def moving_paddle(self, mouse):
        if mouse.x-(self.paddle.width)/2 >= self.window_width-self.paddle.width:
            self.paddle.x = self.window_width-self.paddle.width
        elif mouse.x <= 0:
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x-(self.paddle.width)/2
        self.paddle.y = self.window_height-self.paddle_offset

    # start onemouseclicked
    def handle_click(self, event):
        self.start_the_game = True

# getters
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy



    def hit_wall(self):
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx *= -1
        if self.ball.y <= 0:
            self.__dy *= -1
        if self.ball.y + self.ball.height >= self.window.height:
            self.window.add(self.ball, self.start_x, self.start_y)
            self.start_the_game = False
            self.lives -= 1


    def hit_bricks(self):
        upper_left = self.window.get_object_at(self.ball.x,self.ball.y)
        upper_right = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        downer_left = self.window.get_object_at(self.ball.x,self.ball.y+self.ball.width)
        downer_right = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.width)

        if upper_left is not None:
            if upper_left is self.paddle:
                if self.__dy >0:
                    self.__dy *= -1
                    self.bricks_total -= 1
            else:
                self.window.remove(upper_left)
                self.__dy *= -1
                self.bricks_total -= 1

        elif upper_right is not None:
            if upper_right is self.paddle:
                if self.__dy > 0:
                    self.__dy *= -1
            else:
                self.window.remove(upper_right)
                self.__dy *= -1
                self.bricks_total-=1

        elif downer_left is not None:
            if downer_left is self.paddle:
                if self.__dy > 0:
                    self.__dy *= -1
            else:
                self.window.remove(downer_left)
                self.__dy *= -1

        elif downer_right is not None:
            if downer_right is self.paddle:
                if self.__dy > 0:
                    self.__dy *= -1
            else:
                self.window.remove(downer_right)
                self.__dy *= -1
                self.bricks_total -= 1








