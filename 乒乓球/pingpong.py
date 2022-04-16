# -*- encoding: utf-8 -*-
'''
@File    :   pingpong.py
@Time    :   2022/03/25 00:01:21
@Author  :   NMOON 
@Version :   1.0
@Contact :   ay1054@qq.com
@Personal:   应无所往，而生其心
@Function:   乒乓球小游戏
@Desc    :   失败，小球无限快，暂无解决方案，只能放弃
'''

# here put the import lib
import turtle


game_witdh = 800
game_height = 600
wn = turtle.Screen()
wn.title("Pong by Nmoon")
wn.bgcolor('black')
wn.setup(width=game_witdh, height=game_height)
wn.tracer(0)


class Paddle:  # 配置玩家
    def __init__(self, brith_point=-350):
        self.pd = turtle.Turtle()
        self.pd.speed(0)
        self.pd.shape('square')
        self.pd.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        self.pd.color('white')
        self.pd.penup()
        self.pd.goto(brith_point, 0)
        self.dy = 20

    def padUp(self):
        self.pd.sety(self.pd.ycor() + self.dy)

    def padDown(self):
        self.pd.sety(self.pd.ycor() - self.dy)


class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed('slowest')
        self.ball.shape('circle')
        self.ball.color('white')
        self.ball.penup()
        self.ball.goto(0, 0)
        self.dx = 2
        self.dy = 2

    def move(self):
        self.ball.setx(self.ball.xcor() + self.dx)
        self.ball.sety(self.ball.xcor() + self.dy)

    def borderLimit(self):
        if self.ball.ycor() > game_height / 2:
            self.ball.sety(game_height / 2)
            self.dy *= -1

        if self.ball.ycor() < -game_height / 2:
            self.ball.sety(-game_height / 2)
            self.dy *= -1

        if self.ball.xcor() > game_witdh / 2:
            self.ball.goto(0, 0)
            self.dx *= -1

        if self.ball.xcor() < -game_witdh / 2:
            self.ball.goto(0, 0)
            self.dx *= -1


# 玩家 A
paddle_a = Paddle(brith_point=-350)

#  玩家 B
paddle_b = Paddle(brith_point=350)

wn.listen()
wn.onkeypress(paddle_a.padUp, 'w')
wn.onkeypress(paddle_a.padDown, 's')
wn.onkeypress(paddle_b.padUp, 'Up')
wn.onkeypress(paddle_b.padDown, 'Down')

# 球
ball = Ball()

# 游戏开始
while True:
    wn.update()

    ball.move()

    ball.borderLimit()
    if ball.ball.xcor() > 340 and (
        ball.ball.ycor() < paddle_b.pd.ycor() + 40
        and ball.ball.ycor() > paddle_b.pd.ycor() - 40
    ):
        ball.ball.setx(340)
        ball.dx *= -1

    if ball.ball.xcor() > -340 and (
        ball.ball.ycor() < paddle_a.pd.ycor() + 40
        and ball.ball.ycor() > paddle_a.pd.ycor() - 40
    ):
        ball.ball.setx(-340)
        ball.dx *= -1

