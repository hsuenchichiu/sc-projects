"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics(lives=NUM_LIVES)
    while True:
        pause(FRAME_RATE)
        if graphics.start_the_game:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            graphics.ball.move(dx, dy)
            graphics.hit_wall()
            graphics.hit_bricks()
            if graphics.lives == 0:
                graphics.start_the_game = False
                break
            if graphics.bricks_total == 0:
                graphics.window.add(graphics.winning_label, (graphics.window_width-graphics.ball.width)/2-20,
                                    (graphics.window_height-graphics.ball.width)/2)
                break

















if __name__ == '__main__':
    main()
