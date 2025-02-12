import time
import sys
import os
import random
from psychopy import visual,event,core,gui

stimuli = ['red', 'orange', 'yellow', 'green', 'blue']

win = visual.Window([800,600],color="gray", units='pix',checkTiming=False)
placeholder = visual.Rect(win,width=180,height=80, fillColor="lightgray",lineColor="black", lineWidth=6,pos=[0,0])
word_stim = visual.TextStim(win,text="", height=40, color="black",pos=[0,0])
instruction = visual.TextStim(win,text="Press the first letter of the ink color", height=20, color="black",pos=[0,-200],autoDraw=True) 
    # draw instruction for every window flip

# add fixation cross
fixation = visual.TextStim(win,text="+",color="black",height=15)

RTs = [] # store reaction time 
timer = core.Clock() # use psychopy times 
key_pressed=False # for key press

while True:
    cur_stim = random.choice(stimuli)
    valid_response_keys = cur_stim[0] # valid response keys for current stimuli

    word_stim.setText(cur_stim)
    word_stim.setColor(cur_stim)

    placeholder.draw()
    fixation.draw() # draw fixation
    win.flip()
    core.wait(.5)

    placeholder.draw()
    win.flip() # fixation disappear
    core.wait(.5)

    placeholder.draw()
    word_stim.draw() # color word appear 
    win.flip()

    timer.reset() # reset clock to measure RT after flip
    key_pressed = event.waitKeys(keyList=valid_response_keys)
    RTs.append(round(timer.getTime()*1000,0)) # rounded to the nearest milliseconds 

    if key_pressed[0] == 'q':
        break

print(RTs)
 
