from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
checkmark_string = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global checkmark_string
    checkmark_string = ""
    timer_label.config(fg=GREEN)
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmarks_label.config(text=checkmark_string)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global checkmark_string
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        countdown(work_sec)
        timer_label.config(fg=GREEN, text="Work")
    elif reps == 8:
        checkmarks_label.config(text=checkmark_string)
        countdown(long_break_sec)
        timer_label.config(fg=RED, text="Long brake")
    else:
        checkmarks_label.config(text=checkmark_string)
        countdown(short_break_sec)
        timer_label.config(fg=PINK, text="Short brake")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global timer
    global checkmark_string
    min_left = math.floor(count / 60)
    sec_left = count % 60
    if sec_left < 10:
        sec_left = f"0{sec_left}"

    canvas.itemconfig(timer_text, text=f"{min_left}:{sec_left}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        if reps % 2 == 1:
            checkmark_string += "✔"
        elif reps == 8:
            reset_timer()
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer")
timer_label.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

checkmarks_label = Label()
checkmarks_label.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checkmarks_label.grid(column=1, row=3)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()
