import tkinter
import mysql.connector
from mysql.connector import errorcode
from tkinter import ttk
#initilization entities
global r
global e1
global e2
#connection to DB
global connection
global cursor
#display and selected element
global listbox
#gun
global var1
global list1
#shields
global var2
global list2
#grenade
global var3
global list3
#class
global var4
global list4
#relic
global var5
global list5
#search and character select
global previousSearch
global previousCharacter


def query():
    global listbox
    global previousSearch
    global previousCharacter
    global var1
    global list1
    global var2
    global list2
    global var3
    global list3
    global var4
    global list4
    global var5
    global list5
    global cursor
    print("search:", previousSearch)
    print("character:", previousCharacter)
    print(listbox.index(tkinter.ACTIVE))
    print("%d, %d, %d, %d, %d" % (var1.get(), var2.get(), var3.get(), var4.get(), var5.get()))
    if previousSearch != '. . .':
        print("Made it 1") #check if a command selected
        if previousSearch == 'Show All Items':
            listbox.delete(0, tkinter.END)
            listbox.insert(tkinter.END, "Name   :-:   Item Type   :-:   Damage Type   " +
                           ":-:   Rarity   :-:   Manufacturer")
            cursor.execute("SELECT gun_name, type, damage_type, rarity, manu_name FROM gun join" +
                           " manufacturer on gun.manu_id = manufacturer.manu_id")
            list1 = cursor.fetchall()
            for (name, item, damage, rarity, manu) in list1:
                listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                               "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
            cursor.execute("SELECT shield_name, item_type, damage_type, rarity, manu_name " +
                           "FROM shield join manufacturer on shield.manu_id = manufacturer.manu_id")
            list2 = cursor.fetchall()
            for (name, item, damage, rarity, manu) in list2:
                listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                               "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
            cursor.execute("SELECT grenade_name, item_type, damage_type, rarity, manu_name " +
                           "FROM grenade join manufacturer on grenade.manu_id = manufacturer.manu_id")
            list3 = cursor.fetchall()
            for (name, item, damage, rarity, manu) in list3:
                listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                               "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
            cursor.execute("SELECT mod_name, item_type, damage_type, rarity, manu_name " +
                           "FROM class_mod join manufacturer on class_mod.manu_id = manufacturer.manu_id")
            list4 = cursor.fetchall()
            for (name, item, damage, rarity, manu) in list4:
                listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                               "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
            cursor.execute("SELECT relic_name, item_type, damage_type, rarity, manu_name " +
                           "FROM relic join manufacturer on relic.manu_id = manufacturer.manu_id")
            list5 = cursor.fetchall()
            for (name, item, damage, rarity, manu) in list5:
                listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                               "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
        if previousCharacter != '. . .':
            print("Made it 2") # check if character selected
            if var1.get() == 1 or var2.get() == 1 or var3.get() == 1 or var4.get() == 1 or var5.get() == 1:
                print("Made it 3") # do we need to query?
                listbox.delete(0, tkinter.END)
                if previousSearch == 'Show Character Inventory':
                    print("Made it 4") #command ^ has been selected
                    listbox.insert(tkinter.END, "Name   :-:   Item Type   :-:   Damage Type   "+
                                   ":-:   Rarity   :-:   Manufacturer")
                    # Each Checkbox is checked
                    if var1.get() == 1:
                        # manipulate query for inventory join and character join
                        cursor.execute("SELECT gun_name, type, damage_type, rarity, manu_name FROM gun join"+
                        " manufacturer on gun.manu_id = manufacturer.manu_id")
                        list1 = cursor.fetchall()
                        for (name, item, damage, rarity, manu) in list1:
                            listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                            "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
                    if var2.get() == 1:
                        # manipulate query for inventory join and character join
                        cursor.execute("SELECT shield_name, item_type, damage_type, rarity, manu_name " +
                        "FROM shield join manufacturer on shield.manu_id = manufacturer.manu_id")
                        list2 = cursor.fetchall()
                        for (name, item, damage, rarity, manu) in list2:
                            listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                            "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
                    if var3.get() == 1:
                        # manipulate query for inventory join and character join
                        cursor.execute("SELECT grenade_name, item_type, damage_type, rarity, manu_name " +
                        "FROM grenade join manufacturer on grenade.manu_id = manufacturer.manu_id")
                        list3 = cursor.fetchall()
                        for (name, item, damage, rarity, manu) in list3:
                            listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                            "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
                    if var4.get() == 1:
                        # manipulate query for inventory join and character join
                        cursor.execute("SELECT mod_name, item_type, damage_type, rarity, manu_name " +
                                       "FROM class_mod join manufacturer on class_mod.manu_id = manufacturer.manu_id")
                        list4 = cursor.fetchall()
                        for (name, item, damage, rarity, manu) in list4:
                            listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                            "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
                    if var5.get() == 1:
                        # manipulate query for inventory join and character join
                        cursor.execute("SELECT relic_name, item_type, damage_type, rarity, manu_name " +
                                       "FROM relic join manufacturer on relic.manu_id = manufacturer.manu_id")
                        list5 = cursor.fetchall()
                        for (name, item, damage, rarity, manu) in list5:
                            listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                            "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))

