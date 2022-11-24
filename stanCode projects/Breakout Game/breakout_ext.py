"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This is the extension version of the breakout game! Some features were added:
1. Start page, winning page, losing page and reply function.
2. Scoreboard, score ranking board, and a more precise score calculation method.
3. More accurate collision conditions, however, multi-collision still happens sometimes when the speed is too fast.
4. The speed of the ball increase during the game! (after knocking the bricks)
5. Bonus brick appears randomly after knocking out the bricks!!!
6. Three special events were added when the user catches a bonus brick, which is (1). increase the width of the paddle
   (2). randomly changes the color and the size of the ball, and (3). summon a laser beammmmmmmmmm!!!!!
"""
from campy.graphics.gobjects import GRect
from campy.gui.events.timer import pause
from breakoutgraphics_ext import BreakoutGraphics
import random

FRAME_RATE = 10         # 100 frames per second.
SURPRISE_CHANCE = 0.2   # Chance for surprise event.

# Global variables.
sup_switch = 0  # Controls when to generate bonus brick.
ran = 0  # Controls the type of the bonus brick.


def main():
    global sup_switch, ran
    sc = SURPRISE_CHANCE
    sup_rect = GRect(10, 10)
    frame = FRAME_RATE
    graphics = BreakoutGraphics()
    vx = vy = 0  # Initial speed.
    count = 0  # Use to calculate how many bricks were removed.
    count2 = 0  # Controls the speed of the ball.

    # Add the animation loop here!
    while True:
        if count == graphics.total_bricks:  # Win condition.
            graphics.score_count()  # Calculate score.
            graphics.you_win()
            vx = graphics.get_dx()
            vy = graphics.get_dy()
            count = 0
            count2 = 0
        if graphics.live_count == graphics.lives:  # Lose condition.
            graphics.score_count()  # Calculate score.
            graphics.you_lose()
            vx = graphics.get_dx()
            vy = graphics.get_dy()
            count = 0
            count2 = 0
            graphics.label_live.text = 'Lives: ' + str(graphics.lives - graphics.live_count)
        if vx == vy == 0:  # Get vx and vy from the coder file.
            vx = graphics.get_dx()
            vy = graphics.get_dy()
        if graphics.switch:  # Game(animation) start!
            graphics.ball.move(vx, vy)
            if sup_switch == 2:  # If a bonus brick appears.
                sup_rect.move(0, 3)
                # Collision condition of the bonus brick and the paddle.
                if graphics.paddle.y < sup_rect.y < graphics.paddle.y+graphics.paddle.width-sup_rect.height \
                        and graphics.paddle.x < sup_rect.x < graphics.paddle.x+graphics.paddle.width-sup_rect.width:
                    graphics.window.remove(sup_rect)
                    sup_switch = 0
                    c = graphics.bonus(ran, graphics.paddle.width, graphics.paddle.height, sup_rect.x)  # Bonus event!
                    count = count + c
                    count2 = count2 + c
                # If the user didn't catch the bonus brick, remove it.
                if sup_rect.y > graphics.window.height:
                    graphics.window.remove(sup_rect)
                    sup_switch = 0
            if graphics.ball.y > graphics.window.height:  # Ball go over the bottom boundary, lose live.
                graphics.set_ball_position()
                graphics.live_count += 1
                graphics.label_live.text = 'Lives: ' + str(graphics.lives-graphics.live_count)
                count2 = 0  # Reset the increasing speed.
                vx = graphics.get_dx()
                vy = graphics.get_dy()
                graphics.window.remove(sup_rect)  # Remove the bonus brick on the screen.
                sup_rect.x = sup_rect.y = 0
            # Check for Collisions
            if graphics.ball.x+vx <= 0:  # Left boundary.
                # Prevent the ball from moving out of the boundary.
                vx2 = -vx
                vx = -graphics.ball.x
                graphics.ball.move(vx, vy)
                pause(frame)
                vx = vx2

            elif graphics.ball.x+graphics.ball.width+vx >= graphics.window.width:  # Right boundary.
                # Prevent the ball from moving out of the boundary.
                vx2 = -vx
                vx = graphics.window.width - graphics.ball.x - graphics.ball.width
                graphics.ball.move(vx, vy)
                pause(frame)
                vx = vx2

            if graphics.ball.y <= 0:  # Top boundary.
                # Prevent the ball from moving out of the boundary.
                vy2 = -vy
                vy = -graphics.ball.y
                graphics.ball.move(vx, vy)
                pause(frame)
                vy = vy2
            # Check collision with objects.
            if vy < 0:  # If vy < 0, only check the collision between bricks and the top two points of the ball.
                if graphics.window.get_object_at(graphics.ball.x, graphics.ball.y) is not None:
                    obj = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
                    if obj is not graphics.paddle and obj is not graphics.label_score and \
                            obj is not graphics.label_live and obj is not sup_rect:
                        graphics.window.remove(obj)
                        count += 1
                        count2 += 1
                        vy = increase_vy(vy, count2)  # Increase speed when removing a brick.
                        vy = -vy
                        graphics.calculate_score(obj.y+5)  # Calculate the score based on the location of the brick.
                        # Move one step away from the brick, to decrease the probability of multi-collision.
                        prevent_multi_collision(graphics.ball, vx, vy)
                        if sup_switch == 0:  # If no bonus brick exist, create one(depends on the probability).
                            ran = random.randint(1, int(3 / sc))
                            if ran <= 3:
                                sup_rect = surprise(graphics.srs)
                                graphics.window.add(sup_rect, x=obj.x + (obj.width - sup_rect.width) / 2, y=obj.y)
                                sup_switch = 2
                elif graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y) is not None:
                    obj = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
                    if obj is not graphics.paddle and obj is not graphics.label_score and \
                            obj is not graphics.label_live and obj is not sup_rect:
                        graphics.window.remove(obj)
                        count += 1
                        count2 += 1
                        vy = increase_vy(vy, count2)
                        vy = -vy
                        graphics.calculate_score(obj.y+5)
                        # Move one step away from the brick, to decrease the probability of multi-collision.
                        prevent_multi_collision(graphics.ball, vx, vy)
                        if sup_switch == 0:
                            ran = random.randint(1, int(3 / sc))
                            if ran <= 3:
                                sup_rect = surprise(graphics.srs)
                                graphics.window.add(sup_rect, x=obj.x + (obj.width - sup_rect.width) / 2, y=obj.y)
                                sup_switch = 2
            if vy > 0:  # If vy > 0, check the collision between bricks or paddle and the lower two points of the ball.
                if graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height) is not None:
                    obj = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height)
                    if obj is graphics.paddle:
                        vy = -vy
                    elif obj is not graphics.paddle and obj is not graphics.label_score \
                            and obj is not graphics.label_live and obj is not sup_rect:
                        graphics.window.remove(obj)
                        count += 1
                        count2 += 1
                        vy = increase_vy(vy, count2)
                        vy = -vy
                        graphics.calculate_score(obj.y+5)
                        # Move one step away from the brick, to decrease the probability of multi-collision.
                        prevent_multi_collision(graphics.ball, vx, vy)
                        if sup_switch == 0:
                            ran = random.randint(1, int(3 / sc))
                            if ran <= 3:
                                sup_rect = surprise(graphics.srs)
                                graphics.window.add(sup_rect, x=obj.x + (obj.width - sup_rect.width) / 2, y=obj.y)
                                sup_switch = 2
                elif graphics.window.get_object_at(graphics.ball.x+graphics.ball.width,
                                                   graphics.ball.y+graphics.ball.height) is not None:
                    obj = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width,
                                                        graphics.ball.y+graphics.ball.height)
                    if obj is graphics.paddle:
                        vy = -vy
                    elif obj is not graphics.paddle and obj is not graphics.label_score \
                            and obj is not graphics.label_live and obj is not sup_rect:
                        graphics.window.remove(obj)
                        count += 1
                        count2 += 1
                        vy = increase_vy(vy, count2)
                        vy = -vy
                        graphics.calculate_score(obj.y+5)
                        # Move one step away from the brick, to decrease the probability of multi-collision.
                        prevent_multi_collision(graphics.ball, vx, vy)
                        if sup_switch == 0:
                            ran = random.randint(1, int(3 / sc))
                            if ran <= 3:
                                sup_rect = surprise(graphics.srs)
                                graphics.window.add(sup_rect, x=obj.x + (obj.width - sup_rect.width) / 2, y=obj.y)
                                sup_switch = 2
            pause(frame)
        else:
            pause(frame)


def prevent_multi_collision(ball, vx, vy):
    """
    This function prevent unnatural multi-collision by forcing the ball move a short distance to the opposite direction.
    """
    for i in range(1):
        ball.move(vx, vy)
        pause(FRAME_RATE)


def increase_vy(vy, count2):  # This function increases the speed of the ball during the game.
    if vy > 0:
        v = vy + count2 * 0.002
    else:
        v = vy - count2 * 0.002
    return v


def surprise(srs):  # This function creates the bonus brick.
    global sup_switch, ran
    sup_rect = GRect(srs, srs)
    if ran == 1:
        sup_rect.filled = True
        sup_rect.fill_color = 'black'
    elif ran == 2:
        sup_rect.filled = True
        sup_rect.fill_color = 'purple'
    elif ran == 3:
        sup_rect.filled = True
        sup_rect.fill_color = 'pink'
    sup_switch = 1
    return sup_rect


if __name__ == '__main__':
    main()
