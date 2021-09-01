import random
import tkinter as tk

window = tk.Tk()
window.title("Dungeons and Dice")
window.geometry("400x300")


dice = 0


def dice_logic(dice_selected):
    output = f"{dice} \n"
    text_area.insert(tk.END, output)


def d100():
    global dice
    dice = random.randint(1, 100)
    dice_logic(dice)


def d20():
    global dice
    yeet = ""
    dice = random.randint(1, 20)
    if dice == 20:
        yeet = "CRIT!!"
        return yeet
    elif dice == 1:
        yeet == "WOMP WOMP"
        return yeet
    dice_logic(dice)


def d12():
    global dice
    dice = random.randint(1, 12)
    dice_logic(dice)


def d10():
    global dice
    dice = random.randint(1, 10)
    dice_logic(dice)


def d8():
    global dice
    dice = random.randint(1, 8)
    dice_logic(dice)


def d6():
    global dice
    dice = random.randint(1, 6)
    dice_logic(dice)


def d4():
    global dice
    dice = random.randint(1, 4)
    dice_logic(dice)


def clear_text():
    text_area.delete("1.0", "end")


buttonD100 = tk.Button(text="D100", command=d100)
buttonD100.grid(column=0, row=1)

buttonD20 = tk.Button(text="D20", command=d20)
buttonD20.grid(column=1, row=1)

buttonD12 = tk.Button(text="D12", command=d12)
buttonD12.grid(column=2, row=1)

buttonD10 = tk.Button(text="D10", command=d10)
buttonD10.grid(column=0, row=2)

buttonD8 = tk.Button(text="D8", command=d8)
buttonD8.grid(column=1, row=2)

buttonD6 = tk.Button(text="D6", command=d6)
buttonD6.grid(column=2, row=2)

buttonD4 = tk.Button(text="D4", command=d4)
buttonD4.grid(column=0, row=3)

clear_button = tk.Button(text="Clear", command=clear_text)
clear_button.grid(column=1, row=3)

text_area = tk.Text(master=window, height=12, width=30, bg="#F6F8E1")
text_area.grid(column=1, row=4)

output = ''

text_area.insert(tk.END, output)
window.mainloop()
