import turtle

window = turtle.Screen()
window.title("Ping Pong Game")
window.bgcolor("black")
window.setup(height=600, width=800)
window.tracer(0)  # it stops the window from updating to speed up the game quiet a bit

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()  # to avoid drawing the path of moving objects
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()  # to avoid drawing the path of moving objects
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()  # to avoid drawing the path of moving objects
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2
