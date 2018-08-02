from tkinter import *

# player 1 life
def p1_plus_10_life():
    try:
        life = int(p1_life.get())
        p1_life.set(life + 10)
    except ValueError:
        print('ValueError')


def p1_plus_1_life():
    try:
        life = int(p1_life.get())
        p1_life.set(life + 1)
    except ValueError:
        print('ValueError')


def p1_minus_10_life():
    try:
        life = int(p1_life.get())
        p1_life.set(life - 10)
    except ValueError:
        print('ValueError')


def p1_minus_1_life():
    try:
        life = int(p1_life.get())
        p1_life.set(life - 1)
    except ValueError:
        print('ValueError')

# player 1 poison
def p1_plus_5_poison():
    try:
        poison = int(p1_poison.get())
        p1_poison.set(poison + 5)
    except ValueError:
        print('ValueError')


def p1_plus_1_poison():
    try:
        poison = int(p1_poison.get())
        p1_poison.set(poison + 1)
    except ValueError:
        print('ValueError')


def p1_minus_5_poison():
    try:
        poison = int(p1_poison.get())
        p1_poison.set(poison - 5)
    except ValueError:
        print('ValueError')


def p1_minus_1_poison():
    try:
        poison = int(p1_poison.get())
        p1_poison.set(poison - 1)
    except ValueError:
        print('ValueError')



# player 2 life
def p2_plus_10_life():
    try:
        life = int(p2_life.get())
        p2_life.set(life + 10)
    except ValueError:
        print('ValueError')


def p2_plus_1_life():
    try:
        life = int(p2_life.get())
        p2_life.set(life + 1)
    except ValueError:
        print('ValueError')


def p2_minus_10_life():
    try:
        life = int(p2_life.get())
        p2_life.set(life - 10)
    except ValueError:
        print('ValueError')


def p2_minus_1_life():
    try:
        life = int(p2_life.get())
        p2_life.set(life - 1)
    except ValueError:
        print('ValueError')


# player 2 poison
def p2_plus_5_poison():
    try:
        poison = int(p2_poison.get())
        p2_poison.set(poison + 5)
    except ValueError:
        print('ValueError')


def p2_plus_1_poison():
    try:
        poison = int(p2_poison.get())
        p2_poison.set(poison + 1)
    except ValueError:
        print('ValueError')


def p2_minus_5_poison():
    try:
        poison = int(p2_poison.get())
        p2_poison.set(poison - 5)
    except ValueError:
        print('ValueError')


def p2_minus_1_poison():
    try:
        poison = int(p2_poison.get())
        p2_poison.set(poison - 1)
    except ValueError:
        print('ValueError')




# main window
my_window = Tk()
my_window.title('Life/Poison MTG')

# variables
p1_life = StringVar()
p1_life.set(20)
p1_poison = StringVar()
p1_poison.set(0)
p2_life = StringVar()
p2_life.set(20)
p2_poison = StringVar()
p2_poison.set(0)

# labels 2 colunas
label_player_1 = Label(my_window, text='Player 1')
label_player_2 = Label(my_window, text='Player 2')
label_player_1_PV = Label(my_window, text='PV buttons')
label_player_2_PV = Label(my_window, text='PV buttons')
label_player_1_poison = Label(my_window, text='Poison buttons')
label_player_2_poison = Label(my_window, text='Poison buttons')

# labels 1 columna
label_p1_pv_actual = Label(my_window, text='PV')
label_p1_poison_actual = Label(my_window, text='Poison')
label_p2_pv_actual = Label(my_window, text='PV')
label_p2_poison_actual = Label(my_window, text='Poison')

# labels con textvariable
label_p1_display_pv = Label(my_window, textvariable=p1_life)
label_p1_display_poison = Label(my_window, textvariable=p1_poison)
label_p2_display_pv = Label(my_window, textvariable=p2_life)
label_p2_display_poison = Label(my_window, textvariable=p2_poison)

# buttons player 1 life
button_p1_plus_10_life = Button(my_window, text='+10', command=p1_plus_10_life)
button_p1_plus_1_life = Button(my_window, text='+1', command=p1_plus_1_life)
button_p1_minus_10_life = Button(my_window, text='-10', command=p1_minus_10_life)
button_p1_minus_1_life = Button(my_window, text='-1', command=p1_minus_1_life)

# buttons player 1 poison
button_p1_plus_5_poison = Button(my_window, text='+5', command=p1_plus_5_poison)
button_p1_plus_1_poison = Button(my_window, text='+1', command=p1_plus_1_poison)
button_p1_minus_5_poison = Button(my_window, text='-5', command=p1_minus_5_poison)
button_p1_minus_1_poison = Button(my_window, text='-1', command=p1_minus_1_poison)

# buttons player 2 life
button_p2_plus_10_life = Button(my_window, text='+10', command=p2_plus_10_life)
button_p2_plus_1_life = Button(my_window, text='+1', command=p2_plus_1_life)
button_p2_minus_10_life = Button(my_window, text='-10', command=p2_minus_10_life)
button_p2_minus_1_life = Button(my_window, text='-1', command=p2_minus_1_life)

# buttons player 2 poison
button_p2_plus_5_poison = Button(my_window, text='+5', command=p2_plus_5_poison)
button_p2_plus_1_poison = Button(my_window, text='+1', command=p2_plus_1_poison)
button_p2_minus_5_poison = Button(my_window, text='-5', command=p2_minus_5_poison)
button_p2_minus_1_poison = Button(my_window, text='-1', command=p2_minus_1_poison)

# grid
# row 0:
label_player_1.grid(row=0, column=0, columnspan=2)
label_player_2.grid(row=0, column=2, columnspan=2)

# row 1:
label_p1_pv_actual.grid(row=1, column=0)
label_p1_display_pv.grid(row=1, column=1)
label_p2_pv_actual.grid(row=1, column=2)
label_p2_display_pv.grid(row=1, column=3)

# row 2:
label_p1_poison_actual.grid(row=2, column=0)
label_p1_display_poison.grid(row=2, column=1)
label_p2_poison_actual.grid(row=2, column=2)
label_p2_display_poison.grid(row=2, column=3)

# row 3:
label_player_1_PV.grid(row=3, column=0, columnspan=2)
label_player_2_PV.grid(row=3, column=2, columnspan=2)

# row 4:
button_p1_plus_10_life.grid(row=4, column=0)
button_p1_plus_1_life.grid(row=4, column=1)
button_p2_plus_10_life.grid(row=4, column=2)
button_p2_plus_1_life.grid(row=4, column=3)

# row 5:
button_p1_minus_10_life.grid(row=5, column=0)
button_p1_minus_1_life.grid(row=5, column=1)
button_p2_minus_10_life.grid(row=5, column=2)
button_p2_minus_1_life.grid(row=5, column=3)

# row 6:
label_player_1_poison.grid(row=6, column=0, columnspan=2)
label_player_2_poison.grid(row=6, column=2, columnspan=2)

# row 7:
button_p1_plus_5_poison.grid(row=7, column=0)
button_p1_plus_1_poison.grid(row=7, column=1)
button_p2_plus_5_poison.grid(row=7, column=2)
button_p2_plus_1_poison.grid(row=7, column=3)

# row 8:
button_p1_minus_5_poison.grid(row=8, column=0)
button_p1_minus_1_poison.grid(row=8, column=1)
button_p2_minus_5_poison.grid(row=8, column=2)
button_p2_minus_1_poison.grid(row=8, column=3)

# main loop
my_window.mainloop()






