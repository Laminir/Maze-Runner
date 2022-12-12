"""
Maze Runner Game

Maze Runner is a game where a player tries to find treasure
in a maze without running into any monsters lurking in that maze

@author Gavyn Roberts
"""
# Note: This skeleton file has a lot of comments in it.
#       Read the comments. They will help give you some
#       direction and understanding of how to use the code
#       that has already been given to you.
#
#       Later if you find them pesky, you can delete them

import turtle
import functools
import random
import time
turtle.register_shape("MARIO.gif")
import winsound
turtle.register_shape("loading.gif")

# NOTE: cannot play sound in replit currently
# import os #for macs
# import winsound #for windows
#import python.Lib.turtle

# Set up window
window = turtle.Screen()
window.title("Maze Runner by YOUR_NAME")
window.bgcolor("black")
window.setup(width=0.3, height=0.5)
window.tracer(0)
#--------------------------------------------------------------



# Settings
global DEFAULT_TEXT_FILE
global MAZE_TEXT_FILE
DEFAULT_TEXT_FILE = "maze_1.txt"
MAZE_TEXT_FILE = "maze_1.txt"

# Text feedback for winning the game, or losing the game
global game_end_list
global game_win_list
global playlist
game_end_list = ["You Lost", "Game Over", "Get Pwned", "You Suck"]
game_win_list = ["You Won", "Nice Job", "W"]
game_playlist = ["Graze the Roof.wav", "Undyne.wav"]
game_loading_tips = ["Tip: You can press Escape to exit to the main menu", "Tip: If the timer runs out, you will DIE"]

