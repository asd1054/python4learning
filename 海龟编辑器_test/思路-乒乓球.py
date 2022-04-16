import pgzrun

#TODO
# 封装成类
# 缺少长木板

# def draw():
#     screen.draw.circle((400, 300), 100, 'white')
    # 400，300)表示圆的中心位置坐标，100表示圆的半径，'white'表示圆的颜色为白色。

# 'white' 　　白色
# 'black' 　　黑色
# 'red' 　　　红色
# 'yellow'　　黄色
# 'green' 　　绿色
# 'orange'　　橙色
# 'blue' 　　　蓝色
# 'purple' 　　紫色


# def draw():
#     # 背景填充
#     screen.fill('black')

#     # 实心圆
#     screen.draw.filled_circle((150, 300), 100, 'red')
#     screen.draw.filled_circle((400, 300), 100, 'yellow')
#     screen.draw.filled_circle((650, 300), 100, 'blue')

radius = 10
HEIGHT = 600
WIDTH = 800
x = WIDTH//2
y = HEIGHT//2
speed_y = 2
speed_x = 2


def draw():
    # 背景填充
    screen.fill('black')

    # 实心圆
    screen.draw.filled_circle((x, y), radius, 'red')

# def update():
#     # 逐渐变大的气球
#     global radius
#     radius += 1


def update():

    # 逐渐掉落的气球
    global y,x,speed_x,speed_y
    x += speed_x
    y += speed_y
    # 当碰到边界时，复原
    if y >= HEIGHT-radius or y <= radius:
        speed_y *= -1
    if x >=WIDTH-radius or x <= radius:
        print('你输了')
        quit()

        
pgzrun.go()
