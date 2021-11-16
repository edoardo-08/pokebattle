import ctypes
import sqlite3
import tkinter as tk

# Connect to database and create a cursor
db = sqlite3.connect("pokedex.db")
my_cursor = db.cursor()

# Make tkinter window better resolution
ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
root.title('Pokemon battle!')
root.geometry('800x400')

# Add background images
bg = tk.PhotoImage(file="pyproj/pokeball.png")
bg_label = tk.Label(root, image=bg)
bg_label.place(x=1, y=1, relwidth=0.94, relheight=1)

fightbg = tk.PhotoImage(file="pyproj/a4mrs3.png")

# Create title Label
title_label = tk.Label(root, text="All generation database",
                       font=("Helvetica", 16))
title_label.grid(row=0, column=2,)


# Create second window
def search_pokemon():
    search_pokemons = tk.Toplevel()

    search_pokemons.title("1v1 duel")
    search_pokemons.geometry("1080x720")

    fightbg_label = tk.Label(search_pokemons, image=fightbg)
    fightbg_label.place(x=1, y=1)

    def seach_now():

        searched = search_box.get()
        sql = "select name from pokemons where name like ? "
        name = ('%'+searched+'%',)
        result = my_cursor.execute(sql, name)
        result = my_cursor.fetchall()

        if not result:
            result = "Record Not Found..."

        searched_label = tk.Label(search_pokemons, text=result)
        searched_label.grid(row=2, column=0)

    def seach_now2():

        searched2 = search_box2.get()
        sql2 = "select name from pokemons where name like ? "
        name2 = ('%'+searched2+'%',)
        result2 = my_cursor.execute(sql2, name2)
        result2 = my_cursor.fetchall()

        if not result2:
            result2 = "Record Not Found..."

        searched_label2 = tk.Label(search_pokemons, text=result2)
        searched_label2.grid(row=2, column=2)

    def fight():

        player1 = search_box.get()
        player2 = search_box2.get()
        sql = "select total_points from pokemons where name like ?"
        sql2 = "select total_points from pokemons where name like ?"
        name = ('%' + player1 + '%',)
        name2 = ('%' + player2 + '%',)
        my_cursor.execute(sql, name)
        total_ponts1 = my_cursor.fetchall()
        my_cursor.execute(sql2, name2)
        total_ponts2 = my_cursor.fetchall()

        if total_ponts1 > total_ponts2:
            winner_label = tk.Label(search_pokemons, text='the winner is %s!' % player1)
            winner_label.grid(row=4, column=2)
        else:
            winner_label = tk.Label(search_pokemons, text='the winner is %s!' % player2)
            winner_label.grid(row=4, column=2)

    # Create entry box, label and button for selecting pokemon
    search_box = tk.Entry(search_pokemons)
    search_box.grid(row=0, column=1)
    search_box_label = tk.Label(search_pokemons, text="Select first fighter ")
    search_box_label.grid(row=0, column=0, padx=10, pady=10)
    search_button = tk.Button(search_pokemons,
                              text="Search Pokemon", command=seach_now)
    search_button.grid(row=1, column=0, padx=10)

    search_box2 = tk.Entry(search_pokemons)
    search_box2.grid(row=0, column=3)
    search_box_label2 = tk.Label(search_pokemons, text="Select second fighter ")
    search_box_label2.grid(row=0, column=2, padx=10, pady=10)
    search_button2 = tk.Button(search_pokemons,
                               text="Search Pokemon", command=seach_now2)
    search_button2.grid(row=1, column=2, padx=10)

    # Add fight button
    fight_button = tk.Button(search_pokemons,
                             text="Start Battle!", command=fight)

    fight_button.grid(row=3, column=2, pady=100)


# Add search Button,that will open a second window
search_pokemons_button = tk.Button(root, text="Search Pokemons",
                                   command=search_pokemon)
search_pokemons_button.grid(row=1, column=2, padx=300)


root.mainloop()
