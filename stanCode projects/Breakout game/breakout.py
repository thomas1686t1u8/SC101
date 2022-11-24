"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This version of the breakout game includes the basic functions and the start page, winning page, losing page, score,
lives. I realize that I should add these functions in a extension file after I added them. Therefore, you can ignore
these functions when judging it xD. The collision conditions were not very precise by pretending the ball as a square.
As a result, multi-collision will occur sometimes. This phenomenon can be reduced by slowing the y-axis speed. Moreover,
the score calculation is not very accurate and this will be fixed in the extension version. To sum up, this program
includes all of the basic functions and some incomplete extension functions.
"""
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second


def main():
    graphics = BreakoutGraphics()
    vx = vy = 0  # Initial speed.
    count = 0  # Use to calculate how many bricks were removed.

    # Add the animation loop here!
    while True:
        if count == graphics.total_bricks:  # Win condition.
            graphics.you_win()
            count = 0
        if graphics.live_count == graphics.lives:  # Lose condition.
            graphics.you_lose()
            graphics.label_live.text = 'Lives: ' + str(graphics.lives - graphics.live_count)
        if vx == vy == 0:  # Get vx and vy from the coder file.
            vx = graphics.get_dx()
            vy = graphics.get_dy()
        if graphics.switch:  # Game(animation) start!
            graphics.ball.move(vx, vy)
            if graphics.ball.y > graphics.window.height:
                graphics.set_ball_position()
                graphics.live_count += 1
                graphics.label_live.text = 'Lives: ' + str(graphics.lives-graphics.live_count)
            # Check for Collisions
            if graphics.ball.x+vx <= 0:  # Left boundary.
                # Prevent the ball from moving out of the boundary.
                vx2 = -vx
                vx = -graphics.ball.x
                graphics.ball.move(vx, vy)
                pause(FRAME_RATE)
                vx = vx2

            elif graphics.ball.x+graphics.ball.width+vx >= graphics.window.width:  # Right boundary.
                # Prevent the ball from moving out of the boundary.
                vx2 = -vx
                vx = graphics.window.width - graphics.ball.x - graphics.ball.width
                graphics.ball.move(vx, vy)
                pause(FRAME_RATE)
                vx = vx2

            if graphics.ball.y <= 0:  # Top boundary.
                # Prevent the ball from moving out of the boundary.
                vy2 = -vy
                vy = -graphics.ball.y
                graphics.ball.move(vx, vy)
                pause(FRAME_RATE)
                vy = vy2
            # Check collision with objects
            if graphics.window.get_object_at(graphics.ball.x, graphics.ball.y) is not None:
                obj = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
                if obj is not graphics.paddle and obj is not graphics.label_score and obj is not graphics.label_live:
                    graphics.window.remove(obj)  # Collision with bricks.
                    count += 1
                    vy = -vy
                    graphics.calculate_score(graphics.ball.y)
                prevent_multi_collision(graphics.ball, vx, vy)

            elif graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y) is not None:
                obj = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y)
                if obj is not graphics.paddle and obj is not graphics.label_score and obj is not graphics.label_live:
                    graphics.window.remove(obj)  # Collision with bricks.
                    count += 1
                    vy = -vy
                    graphics.calculate_score(graphics.ball.y)
                prevent_multi_collision(graphics.ball, vx, vy)

            elif graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height) is not None:
                obj = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height)
                if obj is graphics.paddle:  # Collision with paddle.
                    vy = -vy
                if obj is not graphics.paddle and obj is not graphics.label_score and obj is not graphics.label_live:
                    graphics.window.remove(obj)  # Collision with bricks.
                    count += 1
                    vy = -vy
                    graphics.calculate_score(graphics.ball.y)
                prevent_multi_collision(graphics.ball, vx, vy)

            elif graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                               graphics.ball.y + graphics.ball.height) is not None:
                obj = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                    graphics.ball.y + graphics.ball.height)
                if obj is graphics.paddle:  # Collision with paddle.
                    vy = -vy
                if obj is not graphics.paddle and obj is not graphics.label_score and obj is not graphics.label_live:
                    graphics.window.remove(obj)  # Collision with bricks.
                    count += 1
                    vy = -vy
                    graphics.calculate_score(graphics.ball.y)
                prevent_multi_collision(graphics.ball, vx, vy)
            pause(FRAME_RATE)

        else:
            pause(FRAME_RATE)


def prevent_multi_collision(ball, vx, vy):
    """
    This function prevent unnatural multi-collision by forcing the ball move a short distance to the opposite direction.
    """
    for i in range(2):
        ball.move(vx, vy)
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
