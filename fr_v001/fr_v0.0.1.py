# if you can't find path apply 'import sys'
# import sys
# sys.path.append("D:\\frcobot\\windows")
from fairino_linux import Robot
import math
import time

# default point
homePoint = [-55.0, -90, -90, -90, 90, 0]


def action(defalutPoint, distance, angle_deg):
    """
    c : length
    # offset_pos instance
    # 0: -left +right
    # 1: -front +back
    # 2: -up +down
    # 3: +front -back degree
    # 4: -left +right degree
    # 5: end point turn degree

    error code : 0 >> Normal status
    """
    tool = 0  # Tool number
    user = 0  # Workpiece number
    robot = Robot.RPC("192.168.58.2")

    angle_rad = math.radians(angle_deg)

    cal_heiht = distance - distance * math.sin(angle_rad)
    cal_base = distance * math.cos(90 - angle_rad)

    ret = robot.MoveJ(defalutPoint, tool, user, vel=100)
    print("home point, error code:", ret)
    time.sleep(0.5)

    ret = robot.MoveJ(
        defalutPoint,
        tool,
        user,
        vel=100,
        offset_flag=2,
        offset_pos=[-cal_base, 0, cal_heiht, 0, 45],
    )
    print("left point, error code:", ret)
    time.sleep(0.5)

    ret = robot.MoveJ(
        defalutPoint,
        tool,
        user,
        vel=100,
        offset_flag=2,
        offset_pos=[0, -cal_base, cal_heiht, -45, 0, 0],
    )
    print("front point, error code:", ret)
    time.sleep(0.5)

    ret = robot.MoveJ(
        defalutPoint,
        tool,
        user,
        vel=100,
        offset_flag=2,
        offset_pos=[cal_base, 0, cal_heiht, 0, -45, 0],
    )
    print("right point, error code:", ret)
    time.sleep(0.5)

    ret = robot.MoveJ(
        defalutPoint,
        tool,
        user,
        vel=100,
        offset_flag=2,
        offset_pos=[0, cal_base, cal_heiht, 45, 0, 0],
    )
    print("back point, error code:", ret)
    time.sleep(0.5)

    ret = robot.MoveJ(defalutPoint, tool, user, vel=100)
    print("home point, error code:", ret)


action(homePoint, 300, 45)
