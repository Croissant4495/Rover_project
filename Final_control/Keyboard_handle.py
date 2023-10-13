import keyboard

# Name -> index
button_dict = {
    "forward": 0,
    "backward": 3,
    "right": 2,
    "left": 1,
    "gripper_open": 4,
    "gripper_close": 5,
    "line" : 6
}

def check_button():
    button_arr = [0, 0, 0, 0, 0, 0, 0]

    if keyboard.is_pressed("w"):
        button_arr[0] = 1
    if keyboard.is_pressed("a"):
        button_arr[1] = 1
    if keyboard.is_pressed("d"):
        button_arr[2] = 1
    if keyboard.is_pressed("s"):
        button_arr[3] = 1
    if keyboard.is_pressed("m"):
        button_arr[4] = 1
    if keyboard.is_pressed("n"):
        button_arr[5] = 1
    if keyboard.is_pressed("l"):
        button_arr[6] = 1
    if keyboard.is_pressed(";"):
        button_arr[6] = 0


    return button_arr

def decide_mode():
    arr = check_button()
    # Forward
    min_speed = 0
    mid_speed = 60
    max_speed = 120

    if arr[button_dict["line"]]:
        # line track
        return [5, 0, 0, 0]
    else:
        # Driver mode
        # forward and right
        if arr[button_dict["forward"]] == 1 and arr[button_dict["right"]]:
            mode = 1
            speed1 = mid_speed
            speed2 = max_speed
        # forward and left
        elif arr[button_dict["forward"]] == 1 and arr[button_dict["left"]]:
            mode = 1
            speed1 = max_speed
            speed2 = mid_speed
        # forward only
        elif arr[button_dict["forward"]] == 1:        
            mode = 1
            speed1 = max_speed
            speed2 = max_speed
        # right only
        elif arr[button_dict["right"]] == 1:
            mode = 1
            speed1 = mid_speed
            speed2 = min_speed 
        # left only
        elif arr[button_dict["left"]] == 1:
            mode = 1
            speed1 = min_speed
            speed2 = mid_speed
        # if none then stop
        else:
            mode = 0
            speed1 = min_speed
            speed2 = min_speed
        
        gripper_motion = 0
        # Gripper
        if arr[button_dict["gripper_open"]]:
            gripper_motion = 1
        elif arr[button_dict["gripper_close"]]:
            gripper_motion = 2
        
        return [mode, speed1, speed2, gripper_motion]