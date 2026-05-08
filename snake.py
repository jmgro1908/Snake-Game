from turtle import *
from random import randrange, choice
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

FOOD_DIRECTIONS = [
    vector(10, 0),   # right
    vector(-10, 0),  # left
    vector(0, 10),   # up
    vector(0, -10),  # down
]

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def inside_food(pos):
    "Return True if food position is inside boundaries."
    return -200 < pos.x < 190 and -200 < pos.y < 190

def move_food():
    "Move food one step in a random valid direction."
    shuffled = FOOD_DIRECTIONS[:]
    for _ in range(4):
        direction = choice(shuffled)
        new_pos = food.copy()
        new_pos.move(direction)
        if inside_food(new_pos):
            food.x = new_pos.x
            food.y = new_pos.y
            break  

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    move_food()

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