#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------
def gameplay():

    window.bgcolor("black")
    loading = turtle
    loading.penup()
    random_tip = random.randint(0, 1)
    loading.goto(0, -110)
    loading.color("white")
    loading.write(game_loading_tips[random_tip], move=False, align="center", font=("Arial", 18, "bold"))
    loading.color("white")
    loading.shape("loading.gif")
    loading.goto(0,70)

    def create_maze(file=DEFAULT_TEXT_FILE):
        cell_maze = [[]]

        file_object = open(file, "r")
        row = 0
        for line in file_object:
            cell_list = line.split(" ")
            for cell in cell_list:
                cell_maze[row].append(cell.strip())
            row += 1
            new_list = []
            cell_maze.append(new_list)

        del cell_maze[len(cell_maze) - 1]
        file_object.close()

        return(cell_maze)

    #------------------------------------------------------------------------------------

    #counting variables
    monster_counter = 0
    wall_counter = 0
    empty_counter = 0
    treasure_counter = 0
    mtn = [0]
    wtn = [0]
    etn = [0]
    ttn = [0]
    tmtn = [0]

    for row in create_maze(file=DEFAULT_TEXT_FILE):
        for let in row:
            if let == "M":
                monster_counter += 1
                mtn.append(monster_counter)
                tmtn.append(monster_counter)
            elif let == "X":
                wall_counter += 1
                wtn.append(wall_counter)
            elif let == ".":
                empty_counter += 1
                etn.append(empty_counter)
            elif let == "T":
                treasure_counter += 1
                ttn.append(treasure_counter)

    empty_counter2 = monster_counter + treasure_counter + empty_counter
    for x in range(empty_counter, empty_counter2+1):
        etn.append(x)

    #-----------------------------------------------------------------------------------------

    #creating turtle objects

    mt = {}
    for x in range(monster_counter):
        mt[mtn[x]] = turtle.Turtle()

    wt = {}
    for x in range(wall_counter):
        wt[wtn[x]] = turtle.Turtle()

    et = {}
    for x in range(empty_counter2+1):
        et[etn[x]] = turtle.Turtle()

    tt = {}
    for x in range(treasure_counter):
        tt[ttn[x]] = turtle.Turtle()

    tmt = {}
    for x in range(monster_counter):
        tmt[mtn[x]] = turtle.Turtle()

    player = turtle.Turtle()


    #-----------------------------------------------------------------------------------------------

    #saving cords

    monster_dic = {}
    wall_dic = {}
    empty_dic = {}
    treasure_dic = {}



    #--------------------------------------------------------------------------------------------------

    grid = create_maze(MAZE_TEXT_FILE)

    #----------------------------------------------------------------------------------------------------

    #creating map
    window.tracer(False)
    mmn = 0
    wmn = 0
    emn = 0
    tmn = 0
    x = -170
    y = 170
    line_move_down = 0
    monster_namer = 1

    mmn = 0
    wmn = 0
    emn = 0
    tmn = 0
    x = -(len(grid[0]) * 33)//2
    y = (len(grid) * 33)//2
    line_move_down = 0
    monster_namer = 1
    loading.hideturtle()
    loading.clear()
    for row in create_maze(file=DEFAULT_TEXT_FILE):
            limit = len(row)
            for let in row:
                if let == "M":
                    et[emn].penup()
                    et[emn].goto(x, y)
                    et[emn].color("black")
                    et[emn].shape("turtle")
                    et[emn].hideturtle()
                    empty_dic[emn] = (et[emn].xcor(), et[emn].ycor())
                    emn += 1
                    mt[mmn].penup()
                    mt[mmn].goto(x, y)
                    mt[mmn].color("red")
                    mt[mmn].shape("MARIO.gif")
                    mt[mmn].turtlesize(1)
                    monster_dic[mmn] = (mt[mmn].xcor(), mt[mmn].ycor())
                    tmt[mmn].penup()
                    tmt[mmn].goto(x, y)
                    tmt[mmn].color("green")
                    tmt[mmn].shape("circle")
                    tmt[mmn].hideturtle()
                    monster_dic[mmn] = (mt[mmn].xcor(), mt[mmn].ycor())
                    mmn += 1
                elif let == "X":
                    wt[wmn].penup()
                    wt[wmn].goto(x, y)
                    wt[wmn].color("gray")
                    wt[wmn].shape("square")
                    wt[wmn].turtlesize(1)
                    wall_dic[wmn] = (wt[wmn].xcor(), wt[wmn].ycor())
                    wmn += 1
                if let == ".":
                    et[emn].penup()
                    et[emn].goto(x, y)
                    et[emn].color("black")
                    et[emn].shape("turtle")
                    et[emn].hideturtle()
                    empty_dic[emn] = (et[emn].xcor(), et[emn].ycor())
                    emn += 1
                elif let == "T":
                    et[emn].penup()
                    et[emn].goto(x, y)
                    et[emn].color("black")
                    et[emn].shape("turtle")
                    et[emn].hideturtle()
                    empty_dic[emn] = (et[emn].xcor(), et[emn].ycor())
                    emn += 1
                    tt[tmn].penup()
                    tt[tmn].goto(x, y)
                    tt[tmn].color("yellow")
                    tt[tmn].shape("triangle")
                    tt[tmn].turtlesize(1)
                    treasure_dic[tmn] = (tt[tmn].xcor(), tt[tmn].ycor())
                    tmn += 1
                elif let == "C":
                    player.penup()
                    player.goto(x, y)
                    player.color("blue")
                    player.shape("turtle")
                    player.turtlesize(1)
                x += 33
                line_move_down += 1
                while line_move_down == limit:
                    y -= 33
                    x = -(len(grid[0])*33)//2
                    line_move_down = 0


    #---------------------------------------------------------------------------------------
    global game_loop_active
    game_loop_active = True

    #functions for ending game

    def game_end(status):
        global game_loop_active
        pen = turtle.Turtle()
        window.tracer(0)
        pen.goto(0, 80)
        if status == "Game Over":
            game_loop_active = False
            winsound.PlaySound("Determination.wav", True)
            window.clear()
            window.bgcolor("black")
            lose_key = random.randint(0, len(game_end_list)-1)
            text = str(game_end_list[lose_key])
            pen.color("white")
            pen.hideturtle()
            pen.write(text, move=False, align="center", font=("Arial", 50, "normal"))
            pen.penup()
            pen.goto(70, 50)
            pen.fillcolor("green")
            pen.begin_fill()
            pen.goto(-70, 50)
            pen.goto(-70, -20)
            pen.goto(70, -20)
            pen.goto(70, 50)
            pen.end_fill()
            pen.goto(0, 0)
            pen.write("Try Again?", move=False, align="center", font=("Arial", 18, "bold"))
            pen.fillcolor("red")
            pen.goto(70, -40)
            pen.begin_fill()
            pen.goto(-70, -40)
            pen.goto(-70, -110)
            pen.goto(70, -110)
            pen.goto(70, -40)
            pen.end_fill()
            pen.goto(0, -90)
            pen.write("Main Menu", move=False, align="center", font=("Arial", 18, "bold"))

            def play_again1(x, y):
                if (-70 <= x <= 70) and (-20 < y < 50):
                    window.clear()
                    gameplay()

                elif (-70 <= x <= 70) and (-110 < y < -40):
                    window.clear()
                    window.onclick(start)
                    start_menu()

            window.onclick(play_again1)
        if status == "You Win":
            winsound.PlaySound("Victory Theme FF.wav", True)
            game_loop_active = False
            window.clear()
            window.bgcolor("black")
            win_key = random.randint(0, len(game_win_list) - 1)
            text = str(game_win_list[win_key])
            pen.color("white")
            pen.hideturtle()
            pen.write(text, move=False, align="center", font=("Arial", 50, "normal"))
            pen.penup()
            pen.goto(70, 50)
            pen.fillcolor("green")
            pen.begin_fill()
            pen.goto(-70, 50)
            pen.goto(-70, -20)
            pen.goto(70, -20)
            pen.goto(70, 50)
            pen.end_fill()
            pen.goto(0, 0)
            pen.write("Play Again?", move=False, align="center", font=("Arial", 18, "bold"))
            pen.goto(70, -40)
            pen.fillcolor("red")
            pen.begin_fill()
            pen.goto(-70, -40)
            pen.goto(-70, -110)
            pen.goto(70, -110)
            pen.goto(70, -40)
            pen.end_fill()
            pen.goto(0, -90)
            pen.write("Main Menu", move=False, align="center", font=("Arial", 18, "bold"))

            def play_again2(x, y):
                if (-70 <= x <= 70) and (-20 < y < 50):
                    window.clear()
                    gameplay()

                elif (-70 <= x <= 70) and (-110 < y < -40):
                    window.clear()
                    window.onclick(start)
                    start_menu()

            window.onclick(play_again2)


    #-------------------------------------------------------------------------------------

    #Monster movements


    def monster_movement():




        def monster_move_right():
            for y in range(empty_counter2):
                mycord = y
                if (xcord+33, ycord) == (et[mycord].xcor(), et[mycord].ycor()):
                    mt[x].setheading(0)
                    mt[x].goto(xcord+33, ycord)
        def monster_move_left():
            for y in range(empty_counter2):
                mycord = y
                if (xcord-33, ycord) == (et[mycord].xcor(), et[mycord].ycor()):
                    mt[x].setheading(180)
                    mt[x].goto(xcord-33, ycord)
        def monster_move_up():
            for y in range(empty_counter2):
                mycord = y
                if (xcord, ycord+33) == (et[mycord].xcor(), et[mycord].ycor()):
                    mt[x].setheading(90)
                    mt[x].goto(xcord, ycord+33)
        def monster_move_down():
            for y in range(empty_counter2):
                mycord = y
                if (xcord, ycord-33) == (et[mycord].xcor(), et[mycord].ycor()):
                    mt[x].setheading(270)
                    mt[x].goto(xcord, ycord-33)



        for x in range(monster_counter):
            xcord = int(mt[x].xcor())
            ycord = int(mt[x].ycor())
            key = random.randint(0, 3)
            if key == 0:
                monster_move_right()
            if key == 1:
                monster_move_left()
            if key == 2:
                monster_move_up()
            if key == 3:
                monster_move_down()


            if mt[x].pos() == player.pos():
                status = "Game Over"
                game_end(status)


    global movement_counter
    movement_counter = 0
    def monster_movement_final():
        global movement_counter
        movement_counter += 1
        if movement_counter > 30:
            monster_movement()
            movement_counter = 0



    #-------------------------------------------------------------------------------------

    #Player Movement
    global location_x
    global location_y
    global lx
    global ly
    global status
    global movement_tracker
    location_x = player.xcor()
    location_y = player.ycor()
    lx = float(location_x)
    ly = float(location_y)
    status = "test"
    movement_tracker = []



    #----------------------------------------------------------------------------------------
    def up():

        global game_loop_active
        if game_loop_active == True:
            global lx
            global ly
            # character spot-----------------------------------------------------
            if (location_x == lx) and (location_y == ly+33):
                player.setheading(90)
                player.goto(lx, ly+33)
                ly += 33
            # empty spot-----------------------------------------------------------
            for x in range(empty_counter2):
                if et[x].pos() == (lx, ly+33):
                    player.setheading(90)
                    player.goto(lx, ly + 33)
                    ly += 33
                    break
                else:
                    pass
            # monster spot-----------------------------------------------------------
            for x in range(monster_counter):
                if mt[x].pos() == (lx, ly):
                    global status
                    status = "Game Over"
                    game_end(status)
                    break
                else:
                    pass
            # treasure spot-------------------------------------------------------------
            for x in range(treasure_counter):
                if tt[x].pos() == (lx, ly):
                    status = "You Win"
                    game_end(status)
                    break
                else:
                    pass

    #----------------------------------------------------------------------------------------
    def down():
        global game_loop_active
        if game_loop_active == True:
            global lx
            global ly
            # character spot-----------------------------------------------------
            if (location_x == lx) and (location_y == ly-33):
                player.setheading(270)
                player.goto(lx, ly-33)
                ly -= 33
            # empty spot-----------------------------------------------------------
            for x in range(empty_counter2):
                if et[x].pos() == (lx, ly-33):
                    player.setheading(270)
                    player.goto(lx, ly-33)
                    ly -= 33
                    break
                else:
                    pass
            #monster spot-----------------------------------------------------------
            for x in range(monster_counter):
                if mt[x].pos() == (lx, ly):
                    global status
                    status = "Game Over"
                    game_end(status)
                    break
                else:
                    pass
            # treasure spot-------------------------------------------------------------
            for x in range(treasure_counter):
                if tt[x].pos() == (lx, ly):
                    status = "You Win"
                    game_end(status)
                    break
                else:
                    pass


    #----------------------------------------------------------------------------------------
    def right():
        global game_loop_active
        if game_loop_active == True:
            global lx
            global ly
            # character spot-----------------------------------------------------
            if (location_x == lx+33) and (location_y == ly):
                player.setheading(0)
                player.goto(lx+33, ly)
                lx += 33
            # empty spot-----------------------------------------------------------
            for x in range(empty_counter2):
                if et[x].pos() == (lx+33, ly):
                    player.setheading(0)
                    player.goto(lx + 33, ly)
                    lx += 33
                    break
                else:
                    pass
            # monster spot-----------------------------------------------------------
            for x in range(monster_counter):
                if mt[x].pos() == (lx, ly):
                    global status
                    status = "Game Over"
                    game_end(status)
                    break
                else:
                    pass
            # treasure spot-------------------------------------------------------------
            for x in range(treasure_counter):
                if tt[x].pos() == (lx, ly):
                    status = "You Win"
                    game_end(status)
                    break
                else:
                    pass


    #----------------------------------------------------------------------------------------
    def left():
        global game_loop_active
        if game_loop_active == True:
            global lx
            global ly
            #character spot-----------------------------------------------------
            if (location_x == lx-33) and (location_y == ly):
                player.setheading(180)
                player.goto(lx-33, ly)
                lx -= 33
            #empty spot-----------------------------------------------------------
            for x in range(empty_counter2):
                if et[x].pos() == (lx-33, ly):
                    player.setheading(180)
                    player.goto(lx - 33, ly)
                    lx -= 33
                    break
                else:
                    pass
            # monster spot-----------------------------------------------------------
            for x in range(monster_counter):
                if mt[x].pos() == (lx, ly):
                    global status
                    status = "Game Over"
                    game_end(status)
                    break
                else:
                    pass
            #treasure spot-------------------------------------------------------------
            for x in range(treasure_counter):
                if tt[x].pos() == (lx, ly):
                    status = "You Win"
                    game_end(status)
                    break
                else:
                    pass  



    def escape():
        window.clear()
        window.onclick(start)
        start_menu()




    global timer
    timer = 30
    def game_time():
        turtle.tracer(0)
        global timer
        ypos = (len(grid)*33//2)+10
        turtle.goto(0, ypos)
        #----------------------------------
        turtle.clear()
        turtle.write(str(timer), move=False, align="center", font=("Arial", 45, "bold"))
        timer -= 1
        if timer == -1:
            status = "Game Over"
            game_end(status)

        
    
    global timer_counter
    timer_counter = 0
    def game_time_final():
        global timer_counter
        timer_counter += 1
        if timer_counter > 250:
            game_time()
            timer_counter = 0














    random_key = random.randint(0, 1)
    winsound.PlaySound(game_playlist[random_key], True)


    window.listen()
    turtle.onkey(up, "w")
    turtle.onkey(down, "s")
    turtle.onkey(right, "d")
    turtle.onkey(left, "a")
    turtle.onkey(escape, "Escape")




    while game_loop_active == True:
        game_time_final()
        monster_movement_final()
        window.update()



def start_menu():
    window.title("Maze Runner by YOUR_NAME")
    window.bgcolor("black")
    window.setup(width=0.3, height=0.5)
    window.tracer(0)
    #------------------------------------
    turtle.goto(0, 70)
    turtle.color("white")
    turtle.write("Maze Runner", move=False, align="center", font=("Arial", 45, "bold"))
    turtle.fillcolor("green")
    turtle.penup()
    turtle.goto(70, 30)
    turtle.begin_fill()
    turtle.goto(70, -40)
    turtle.goto(-70, -40)
    turtle.goto(-70, 30)
    turtle.end_fill()
    turtle.goto(0, -30)
    turtle.write("START", move=False, align="center", font=("Arial", 30, "bold"))
    winsound.PlaySound("Zen Garden.wav", True)
    turtle.fillcolor("red")
    turtle.goto(70, -60)
    turtle.begin_fill()
    turtle.goto(-70, -60)
    turtle.goto(-70, -130)
    turtle.goto(70, -130)
    turtle.goto(70, -60)
    turtle.end_fill()
    turtle.goto(0, -120)
    turtle.write("Quit", move=False, align="center", font=("Arial", 30, "bold"))
    turtle.done()

    game_start = False

def start(x, y):
        if (-70 <= x <= 70) and (-40 < y < 30):
            window.clear()
            gameplay()

        elif (-70 <= x <= 70) and (-130 <= y <= -60):
            window.bye()

window.onclick(start)




start_menu()







