import turtle, random

WIDTH = 500     # Screen width
HEIGHT = 500    # Screen height
DELAY = 200     # Speed of snake movement
FOODSIZE = 20


offsets = { "up": (0, 20), 
           "down": (0, -20), 
           "right": (20, 0), 
           "left": (-20, 0), 
           }

# Old way of setting direction according to arrow key pressed
#
# def goUp():
#     global snakeDirection
#     if snakeDirection != "down":    # if snake returns from direction it will just over draw
#         snakeDirection = "up"
# def goDown():
#     global snakeDirection
#     if snakeDirection != "up":
#         snakeDirection = "down"
# def goRight():
#     global snakeDirection
#     if snakeDirection != "left":
#         snakeDirection = "right"
# def goLeft():
#     global snakeDirection
#     if snakeDirection != "right":
#         snakeDirection = "left"

def bindDirection():
    screen.onkey(lambda: setDirection("up"), "Up")
    screen.onkey(lambda: setDirection("down"), "Down")
    screen.onkey(lambda: setDirection("right"), "Right")
    screen.onkey(lambda: setDirection("left"), "Left")

def setDirection(direction):
    global snakeDirection
    if direction == "up":
        if snakeDirection != "down":
            snakeDirection = "up"
    elif direction == "down":
        if snakeDirection != "up":
            snakeDirection = "down"
    elif direction == "right":
        if snakeDirection != "left":
            snakeDirection = "right"
    elif direction == "left":
        if snakeDirection != "right":
            snakeDirection = "left"

def snakeMove():
    snake.clearstamps()

    sHead = snakeBody[-1].copy()
    #sHead[0] += 20
    sHead[0] += offsets[snakeDirection][0]
    sHead[1] += offsets[snakeDirection][1]

    # Check if snake has turned into itself
    # Check if snake has reached to top or sides edges of the screen
    if sHead in snakeBody or \
        sHead[0] > WIDTH/2 or sHead[0] < -WIDTH/2 or \
        sHead[1] > HEIGHT/2 or HEIGHT < -HEIGHT/2:
        turtle.bye()
    else:
        snakeBody.append(sHead)
        if not detectCollision():
            snakeBody.pop(0)

        for i in snakeBody:
            snake.goto(i[0], i[1])
            snake.stamp()

        screen.title(f'Snake game: {score}')
        screen.update()

        turtle.ontimer(snakeMove, DELAY)

def detectCollision():
    global foodPos, score
    sHead = snakeBody[-1].copy
    if (getDistance(snakeBody[-1], foodPos) < 20):
        foodPos = newFoodPos()
        food.goto(foodPos)
        score += 1
        return True
    return False
    
def newFoodPos():
    x = random.randint(-WIDTH/2+FOODSIZE, WIDTH/2-FOODSIZE)
    y = random.randint(-HEIGHT/2+FOODSIZE, HEIGHT/2-FOODSIZE)
    return (x, y)

def getDistance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2-y1)**2 + (x2-x1)**2)**0.5   # Pythagora's Theorem - sqrt( sqr(y2-y1)+sqr(x2-x1) )
    return distance

# Set up the screen
score = 0
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("cyan")
screen.tracer(0)   # If not 0, it will start drawing snake before erasing it with clearstamps() above

# Listen for arrow keys being pressed
screen.listen()
bindDirection()     # New way to set direction
# Old way of setting direction according to arrow key pressed
# screen.onkey(goUp, "Up")
# screen.onkey(goDown, "Down")
# screen.onkey(goRight, "Right")
# screen.onkey(goLeft, "Left")


# Set up food
food = turtle.Turtle()
food.shape("circle")
food.shapesize(FOODSIZE/20)
food.color("red")
food.penup()
foodPos = newFoodPos()
food.goto(foodPos)




# Set up snake
snake = turtle.Turtle()
snake.shape("square")
snake.penup()

snakeBody = [[0, 0], [20, 0], [40, 0], [60, 0]]

snakeDirection = "up"
# Snake initial print
for i in snakeBody:
    snake.goto(i[0], i[1])
    snake.stamp()       # stamp leaves draws the object and leaves it drawn on the screen, otherwise it would be deleted



# call function to start moving the snake
snakeMove()

# Standard finishing command
turtle.done()
