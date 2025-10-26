from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer=None
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
   if timer:
    window.after_cancel(timer)
    canvas.itemconfig(text_label,text="00:00")
    my_label.config(text='timer')
    check_marks.config(text='')
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        s_timer(long_break_sec)
        my_label.config(text="Long Break", fg=RED)

    elif reps % 2 == 0:
        s_timer(short_break_sec)
        my_label.config(text="Long Break", fg=PINK)
    else:
        s_timer(work_sec)
        my_label.config(text='WORK',fg=GREEN)
   


def s_timer(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(text_label, text=f"{count_min}:{count_sec}")

    

    if count > 0:
      timer= window.after(1000, s_timer, count - 1)
    else:
        start_timer()

        check=""
        check_resoures=math.floor(reps/2)
        for _ in range(check_resoures):
            check+='✓'

            check_marks.config(text=check)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title('pomodoro')
window.config(padx=100,pady=50,bg=YELLOW)
my_label=Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,40,'bold'))
my_label.grid(row=0,column=1)


    
butto=Button(text='Start',highlightthickness=0,command=start_timer)
butto.grid(row=2,column=0)

butto=Button(text='Reset',highlightthickness=0,command=reset_timer)
butto.grid(row=2,column=2)

check_marks= Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,'bold'))
check_marks.grid(row=3,column=1)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_img)

text_label = canvas.create_text(100, 112, text="00:00", fill="white", font=("Arial", 35, "bold"))

canvas.grid(row=1,column=1)

window.mainloop()