"""
File: bouncing_ball.py
Name:HsuenChi Chiu
-------------------------
TODO: This program stinulates a ball fall down from a higher place
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_X)
switch = True
turns = 3


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(ball)
    ball.filled = True
    onmouseclicked(bounce)


def bounce(mouse):
    global ball, turns, switch
    start=GOval(SIZE, SIZE, x=START_X, y=START_Y)
    start.filled=True
    speed = GRAVITY

    if switch:
        switch = False
        while True:
            ball.move(VX, speed)
            speed += GRAVITY
            # bounce back
            if ball.y + SIZE >= window.height:
                speed *= -REDUCE
            # back to start place
            if ball.x+SIZE >= window.width:
                window.add(ball, x=START_X, y=START_Y)
                turns -= 1
                if turns > 0:
                    switch = True
                break

            pause(DELAY)

            # if turns == 0:
            #     break








if __name__ == "__main__":
    main()
