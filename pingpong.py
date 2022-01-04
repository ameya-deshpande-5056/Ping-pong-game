import turtle

# Window
wind = turtle.Screen()
wind.title('Ping pong')
wind.bgcolor('black')
wind.setup(width=800, height=600)
wind.tracer(0)

# Player
play = turtle.Turtle()
play.shape('square')
play.color('white')
play.shapesize(stretch_wid=5, stretch_len=1)
play.penup()
play.goto(-350,0)

# Bot
bot = turtle.Turtle()
bot.shape('square')
bot.color('white')
bot.shapesize(stretch_wid=5, stretch_len=1)
bot.penup()
bot.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0,0)
ball_x = 0.1
ball_y = 0.1
ball.speed(30)

#score
sboard = turtle.Turtle()
sboard.shape('square')
sboard.color('white')
sboard.penup()
sboard.hideturtle()
sboard.goto(0, 260)
sboard.write("Player: 0                  Bot: 0", align="center", font=("Courier", 24,'normal'))
score_a = 0
score_b = 0

# Functions
def play_up():
    if play.ycor() < 250:
        y = play.ycor()
        y += 30
        play.sety(y)
def play_down():
    if play.ycor() > -250:
        y = play.ycor()
        y -= 30
        play.sety(y)
def bot_up():
    if bot.ycor() < 250:
        y = bot.ycor()
        y += 30
        bot.sety(y)
def bot_down():
    if bot.ycor() > -250:
        y = bot.ycor()
        y -= 30
        bot.sety(y)

# Keyboard Bindings
wind.listen()
wind.onkeypress(play_up, 'Up')
wind.onkeypress(play_down, 'Down')

while True:
    wind.update()

    # BAll movement
    ball.setx(ball.xcor() + ball_x)
    ball.sety(ball.ycor() + ball_y)

    # Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball_y *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball_y *= -1

    #score
    if ball.xcor() > 350:
        score_a += 1
        sboard.clear()
        sboard.write("Player: {}                  Bot: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))
        ball.goto(0,0)
        ball_x *= -1
    elif ball.xcor() < -350:
        score_b += 1
        sboard.clear()
        sboard.write("Player: {}                  Bot: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))
        ball.goto(0, 0)
        ball_x *= -1

    # Collision with bars
    if ball.xcor() < -340 and ball.ycor() < play.ycor() + 50 and ball.ycor() > play.ycor() - 50:
        ball_x *= -1
    elif ball.xcor() > 340 and ball.ycor() < bot.ycor() + 50 and ball.ycor() > bot.ycor() - 50:
        ball_x *= -1

    # Bot control
    if bot.ycor() < ball.ycor() + 10 and abs(bot.ycor() - ball.ycor()) >= 75:
        bot_up()
    elif bot.ycor() > ball.ycor() - 10 and abs(bot.ycor() - ball.ycor()) >= 75:
        bot_down()
