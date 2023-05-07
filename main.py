
import os
from turtle import *
import turtle as tr
import time
import random as rnd
import pygame
import math


def go_up():
    head.setheading(90)

def go_down():
    head.setheading(270)
def go_right():
    head.setheading(0)

def go_left():
    head.setheading(180)
def getout():
	tr.bye()
def popup_food():
    min_distance = 200  # Minimum distance between food and player
    
    while True:
        x = rnd.randint(-300, 310)
        y = rnd.randint(-263, 263)
        
        # Calculate distance between food and player
        dx = x - head.xcor()
        dy = y - head.ycor()
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance >= min_distance:
            break  # Exit the loop if the distance is acceptable
    
    food.goto(x, y)
    foodpos[0] = x
    foodpos[1] = y
    print(foodpos[0], foodpos[1])
    food.showturtle()


def check(count):
	sound = pygame.mixer.Sound(popup_path)
	headpos[0] = head.xcor()
	headpos[1] = head.ycor()
	foodpos[0] = food.xcor()
	foodpos[1] = food.ycor()
	dx = headpos[0] - foodpos[0]
	dy = headpos[1] - foodpos[1]
	distance = math.sqrt(dx*dx + dy*dy)
	if distance <= (150/4 + 50/2):
		channel1.play(sound)
		count += 1
		popup_food()
		score.clear()
		score.write("Score: {}".format(count), align='left', font=('Arial', 20, 'normal'))
	return count
def checkpos():

	if head.xcor()<-300:
		head.ht()
		head.speed(0)
		head.goto(312, head.ycor())
		head.st()
		head.speed(1)
		head.forward(15)
	if 310 < head.xcor():
		head.ht()
		head.speed(0)
		head.goto(-302, head.ycor())
		head.st()
		head.speed(1)		
	if head.ycor()<-263:
		head.ht()
		head.speed(0)
		head.goto(head.xcor(), 261)
		head.st()
		head.speed(1)
	if head.ycor()>263:
		head.ht()		
		head.speed(0)
		head.goto(head.xcor(), -265)
		head.st()
		head.speed(1)
		
def main(x,y):
	sound1=pygame.mixer.Sound(song_path)
	channel0.play(sound1,loops=-1)
	count=0
	head.hideturtle()
	time.sleep(0.2)
	head.showturtle()
	
	while True:	
		onkey(go_up,"Up")
		onkey(go_down,"Down")
		onkey(go_left,"Left")
		onkey(go_right,"Right")
		onkey(getout,"f")
		head.forward(15)
		count=check(count)
		checkpos()
		listen()
		if count ==10:
			break
	score.clear()
	score.goto(-320,0)
	score.color("white")
	score.write("Dear Carla, \nYou finished the game but my love for you never ends!\nHappy birthday! I love you so much, you're my treasure\n33 years of pure cuteness :) \nForever yours,\nFelipe " ,align='left', font=('Arial', 20, 'normal'))
	
		




script_dir = os.path.dirname(__file__)
bg_image_path = os.path.join(script_dir, 'imgs','Background.gif')
food_image_path = os.path.join(script_dir, 'imgs','cake.gif')
head_image_path = os.path.join(script_dir, 'imgs','player.gif')

song_path = os.path.join(script_dir, 'soundtrack','StardewValley.mp3')
popup_path = os.path.join(script_dir, 'soundtrack','popup.mp3')

tr.Screen().bgpic(bg_image_path)

pygame.init()
pygame.mixer.init()
channel0=pygame.mixer.Channel(0)
channel1=pygame.mixer.Channel(1)


tr.title('Happy birthday, Carla! <3')
tr.screensize(600,547)
screen = tr.Screen()
screen.bgcolor("black")
tr.hideturtle()
begin_fill()

score=tr.Turtle()
score.hideturtle()
score.pu()
score.goto(-250,220)
score.color("white")
score.write("Score:{}" .format(0), align=('left'),font=('arial',16,'normal'))

head = tr.Turtle()
food=tr.Turtle()
headpos=[0,0]
foodpos=[0,0]

screen.addshape(head_image_path)
head.shape(head_image_path)
head.pu()
head.speed(1)

screen.addshape(food_image_path)
food.hideturtle()
food.speed(0)
food.pu()
food.shape(food_image_path)
food.penup()
food.hideturtle()
food.shapesize(0.8, 0.8)

listen()
onscreenclick(main,1)
popup_food()

food.showturtle()
end_fill()

mainloop()
