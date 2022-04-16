import pgzrun  # 导入游戏库
import random
WIDTH = 288  # 设置窗口的宽度
HEIGHT = 488  # 设置窗口的高度

#todo
# 增加开始，结束！重新开始等按钮


# 导入背景图片
background = Actor(
    'day')
bird = Actor('blue-mid.png')
bird.x = 50
bird.y = HEIGHT//2

bar_up = Actor('green-pipe.png') # 导入障碍物上半部分图片
bar_up.x = 150# 设置障碍物上半部分的x坐标
bar_up.y = 0 # 设置障碍物上半部分的y坐标
bar_down = Actor('green-pipe.png') # 导入障碍物下半部分图片
bar_down.x = 150 # 设置障碍物下半部分的x坐标
bar_down.y = 600 # 设置障碍物下半部分的y坐标

score = 0
speed = 2

def draw():  # 绘制模块，每帧重复执行
    background.draw()  # 绘制背景图片
    bird.draw()
    bar_up.draw()
    bar_down.draw()
    screen.draw.text(str(score), (30, 30),
                     fontsize=50, color='green')


def update():
    global score
    bird.y += 3
    bar_down.x -= speed 
    bar_up.x -= speed 
    if bar_down.x <0:
        score += 1
        bar_down.x = WIDTH
        bar_up.x = WIDTH
        bar_up.y = random.randint(-160, 160)
        bar_down.y = 320+160+bar_up.y
    if bird.colliderect(bar_down) or bird.colliderect(bar_up) or bird.y<0 or bird.y>HEIGHT:
        print("GAME OVER")


def on_mouse_down():  # 当鼠标点击时运行
    bird.y = bird.y - 30  # 小鸟y坐标减小，即上升一段距离


pgzrun.go()  # 开始执行游戏
