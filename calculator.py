"""
Task-3
BMI Calculator
Made By : Krishna Chauhan
Date : 05.03.2024

"""
# Code:

from tkinter import *
from tkinter import messagebox

def reset_entry():
    age_tf.delete(0, 'end')
    height_tf.delete(0, 'end')
    weight_tf.delete(0, 'end')

def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get()) / 100
    bmi = kg / (m * m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('Result', f'BMI = {bmi} is Underweight')
    elif 18.5 < bmi < 24.9:
        messagebox.showinfo('Result', f'BMI = {bmi} is Normal')
    elif 24.9 < bmi < 29.9:
        messagebox.showinfo('Result', f'BMI = {bmi} is Overweight')
    elif bmi > 29.9:
        messagebox.showinfo('Result', f'BMI = {bmi} is Obesity')
    else:
        messagebox.showerror('Result', 'Something went wrong!')

ws = Tk()
ws.title('BMI Calculator')
ws.geometry('400x300')
ws.config(bg='#ADD8E6')


font_style = ('Georgia', 12)

var = IntVar()

frame = Frame(
    ws,
    padx=10,
    pady=10,
    bg='#ADD8E6'
)
frame.pack(expand=True)

age_lb = Label(
    frame,
    text="Enter Age",
    font=font_style,
    bg='#ADD8E6'
)
age_lb.grid(row=1, column=1)

age_tf = Entry(
    frame,
    font=font_style,
)
age_tf.grid(row=1, column=2, pady=5)

gen_lb = Label(
    frame,
    text='Select Gender',
    font=font_style,
    bg='#ADD8E6'
)
gen_lb.grid(row=2, column=1)

frame2 = Frame(
    frame,
    bg='#ADD8E6'
)
frame2.grid(row=2, column=2, pady=5)

male_rb = Radiobutton(
    frame2,
    text='Male',
    variable=var,
    value=1,
    font=font_style,
    bg='#ADD8E6'
)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(
    frame2,
    text='Female',
    variable=var,
    value=2,
    font=font_style,
    bg='#ADD8E6' 
)
female_rb.pack(side=RIGHT)

height_lb = Label(
    frame,
    text="Enter Height (cm)  ",
    font=font_style,
    bg='#ADD8E6'  
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Enter Weight (kg)  ",
    font=font_style,
    bg='#ADD8E6' 
)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
    font=font_style,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
    frame,
    font=font_style,
)
weight_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame,
    bg='#ADD8E6' 
)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(
    frame3,
    text='Calculate',
    command=calculate_bmi,
    font=font_style,
)
cal_btn.pack(side=LEFT)

reset_btn = Button(
    frame3,
    text='Reset',
    command=reset_entry,
    font=font_style,
)
reset_btn.pack(side=LEFT)

exit_btn = Button(
    frame3,
    text='Exit',
    command=lambda: ws.destroy(),
    font=font_style,
)
exit_btn.pack(side=RIGHT)

ws.mainloop()
