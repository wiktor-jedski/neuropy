from tkinter import *
from playsound import playsound
from random import randint

FONT_NAME = "Courier"
TITLE_COLOR = '#00008B'
LEARNING_DELAY = 60
event = None
timer = None


def count_down(count):
    title_label.config(text=f'{count}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        done()


def sound_down(count):
    global timer
    if count > 0:
        timer = window.after(1000, sound_down, count - 1)
    else:
        flip = randint(0, 1)
        if flip:
            playsound('chord.mid')
        timer = window.after(1000, sound_down, LEARNING_DELAY)


def disable_buttons():
    alert_button['state'] = DISABLED
    focus_button['state'] = DISABLED
    learn_button['state'] = DISABLED


def enable_buttons():
    alert_button['state'] = NORMAL
    focus_button['state'] = NORMAL
    learn_button['state'] = NORMAL


def focus_routine():
    disable_buttons()
    global event
    event = Label()
    event.config(text='Focus on the plus below:'
                      '\n'
                      '\n'
                      '\n'
                      '          +             '
                      '\n'
                      '\n'
                      '\n'
                      '\n')
    event.grid(column=1, row=1)
    count_down(60)


def alert_routine():
    disable_buttons()
    global event
    event = Label()
    event.config(text='1. Get comfortable\n'
                      '2. 30-40 Deep Breaths\n'
                      '3. Inhale, Exhale, Hold\n'
                      '4. Big Breath, Hold for 15s, Let Go')
    event.grid(column=1, row=1)
    title_label.config(text='!')
    done_button.grid(column=1, row=3)


def learn_routine():
    disable_buttons()
    global event
    event = Label()
    event.config(text='When you hear the chord, stop learning for 10 seconds.')
    event.grid(column=1, row=1)
    title_label.config(text='Learning')
    done_button.grid(column=1, row=3)
    sound_down(LEARNING_DELAY)


def done():
    global event
    global timer
    title_label.config(text='Neuropy')
    if event:
        event.grid_remove()
        event = None
    window.after_cancel(timer)
    enable_buttons()
    done_button.grid_remove()


# window
window = Tk()
window.title('Neuropy')
window.config(padx=100, pady=50)

# labels
title_label = Label()
title_label.config(text='Neuropy', font=(FONT_NAME, 35, 'bold'), fg=TITLE_COLOR)
title_label.grid(column=1, row=0)

# buttons
alert_button = Button(text='Get Alert', highlightthickness=0, command=alert_routine)
alert_button.grid(column=0, row=2)

focus_button = Button(text='Get Focused', highlightthickness=0, command=focus_routine)
focus_button.grid(column=1, row=2)

learn_button = Button(text='Learn', highlightthickness=0, command=learn_routine)
learn_button.grid(column=2, row=2)

done_button = Button(text='Done!', highlightthickness=0, command=done)

if __name__ == '__main__':
    window.mainloop()
