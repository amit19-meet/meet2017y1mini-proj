import turtle
import random #we will need this later in the lab

turtle.tracer(1,0) #this helps the turtle move mor smoothly

SIZE_X = 800
SIZE_Y = 500
turtle.setup(SIZE_X, SIZE_Y) #it's the turtle window size

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 3

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")
#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for i in range(START_LENGTH):
    x_pos = snake.pos()[0]
    y_pos = snake.pos()[1]

    #add SQUARE_SIZE to x_pos. where does x_pos point to now?
    x_pos+=SQUARE_SIZE

    my_pos = (x_pos,y_pos) #store position variables in a tuple
    snake.goto(x_pos,y_pos) #move sanke to new (x,y)

    pos_list.append(my_pos)

    #save the stamp ID. you will need to erase it later. Then append
    #it to stamp_list
    snake2 = snake.stamp()
    stamp_list.append(snake2)

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
TIME_STEP = 100 #Update snake position after this many milliseconds
SPACEBAR = "space"

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    global direction
    direction = UP
    #move_snake() #update the snake drawing <- remember me later
    print("you pressed the up key!")

def down():
    global direction
    direction = DOWN
    #move_snake()
    print("you pressed the down key!")

def left():
    global direction
    direction = LEFT
    #move_snake()
    print("you pressed the left key!")

def right():
    global direction
    direction = RIGHT
    #move_snake()
    print("you pressed the right key!")

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("you moves right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("you moved left!")
    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("you moved down!")
    elif direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("you moved up!")

    my_pos = snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ##### SPECIAL PLACE= remember it for part 5
    global food_stamps, food_pos
    #if snake is on top of food item
    if snake.pos() in food_pos:
        food_ind = food_pos.index(snake.pos()) #what does this do?
        food.clearstamp(food_stamps[food_ind]) #remove eaten food stamp
        food_pos.pop(food_ind) #remove eaten food position
        food.stamps.pop(food_ind) #remove eaten food stamp
        print("you have eaten the food!")

    #HINT: this if statement may be useful for part 8
        
    #pop zeroth element in pos_list to get rid of last the last
    #piece of the tail
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
    #grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    #the next three lines check if the snake is hitting the right edge
    if new_x_pos >= RIGHT_EDGE:
        print("you hit the right edge! game over!")
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("you hit the left edge! game over!")
        quit()
    elif new_y_pos >= UP_EDGE:
        print("you hit the top edge! game over!")
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("you hit the bottom edge! game over!")
        quit()
    turtle.ontimer(move_snake, TIME_STEP)
move_snake()

turtle.register_shape("trash.gif") #add trash picture 

food = turtle.clone()
food.shape("trash.gif")

#location of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

for this_food_pos in food_pos:
    food.goto(this_food_pos)
    food1 = food.stamp()
    food_stamps.append(food1)
    

    
        
    
    

