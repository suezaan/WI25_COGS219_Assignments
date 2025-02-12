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

valid_response_keys = ['r', 'o', 'y', 'g', 'b','q']

feedback_ic = visual.TextStim(win,text="Incorrect", height=30, color="black",pos=[0,0])
feedback_slow = visual.TextStim(win,text="Too slow", height=30, color="black",pos=[0,0])

trial_types = ['congruent', 'incongruent']

# incongruent trials
def make_incongruent(color):
    other_colors = [stimulus for stimulus in stimuli if stimulus != color]
    incongruent_color = random.choice(other_colors)
    return incongruent_color

while True:
    cur_word = random.choice(stimuli)
    trial_type = random.choice(trial_types)

    word_stim.setText(cur_word)
    if trial_type == 'congruent':
        cur_color = cur_word
    else:
        cur_color = make_incongruent(cur_word)
    word_stim.setColor(cur_color)

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
    key_pressed = event.waitKeys(keyList=valid_response_keys,maxWait=2) # set max wait time

    if not key_pressed: # too slow
        feedback_slow.draw()
        win.flip()
        core.wait(1)
    elif key_pressed[0] == cur_color[0]: # should response first letter of ink color (not a word)!
        pass
    elif key_pressed[0] == 'q':
        break
    else: 
        feedback_ic.draw()
        win.flip()
        core.wait(1)
    RTs.append(round(timer.getTime()*1000,0)) # rounded to the nearest milliseconds 


print(RTs) # printed RTs: [1059.0, 790.0, 809.0, 733.0, 787.0, 387.0]
 