def onSelectSearch(event=None):
    global previousSearch
    if event:
        previousSearch = event.widget.get()
    query()

def onSelectCharacter(event=None):
    global previousCharacter
    if event:
        previousCharacter = event.widget.get()
    query()


def initalize():
    global r
    global connection
    global cursor
    global listbox
    global previousSearch
    global previousCharacter
    global var1
    global var2
    global var3
    global var4
    global var5
    r.destroy()
    cursor = connection.cursor()
    previousSearch = '. . .'
    previousCharacter = '. . .'
    main = tkinter.Tk()
    main.title('BorderlandsDB User Interface')
    main.minsize(720, 580)
    #search commands '. . .' negates searches
    tkinter.Label(main, text='Search', relief=tkinter.RIDGE).grid(row=0, column=0)
    combo = ttk.Combobox(main, width=100, values=("Show Character Inventory", "Show All Items", "Show All Item Locations",
                                                  "Show All Things", "Do Something"))
    combo.set(". . .")
    combo.grid(row=1, columnspan=10, padx=30)
    combo.bind('<<ComboboxSelected>>', onSelectSearch)
    tkinter.Label(main, width=1).grid(row=2)
    tkinter.Label(main, text='Character', relief=tkinter.RIDGE).grid(row=3, column=2, columnspan=3)
    tkinter.Label(main, text='Type', relief=tkinter.RIDGE).grid(row=3, column=5, columnspan=3)
    #character select TODO make search for characters and list them
    combochar = ttk.Combobox(main, width=10, values=("Test Bandit", "Some Guy"))
    combochar.grid(row=4, column=2, columnspan=3, padx=30)
    combochar.set(". . .")
    combochar.bind('<<ComboboxSelected>>', onSelectCharacter)
    #list of checkboxes for scope of search
    var1 = tkinter.IntVar()
    tkinter.Checkbutton(main, text="Guns", variable=var1, anchor="w", command=query).\
        grid(row=4, column=6, columnspan=3, sticky="W")
    var2 = tkinter.IntVar()
    tkinter.Checkbutton(main, text="Shields", variable=var2, anchor="w", command=query).\
        grid(row=5, column=6, columnspan=3, sticky="W")
    var3 = tkinter.IntVar()
    tkinter.Checkbutton(main, text="Grenades", variable=var3, anchor="w", command=query).\
        grid(row=6, column=6, columnspan=3, sticky="W")
    var4 = tkinter.IntVar()
    tkinter.Checkbutton(main, text="Class Mods", variable=var4, anchor="w", command=query).\
        grid(row=7, column=6, columnspan=3, sticky="W")
    var5 = tkinter.IntVar()
    tkinter.Checkbutton(main, text="Relics", variable=var5, anchor="w", command=query).\
        grid(row=8, column=6, columnspan=3, sticky="W")
    # sets up listbox and mousewheel scroll capabilities
    tkinter.Label(main, width=1).grid(row=9)
    tkinter.Label(main, text='Results', relief=tkinter.RIDGE).grid(row=10)
    scrollbar = tkinter.Scrollbar(main)
    listbox = tkinter.Listbox(main, width=100, yscrollcommand=scrollbar.set)
    listbox.insert(tkinter.END, ". . .")
    for i in range(9):
        listbox.insert(tkinter.END, str(' '))
    listbox.grid(row=11, columnspan=10, rowspan=10, padx=30)
    scrollbar.config(command=listbox.yview)
    main.mainloop()

def login():
    global e1
    global e2
    global connection
    global r
    try:
        connection = mysql.connector.connect(
        host='ethan.cikeys.com',
        #user=e1.get(),
        #password=e2.get(),
        user='ethancik_charles',
        password='Borderlands2019!',
        database='ethancik_borderlands',
        auth_plugin='mysql_native_password')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text='user name or password is incorrect').pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text=err).pack()
            button = tkinter.Button(e, text='database does not exist', width=25, command=e.destroy)
            button.pack()
        else:
            e = tkinter.Tk()
            e.minsize(260, 40)
            e.title('Error')
            tkinter.Label(e, text=err).pack()
            button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
            button.pack()
    else:
        initalize()

def start():
    global r
    r = tkinter.Tk()
    r.title('Borderlands Database Login')
    r.minsize(260, 100)
    tkinter.Label(r, text='user').grid(row=0)
    tkinter.Label(r, text='password').grid(row=1)
    global e1
    global e2
    e1 = tkinter.Entry(r)
    e2 = tkinter.Entry(r)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    tkinter.Button(r, text='Login', command=login).grid(row=3, column=1)
    r.mainloop()

start()
