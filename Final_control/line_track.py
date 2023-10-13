import line_follower

min_speed = 0
mid_speed = 40
max_speed = 60

def move_line():
    line_follower.control()
    motion = line_follower.get_x()

    # forward
    if motion == 1:
        mode = 1
        speed1 = max_speed
        speed2 = max_speed
    # right
    if motion == 3:
        mode = 1
        speed1 = mid_speed
        speed2 = min_speed 
    # left
    if motion == 2:
        mode = 1
        speed1 = min_speed
        speed2 = mid_speed

    return [mode, speed1, speed2, 0]