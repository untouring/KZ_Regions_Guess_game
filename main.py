import turtle
from turtle import Screen
import pandas
import pygame
import time

screen = Screen()
screen.title("KZ Regions Game")
screen.setup(1200, 900)
img = "kzmap.gif"
screen.addshape(img)

image = turtle.Turtle()

image.shape(img)

#def get_mouse_click_coor(x,y):
    #print(x, y)

#turtle.onscreenclick(get_mouse_click_coor)

#turtle.mainloop()

pygame.init()
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()
time.sleep(0.02)

seventeen_regions = pandas.read_csv('regions.csv')

all_regions = seventeen_regions.region.to_list()
guessed_regions = []

while len(guessed_regions) < 50:
    region_answer = turtle.textinput(title=f"{len(guessed_regions)}/Regions Correct",
                                     prompt="What's another region?").title()
    if region_answer == "Exit":
        missed_regions = []
        for state in all_regions:
            if state not in guessed_regions:
                missed_regions.append(state)
        print(missed_regions)
        #missing_regions = pandas.DataFrame(missed_states)
        #missing_regions.to_csv("states_to_learn.csv")
        break
    if region_answer in all_regions:
        guessed_regions.append(region_answer)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = seventeen_regions[seventeen_regions.region == region_answer]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(region_answer, font=("Verdana", 8, "bold"))



