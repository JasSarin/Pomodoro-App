from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def resettimer():
    window.after_cancel(timer)
    canvas.itemconfig(timertext, text='00:00')
    timerlabel.config(text = 'Timer')
    checkmark.config(text= "")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def starttimer():
    global reps
    reps += 1
    worksec = WORK_MIN * 60
    shortbreak = SHORT_BREAK_MIN * 60
    longbreak = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(longbreak)
        timerlabel.config(text='Long Break', fg=RED)
    elif reps % 2 == 0:
        countdown(shortbreak)
        timerlabel.config(text='Short Break', fg=PINK)
    else:
        countdown(worksec)
        timerlabel.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    countmin = math.floor(count / 60)
    countsec = count % 60
    if countsec < 10:
        countsec = f'0{countsec}'
    canvas.itemconfig(timertext, text= f'{countmin}:{countsec}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        starttimer()
        if reps % 2 == 0:
            marks = ''
            worksessions = math.floor(reps / 2)
            for _ in range(worksessions):
                marks +='✅'
            checkmark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

timerlabel = Label(text = 'Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timerlabel.grid(row= 0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoimg = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image= tomatoimg)
timertext = canvas.create_text(100, 130, text= '00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row= 1, column=1)

startbutton = Button(text = 'Start', highlightthickness=0, command= starttimer)
startbutton.grid(row= 2, column=0)

resetbutton = Button(text = 'Reset', highlightthickness=0,  command= resettimer)
resetbutton.grid(row= 2, column=2)

checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

window.mainloop()