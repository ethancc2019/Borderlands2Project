import tkinter
import mysql.connector
from mysql.connector import errorcode
from tkinter import ttk
#initilization entities
global r
global e1
global e2
global e
global user
global characters
global main
#connection to DB
global connection
global cursor
#display and selected element
global listbox
#gun
global list1
global gunAR
global gunPistol
global gunRocket
global gunShotgun
global gunSMG
global gunSniper
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
global previousPreviousSearch
global previousPreviousCharacter
#currency
global money
global keys
global eridium
#ammo
global ammo1
global ammo2
global ammo3
global ammo4
global ammo5
global ammo6
global ammo7
#variables to create
global u
global a
global v
#insert
inventory = ("INSERT INTO inventory "
             "(user_id, hunter_id, gun_id, shield, class_mod, relic, grenade_mod) "
             "VALUES (%s,%s,%s,%s,%s,%s,%s)"
             )
charInsert = ("INSERT INTO vault_hunter "
             "(user_id, class, level, name)"
             "VALUES (%s,%s,%s,%s)"
             )
#additional ui
global confirm
global confirm2
global k1
global k2
global k3
global k4
def errorbox(title, content):
    e = tkinter.Tk()
    e.minsize(260, 40)
    e.title(title)
    tkinter.Label(e, text=content).pack()
    button = tkinter.Button(e, text='Okay', width=25, command=e.destroy)
    button.pack()

def query():
    global listbox
    global previousSearch
    global previousCharacter
    global previousPreviousSearch
    global previousPreviousCharacter
    global gunAR
    global gunPistol
    global gunRocket
    global gunShotgun
    global gunSMG
    global gunSniper
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
    global e1
    global user
    print("search:", previousSearch)
    print("character:", previousCharacter)
    print(listbox.index(tkinter.ACTIVE))
    print("%d, %d, %d, %d" % ( var2.get(), var3.get(), var4.get(), var5.get()))
    if previousSearch != '. . .': # does not operate if no command
        #first check all general things
        #show all items
        if previousSearch == 'Show All Items(Ignore Checkboxes)' and previousPreviousSearch != previousSearch:
            previousPreviousSearch = 'Show All Items(Ignore Checkboxes)'
            listbox.delete(0, tkinter.END)
            listbox.insert(tkinter.END, "Name   :-:   Item Type   :-:   Damage Type   " +
                           ":-:   Rarity   :-:   Manufacturer")
            cursor.execute("SELECT gun_id, gun_name, type, damage_type, rarity, manu_name FROM gun join" +
                           " manufacturer on gun.manu_id = manufacturer.manu_id")
            list1 = cursor.fetchall()
            for (ident, name, item, damage, rarity, manu) in list1:
                listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                               "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
            cursor.execute("SELECT shield_id, shield_name, item_type, damage_type, rarity, manu_name " +
                           "FROM shield join manufacturer on shield.manu_id = manufacturer.manu_id")
            list2 = cursor.fetchall()
            for (ident, name, item, damage, rarity, manu) in list2:
                listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                               "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
            cursor.execute("SELECT grenade_id, grenade_name, item_type, damage_type, rarity, manu_name " +
                           "FROM grenade join manufacturer on grenade.manu_id = manufacturer.manu_id")
            list3 = cursor.fetchall()
            for (ident, name, item, damage, rarity, manu) in list3:
                listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                               "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
            cursor.execute("SELECT mod_id, mod_name, item_type, damage_type, rarity, manu_name " +
                           "FROM class_mod join manufacturer on class_mod.manu_id = manufacturer.manu_id")
            list4 = cursor.fetchall()
            for (ident, name, item, damage, rarity, manu) in list4:
                listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                               "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
            cursor.execute("SELECT relic_id, relic_name, item_type, damage_type, rarity, manu_name " +
                           "FROM relic join manufacturer on relic.manu_id = manufacturer.manu_id")
            list5 = cursor.fetchall()
            for (ident, name, item, damage, rarity, manu) in list5:
                listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                               "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
        if previousSearch == 'Show All Items':
            previousPreviousSearch = 'Show All Items'
            if (var2.get() == 1 or var3.get() == 1 or var4.get() == 1 or var5.get() == 1 or gunAR.get() == 1 or
            gunSMG.get() == 1 or gunShotgun.get() == 1 or gunSniper.get() == 1 or gunPistol.get() == 1 or
            gunRocket.get() == 1):
                    listbox.delete(0, tkinter.END)
                    listbox.insert(tkinter.END, "Name   :-:   Item Type   :-:   Damage Type   " +
                                   ":-:   Rarity   :-:   Manufacturer")
                    list1 = None
                    if gunAR.get() == 1:
                        cursor.execute("SELECT gun_id, gun_name, type, damage_type, rarity, manu_name FROM gun join" +
                                       " manufacturer on gun.manu_id = manufacturer.manu_id where type = "+
                                       "'Assault Rifle'")
                        if list1 is not None:
                            list1.extend(cursor.fetchall())
                        else:
                            list1 = cursor.fetchall()
                    if gunSMG.get() == 1:
                        cursor.execute("SELECT gun_id, gun_name, type, damage_type, rarity, manu_name FROM gun join" +
                                       " manufacturer on gun.manu_id = manufacturer.manu_id where type =" +
                                       "'Submachine Gun'")
                        if list1 is not None:
                            list1.extend(cursor.fetchall())
                        else:
                            list1 = cursor.fetchall()
                    if gunPistol.get() == 1:
                        cursor.execute("SELECT gun_id, gun_name, type, damage_type, rarity, manu_name FROM gun join" +
                                       " manufacturer on gun.manu_id = manufacturer.manu_id where type =" +
                                       " 'Pistol'")
                        if list1 is not None:
                            list1.extend(cursor.fetchall())
                        else:
                            list1 = cursor.fetchall()
                    if gunShotgun.get() == 1:
                        cursor.execute("SELECT gun_id, gun_name, type, damage_type, rarity, manu_name FROM gun join" +
                                       " manufacturer on gun.manu_id = manufacturer.manu_id where type = " +
                                       "'Shotgun'")
                        if list1 is not None:
                            list1.extend(cursor.fetchall())
                        else:
                            list1 = cursor.fetchall()
                    if gunSniper.get() == 1:
                        cursor.execute("SELECT gun_id, gun_name, type, damage_type, rarity, manu_name FROM gun join" +
                                       " manufacturer on gun.manu_id = manufacturer.manu_id where type =" +
                                       " 'Sniper Rifle'")
                        if list1 is not None:
                            list1.extend(cursor.fetchall())
                        else:
                            list1 = cursor.fetchall()
                    if gunRocket.get() == 1:
                        cursor.execute("SELECT gun_id, gun_name, type, damage_type, rarity, manu_name FROM gun join" +
                                       " manufacturer on gun.manu_id = manufacturer.manu_id where type =" +
                                       "'Rocket Launcher'")
                        if list1 is not None:
                            list1.extend(cursor.fetchall())
                        else:
                            list1 = cursor.fetchall()
                    if list1 is not None:
                        for (ident, name, item, damage, rarity, manu) in list1:
                            listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                            "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
                    # Each Checkbox is checked
                    if var2.get() == 1:
                        cursor.execute("SELECT shield_id, shield_name, item_type, damage_type, rarity, manu_name " +
                        "FROM shield join manufacturer on shield.manu_id = manufacturer.manu_id")
                        list2 = cursor.fetchall()
                        for (ident, name, item, damage, rarity, manu) in list2:
                            listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                            "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
                    if var3.get() == 1:
                        cursor.execute("SELECT grenade_id, grenade_name, item_type, damage_type, rarity, manu_name " +
                        "FROM grenade join manufacturer on grenade.manu_id = manufacturer.manu_id")
                        list3 = cursor.fetchall()
                        for (ident, name, item, damage, rarity, manu) in list3:
                            listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                            "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
                    if var4.get() == 1:
                        cursor.execute("SELECT mod_id, mod_name, item_type, damage_type, rarity, manu_name " +
                                       "FROM class_mod join manufacturer on class_mod.manu_id = manufacturer.manu_id")
                        list4 = cursor.fetchall()
                        for (ident, name, item, damage, rarity, manu) in list4:
                            listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                            "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
                    if var5.get() == 1:
                        cursor.execute("SELECT relic_id, relic_name, item_type, damage_type, rarity, manu_name " +
                                       "FROM relic join manufacturer on relic.manu_id = manufacturer.manu_id")
                        list5 = cursor.fetchall()
                        for (ident, name, item, damage, rarity, manu) in list5:
                            listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                            "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
            else:
                if previousSearch == 'Show Character Inventory' or previousSearch == 'Show All Items':
                    listbox.delete(0, tkinter.END)
        if previousSearch == 'Show All Item Locations' and previousPreviousSearch != previousSearch:
            #USE SP
            previousPreviousSearch = previousSearch
        if previousCharacter != '. . .': # check if character selected
            #all possibilities
            if previousSearch == "Show Current Character Stats and Badass":
                previousPreviousSearch = previousSearch
                listbox.delete(0, tkinter.END)
                cursor.execute("SELECT * from vault_hunter join user on vault_hunter.user_id = user.user_id where username = \'" +
                    e1 + "\' and name = \'" + previousCharacter + "\'")
                character = cursor.fetchall()
                listbox.insert(tkinter.END, "User: " + user[0][1])
                listbox.insert(tkinter.END, "Name: " + character[0][4])
                listbox.insert(tkinter.END, "Class: " + character[0][2])
                listbox.insert(tkinter.END, "Level: " + str(character[0][3]))
                cursor.execute("SELECT * from badass_rank where user_id = \'" +
                    str(user[0][0]) + "\'")
                character = cursor.fetchall()
                listbox.insert(tkinter.END, "Badass Level: " + str(character[0][1]))
                listbox.insert(tkinter.END, "Health Increase %: " + str(character[0][2]))
                listbox.insert(tkinter.END, "Shield Increase %: " + str(character[0][3]))
                listbox.insert(tkinter.END, "Shield Recharge Delay: " + str(character[0][4]))
                listbox.insert(tkinter.END, "Shield Recharge Rate: " + str(character[0][5]))
                listbox.insert(tkinter.END, "Melee Damage: " + str(character[0][6]))
                listbox.insert(tkinter.END, "Grenade Damage: " + str(character[0][7]))
                listbox.insert(tkinter.END, "Gun Accuracy: " + str(character[0][8]))
                listbox.insert(tkinter.END, "Gun Damage: " + str(character[0][9]))
                listbox.insert(tkinter.END, "Fire Rate: " + str(character[0][10]))
                listbox.insert(tkinter.END, "Recoil Reduction: " + str(character[0][11]))
                listbox.insert(tkinter.END, "Reload Speed: " + str(character[0][12]))
                listbox.insert(tkinter.END, "Elemental Effect Chance: " + str(character[0][13]))
                listbox.insert(tkinter.END, "Elemental Effect Damage: " + str(character[0][14]))
                listbox.insert(tkinter.END, "Critical Hit Chance: " + str(character[0][15]))
            if (var2.get() == 1 or var3.get() == 1 or var4.get() == 1 or var5.get() == 1 or gunAR.get() == 1 or
            gunSMG.get() == 1 or gunShotgun.get() == 1 or gunSniper.get() == 1 or gunPistol.get() == 1 or
            gunRocket.get() == 1):
                if previousSearch == 'Show Character Inventory':
                    cursor.execute(
                        "SELECT hunter_id, vault_hunter.user_id from vault_hunter join user on "
                        "vault_hunter.user_id = user.user_id where username = \'" + e1 + "\' and name = \'" +
                         previousCharacter + "\'")
                    character = cursor.fetchall()
                    listbox.delete(0, tkinter.END)
                    listbox.insert(tkinter.END, "Name   :-:   Item Type   :-:   Damage Type   " +
                                   ":-:   Rarity   :-:   Manufacturer")
                    list1 = None
                    if gunAR.get() == 1:
                        cursor.execute("SELECT gun.gun_id, gun_name, type, damage_type, rarity, manu_name FROM gun join"
                                       + " manufacturer on gun.manu_id = manufacturer.manu_id join inventory on" +
                                       " inventory.gun_id = gun.gun_id where hunter_id = "+ str(character[0][0]) +
                                       " and user_id = " + str(character[0][1]) +" and type = 'Assault Rifle'")
                        if list1 is not None:
                            list1.extend(cursor.fetchall())
                        else:
                            list1 = cursor.fetchall()
                    if gunSMG.get() == 1:
                        cursor.execute("SELECT gun.gun_id, gun_name, type, damage_type, rarity, manu_name FROM gun join"
                                       +" manufacturer on gun.manu_id = manufacturer.manu_id join inventory on" +
                                       " inventory.gun_id = gun.gun_id where hunter_id = "+ str(character[0][0]) +
                                       " and inventory.user_id = " + str(character[0][1]) +
                                       " and type ='Submachine Gun'")
                        if list1 is not None:
                            list1.extend(cursor.fetchall())
                        else:
                            list1 = cursor.fetchall()
                    if gunPistol.get() == 1:
                        cursor.execute("SELECT gun.gun_id, gun_name, type, damage_type, rarity, manu_name FROM gun join"
                                       +" manufacturer on gun.manu_id = manufacturer.manu_id join inventory on" +
                                       " inventory.gun_id = gun.gun_id where hunter_id = "+ str(character[0][0]) +
                                       " and inventory.user_id = " + str(character[0][1]) +
                                       " and type = 'Pistol'")
                        if list1 is not None:
                            list1.extend(cursor.fetchall())
                        else:
                            list1 = cursor.fetchall()
                    if gunShotgun.get() == 1:
                        cursor.execute("SELECT gun.gun_id, gun_name, type, damage_type, rarity, manu_name FROM gun join"
                                       +" manufacturer on gun.manu_id = manufacturer.manu_id join inventory on" +
                                       " inventory.gun_id = gun.gun_id where hunter_id = "+ str(character[0][0]) +
                                       " and inventory.user_id = " + str(character[0][1]) +
                                       " and type = 'Shotgun'")
                        if list1 is not None:
                            list1.extend(cursor.fetchall())
                        else:
                            list1 = cursor.fetchall()
                    if gunSniper.get() == 1:
                        cursor.execute("SELECT gun.gun_id, gun_name, type, damage_type, rarity, manu_name FROM gun join"
                                       +" manufacturer on gun.manu_id = manufacturer.manu_id join inventory on" +
                                       " inventory.gun_id = gun.gun_id where hunter_id = "+ str(character[0][0]) +
                                       " and inventory.user_id = " + str(character[0][1]) +
                                       " and type = 'Sniper Rifle'")
                        if list1 is not None:
                            list1.extend(cursor.fetchall())
                        else:
                            list1 = cursor.fetchall()
                    if gunRocket.get() == 1:
                        cursor.execute("SELECT gun.gun_id, gun_name, type, damage_type, rarity, manu_name FROM gun join"
                                       +" manufacturer on gun.manu_id = manufacturer.manu_id join inventory on" +
                                       " inventory.gun_id = gun.gun_id where hunter_id = "+ str(character[0][0]) +
                                       " and inventory.user_id = " + str(character[0][1]) +
                                       " and type = 'Rocket Launcher'")
                        if list1 is not None:
                            list1.extend(cursor.fetchall())
                        else:
                            list1 = cursor.fetchall()
                    if list1 is not None:
                        for (ident, name, item, damage, rarity, manu) in list1:
                            listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                            "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
                    # do we need to query if nothing is selected?
                    #command ^ has been selected
                    # Each Checkbox is checked
                    if var2.get() == 1:
                        cursor.execute("SELECT shield.shield_id, shield_name, item_type, damage_type, rarity, manu_name"
                        +" FROM shield join manufacturer on shield.manu_id = manufacturer.manu_id join inventory on" +
                                       " inventory.shield = shield.shield_id where hunter_id = "+ str(character[0][0]) +
                                       " and inventory.user_id = " + str(character[0][1]))
                        list2 = cursor.fetchall()
                        for (ident, name, item, damage, rarity, manu) in list2:
                            listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                            "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
                    if var3.get() == 1:
                        cursor.execute("SELECT grenade.grenade_id, grenade_name, item_type, damage_type, rarity, "
                         + "manu_name FROM grenade join manufacturer on grenade.manu_id = manufacturer.manu_id "+
                         "join inventory on inventory.grenade_mod = grenade.grenade_id where hunter_id = " +
                                       str(character[0][0]) + " and inventory.user_id = " + str(character[0][1]))
                        list3 = cursor.fetchall()
                        for (ident, name, item, damage, rarity, manu) in list3:
                            listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                            "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
                    if var4.get() == 1:
                        cursor.execute("SELECT class_mod.mod_id, mod_name, item_type, damage_type, rarity, manu_name " +
                                       "FROM class_mod join manufacturer on class_mod.manu_id = manufacturer.manu_id " +
                                       "join inventory on inventory.class_mod = class_mod.mod_id where hunter_id = "
                                       + str(character[0][0]) +" and inventory.user_id = " + str(character[0][1]))
                        list4 = cursor.fetchall()
                        for (ident, name, item, damage, rarity, manu) in list4:
                            listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                            "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
                    if var5.get() == 1:
                        cursor.execute("SELECT relic.relic_id, relic_name, item_type, damage_type, rarity, manu_name " +
                                       "FROM relic join manufacturer on relic.manu_id = manufacturer.manu_id "
                                       "join inventory on inventory.relic = relic.relic_id where hunter_id = "
                                       + str(character[0][0]) + " and inventory.user_id = " + str(character[0][1]))
                        list5 = cursor.fetchall()
                        for (ident, name, item, damage, rarity, manu) in list5:
                            listbox.insert(tkinter.END, str(name) + "   :-:   " + str(item) +
                            "   :-:   " + str(damage) + "   :-:   " + str(rarity) + "   :-:   " + str(manu))
            else:
                if previousSearch == 'Show Character Inventory' or previousSearch == 'Show All Items':
                    listbox.delete(0, tkinter.END)

def onSelectSearch(event=None):
    global previousSearch
    if event:
        previousSearch = event.widget.get()
    query()

def onSelectCharacter(event=None):
    global previousCharacter
    global money
    global keys
    global eridium
    global ammo1
    global ammo2
    global ammo3
    global ammo4
    global ammo5
    global ammo6
    global ammo7
    global e1
    if event:
        previousCharacter = event.widget.get()
    cursor.execute("SELECT * from vault_hunter join user on vault_hunter.user_id = user.user_id where username = \'" +
                   e1 + "\' and name = \'" + previousCharacter + "\'")
    character = cursor.fetchall()
    cursor.execute("SELECT * from currency where hunter_id = \'" + str(character[0][0])+ "\' and user_id = \'" +
                   str(character[0][1]) + "\'")
    character = cursor.fetchall()
    for(id, mon, erid, pis, snip, shot, rif, sub, roc, gren, key, uid) in character:
        money.delete(0, tkinter.END)
        money.insert(tkinter.END, mon)
        eridium.delete(0, tkinter.END)
        eridium.insert(tkinter.END, erid)
        keys.delete(0, tkinter.END)
        keys.insert(tkinter.END, key)
        ammo1.config(text=str(rif))
        ammo2.config(text=str(sub))
        ammo3.config(text=str(shot))
        ammo4.config(text=str(snip))
        ammo5.config(text=str(pis))
        ammo6.config(text=str(roc))
        ammo7.config(text=str(gren))
    query()

def addtochar():
    global cursor
    global connection
    global previousSearch
    global previousCharacter
    global characters
    global listbox
    global e1
    global gunAR
    global gunPistol
    global gunRocket
    global gunShotgun
    global gunSMG
    global gunSniper
    global list1
    global var2
    global list2
    global var3
    global list3
    global var4
    global list4
    global var5
    global list5
    if previousSearch == 'Show All Items(Ignore Checkboxes)' or previousSearch == 'Show All Items'or \
            previousSearch == 'Show Character Inventory':
        x = listbox.index(tkinter.ACTIVE)
        if x != 0:
            x = x - 1
            row = None
            if (var2.get() == 1 or var3.get() == 1 or var4.get() == 1 or var5.get() == 1 or gunAR.get() == 1 or
                    gunSMG.get() == 1 or gunShotgun.get() == 1 or gunSniper.get() == 1 or gunPistol.get() == 1 or
                    gunRocket.get() == 1):
                if list1 is not None and (gunAR.get() == 1 or gunSMG.get() == 1 or gunShotgun.get() == 1 or
                                          gunSniper.get() == 1 or gunPistol.get() == 1 or gunRocket.get() == 1):
                    if (x - len(list1)) < 0:
                        row = list1[x]
                    else:
                        x = x - len(list1)
                        if list2 is not None and var2.get() == 1:
                            if (x - len(list2)) < 0:
                                row = list2[x]
                            else:
                                x = x - len(list2)
                                if list3 is not None and var3.get() == 1:
                                    if (x - len(list3)) < 0:
                                        row = list3[x]
                                    else:
                                        x = x - len(list3)
                                        if list4 is not None and var4.get() == 1:
                                            if (x - len(list4)) < 0:
                                                row = list4[x]
                                            else:
                                                x = x - len(list4)
                                                if list5 is not None and var5.get() == 1:
                                                    row = list5[x]
                                        else:
                                            if list5 is not None and var5.get() == 1:
                                                row = list5[x]
                                else:
                                    if list4 is not None and var4.get() == 1:
                                        if (x - len(list4)) < 0:
                                            row = list4[x]
                                        else:
                                            x = x - len(list4)
                                            if list5 is not None and var5.get() == 1:
                                                row = list5[x]
                                    else:
                                        if list5 is not None and var5.get() == 1:
                                            row = list5[x]
                        else:
                            if list3 is not None and var3.get() == 1:
                                if (x - len(list3)) < 0:
                                    row = list3[x]
                                else:
                                    x = x - len(list3)
                                    if list4 is not None and var4.get() == 1:
                                        if (x - len(list4)) < 0:
                                            row = list4[x]
                                        else:
                                            x = x - len(list4)
                                            if list5 is not None and var5.get() == 1:
                                                row = list5[x]
                                    else:
                                        if list5 is not None and var5.get() == 1:
                                            row = list5[x]
                            else:
                                if list4 is not None and var4.get() == 1:
                                    if (x - len(list4)) < 0:
                                        row = list4[x]
                                    else:
                                        x = x - len(list4)
                                        if list5 is not None and var5.get() == 1:
                                            row = list5[x]
                                else:
                                    if list5 is not None and var5.get() == 1:
                                        row = list5[x]
                else:
                    if list2 is not None and var2.get() == 1:
                        if (x - len(list2)) < 0:
                            row = list2[x]
                        else:
                            x = x - len(list2)
                            if list3 is not None and var3.get() == 1:
                                if (x - len(list3)) < 0:
                                    row = list3[x]
                                else:
                                    x = x - len(list3)
                                    if list4 is not None and var4.get() == 1:
                                        if (x - len(list4)) < 0:
                                            row = list4[x]
                                        else:
                                            x = x - len(list4)
                                            if list5 is not None and var5.get() == 1:
                                                row = list5[x]
                                    else:
                                        if list5 is not None and var5.get() == 1:
                                            row = list5[x]
                            else:
                                if list4 is not None and var4.get() == 1:
                                    if (x - len(list4)) < 0:
                                        row = list4[x]
                                    else:
                                        x = x - len(list4)
                                        if list5 is not None and var5.get() == 1:
                                            row = list5[x]
                                else:
                                    if list5 is not None and var5.get() == 1:
                                        row = list5[x]
                    else:
                        if list3 is not None and var3.get() == 1:
                            if (x - len(list3)) < 0:
                                row = list3[x]
                            else:
                                x = x - len(list3)
                                if list4 is not None and var4.get() == 1:
                                    if (x - len(list4)) < 0:
                                        row = list4[x]
                                    else:
                                        x = x - len(list4)
                                        if list5 is not None and var5.get() == 1:
                                            row = list5[x]
                                else:
                                    if list5 is not None and var5.get() == 1:
                                        row = list5[x]
                        else:
                            if list4 is not None and var4.get() == 1:
                                if (x - len(list4)) < 0:
                                    row = list4[x]
                                else:
                                    x = x - len(list4)
                                    if list5 is not None and var5.get() == 1:
                                        row = list5[x]
                            else:
                                if list5 is not None and var5.get() == 1:
                                    row = list5[x]
            if previousSearch == 'Show All Items(Ignore Checkboxes)':
                if (x - len(list1)) < 0:
                    row = list1[x]
                    x = x - len(list1)
                else:
                    x = x - len(list1)
                    if (x - len(list2)) < 0:
                        row = list2[x]
                        x = x - len(list2)
                    else:
                        x = x - len(list2)
                        if (x - len(list3)) < 0:
                            row = list3[x]
                            x = x - len(list3)
                        else:
                            x = x - len(list3)
                            if (x - len(list4)) < 0:
                                row = list4[x]
                                x = x - len(list4)
                            else:
                                x = x - len(list4)
                                row = list5[x]
            if previousCharacter != '. . .':
                    cursor.execute(
                        "SELECT * from vault_hunter join user on vault_hunter.user_id = user.user_id where "
                        "username = \'" + e1 + "\' and name = \'" + previousCharacter + "\'")
                    character = cursor.fetchall()
                    global inventory
                    if row[2] == 'Sniper Rifle' or row[2] == 'Submachine Gun' or row[2] == 'Assault Rifle' or \
                            row[2] == 'Pistol' or row[2] == 'Shotgun' or row[2] == 'Rocket Launcher':
                        cursor.execute(inventory, (character[0][1], character[0][0], row[0], None, None, None, None))
                    elif row[2] == 'Shield':
                        cursor.execute(inventory, (character[0][1], character[0][0], None, row[0], None, None, None))
                    elif row[2] == 'Grenade':
                        cursor.execute(inventory, (character[0][1], character[0][0], None, None, None, None, row[0]))
                    elif row[1] == 'Relic': #TODO CHANGE IF TABLE IS FIXED
                        cursor.execute(inventory, (character[0][1], character[0][0], None, None, None, row[0], None))
                    else:
                        print(row)
                        cursor.execute(inventory, (character[0][1], character[0][0], None, None, row[0], None, None))
                    errorbox('Added Item', (row[1] +" added to "+ previousCharacter))
                    connection.commit()
                    query()
            else:
                errorbox('Cannot Add Item', "Please select a character to add to")
        else:
            errorbox('Cannot Add Item', "No query or item not selected")
    else:
        errorbox('Cannot Add Item', "Incorrect Search: Try Show All Items or Show Character Inventory")

def deletefromchar():
    global cursor
    global connection
    global previousSearch
    global previousCharacter
    if previousCharacter != '. . .' and previousSearch == 'Show Character Inventory':
        x = listbox.index(tkinter.ACTIVE)
        if x != 0:
            x = x - 1
            row = None
            if (var2.get() == 1 or var3.get() == 1 or var4.get() == 1 or var5.get() == 1 or gunAR.get() == 1 or
                    gunSMG.get() == 1 or gunShotgun.get() == 1 or gunSniper.get() == 1 or gunPistol.get() == 1 or
                    gunRocket.get() == 1):
                if list1 is not None and (gunAR.get() == 1 or gunSMG.get() == 1 or gunShotgun.get() == 1 or
                                          gunSniper.get() == 1 or gunPistol.get() == 1 or gunRocket.get() == 1):
                    if (x - len(list1)) < 0:
                        row = list1[x]
                    else:
                        x = x - len(list1)
                        if list2 is not None and var2.get() == 1:
                            if (x - len(list2)) < 0:
                                row = list2[x]
                            else:
                                x = x - len(list2)
                                if list3 is not None and var3.get() == 1:
                                    if (x - len(list3)) < 0:
                                        row = list3[x]
                                    else:
                                        x = x - len(list3)
                                        if list4 is not None and var4.get() == 1:
                                            if (x - len(list4)) < 0:
                                                row = list4[x]
                                            else:
                                                x = x - len(list4)
                                                if list5 is not None and var5.get() == 1:
                                                    row = list5[x]
                                        else:
                                            if list5 is not None and var5.get() == 1:
                                                row = list5[x]
                                else:
                                    if list4 is not None and var4.get() == 1:
                                        if (x - len(list4)) < 0:
                                            row = list4[x]
                                        else:
                                            x = x - len(list4)
                                            if list5 is not None and var5.get() == 1:
                                                row = list5[x]
                                    else:
                                        if list5 is not None and var5.get() == 1:
                                            row = list5[x]
                        else:
                            if list3 is not None and var3.get() == 1:
                                if (x - len(list3)) < 0:
                                    row = list3[x]
                                else:
                                    x = x - len(list3)
                                    if list4 is not None and var4.get() == 1:
                                        if (x - len(list4)) < 0:
                                            row = list4[x]
                                        else:
                                            x = x - len(list4)
                                            if list5 is not None and var5.get() == 1:
                                                row = list5[x]
                                    else:
                                        if list5 is not None and var5.get() == 1:
                                            row = list5[x]
                            else:
                                if list4 is not None and var4.get() == 1:
                                    if (x - len(list4)) < 0:
                                        row = list4[x]
                                    else:
                                        x = x - len(list4)
                                        if list5 is not None and var5.get() == 1:
                                            row = list5[x]
                                else:
                                    if list5 is not None and var5.get() == 1:
                                        row = list5[x]
                else:
                    if list2 is not None and var2.get() == 1:
                        if (x - len(list2)) < 0:
                            row = list2[x]
                        else:
                            x = x - len(list2)
                            if list3 is not None and var3.get() == 1:
                                if (x - len(list3)) < 0:
                                    row = list3[x]
                                else:
                                    x = x - len(list3)
                                    if list4 is not None and var4.get() == 1:
                                        if (x - len(list4)) < 0:
                                            row = list4[x]
                                        else:
                                            x = x - len(list4)
                                            if list5 is not None and var5.get() == 1:
                                                row = list5[x]
                                    else:
                                        if list5 is not None and var5.get() == 1:
                                            row = list5[x]
                            else:
                                if list4 is not None and var4.get() == 1:
                                    if (x - len(list4)) < 0:
                                        row = list4[x]
                                    else:
                                        x = x - len(list4)
                                        if list5 is not None and var5.get() == 1:
                                            row = list5[x]
                                else:
                                    if list5 is not None and var5.get() == 1:
                                        row = list5[x]
                    else:
                        if list3 is not None and var3.get() == 1:
                            if (x - len(list3)) < 0:
                                row = list3[x]
                            else:
                                x = x - len(list3)
                                if list4 is not None and var4.get() == 1:
                                    if (x - len(list4)) < 0:
                                        row = list4[x]
                                    else:
                                        x = x - len(list4)
                                        if list5 is not None and var5.get() == 1:
                                            row = list5[x]
                                else:
                                    if list5 is not None and var5.get() == 1:
                                        row = list5[x]
                        else:
                            if list4 is not None and var4.get() == 1:
                                if (x - len(list4)) < 0:
                                    row = list4[x]
                                else:
                                    x = x - len(list4)
                                    if list5 is not None and var5.get() == 1:
                                        row = list5[x]
                            else:
                                if list5 is not None and var5.get() == 1:
                                    row = list5[x]
                cursor.execute(
                    "SELECT * from vault_hunter join user on vault_hunter.user_id = user.user_id where "
                    "username = \'" + e1 + "\' and name = \'" + previousCharacter + "\'")
                character = cursor.fetchall()
                if row[2] == 'Sniper Rifle' or row[2] == 'Submachine Gun' or row[2] == 'Assault Rifle' or \
                        row[2] == 'Pistol' or row[2] == 'Shotgun' or row[2] == 'Rocket Launcher':
                    cursor.execute("delete from inventory where gun_id = \'"+ str(row[0]) +"\' and user_id = \'" +
                                   str(character[0][1]) +"\' and hunter_id = \'"+ str(character[0][0]) +"\' LIMIT 1")
                elif row[2] == 'Shield':
                    cursor.execute("delete from inventory where shield = \'" +str(row[0]) + "\' and user_id = \'" +
                                   str(character[0][1]) + "\' and hunter_id = \'" + str(character[0][0]) + "\' LIMIT 1")
                elif row[2] == 'Grenade':
                    cursor.execute("delete from inventory where grenade_mod = \'" + str(row[0]) + "\' and user_id = \'"
                                   + str(character[0][1]) + "\' and hunter_id = \'" + str(character[0][0])
                                   + "\' LIMIT 1")
                elif row[1] == 'Relic':  # TODO CHANGE IF TABLE IS FIXED
                    cursor.execute("delete from inventory where relic = \'" + str(row[0]) + "\' and user_id = \'" +
                                   str(character[0][1]) + "\' and hunter_id = \'" + str(character[0][0]) + "\' LIMIT 1")
                else:
                    cursor.execute("delete from inventory where class_mod = \'" + str(row[0]) + "\' and user_id = \'" +
                                   str(character[0][1]) + "\' and hunter_id = \'" + str(character[0][0]) + "\' LIMIT 1")
                errorbox('Deleted Item', (row[1] + " deleted from " + previousCharacter))
                connection.commit()
                query()
            else:
                errorbox('Cannot Delete Item', "No query: please check an item")
        else:
            errorbox('Cannot Delete Item', "No query or item not selected")
    else:
        errorbox('Cannot Delete Item', "Show your inventory with a character to delete an item")

def cChar():
    global cursor
    global connection
    global charInsert
    global previousCharacter
    global characters
    global main
    global k1
    global u
    global a
    global v
    if u.get() != '':
        if v.get() != '. . .':
            if a.get() == '':
                a = 1
                cursor.execute(charInsert, (user[0][0], v.get(), a, u.get()))
                connection.commit()
                cursor.execute("SELECT * from vault_hunter where user_id = \'" + str(user[0][0]) + "\'")
                characters = cursor.fetchall()
                names = []
                for (hid, cid, cass, level, name) in characters:
                    names.append(name)
                combochar = ttk.Combobox(main, width=30, values=names)
                combochar.grid(row=4, column=0, columnspan=3, padx=30)
                combochar.set(". . .")
                previousCharacter = ". . ."
                combochar.bind('<<ComboboxSelected>>', onSelectCharacter)
                errorbox('Created Character', (u.get() + " created!"))
            elif a.get() != '':
                try:
                    if 0 < int(a.get()) <= 100:
                        a = int(a.get())
                        cursor.execute(charInsert, (user[0][0], v.get(), a, u.get()))
                        connection.commit()
                        cursor.execute("SELECT * from vault_hunter where user_id = \'" + str(user[0][0]) + "\'")
                        characters = cursor.fetchall()
                        names = []
                        for (hid, cid, cass, level, name) in characters:
                            names.append(name)
                        combochar = ttk.Combobox(main, width=30, values=names)
                        combochar.grid(row=4, column=0, columnspan=3, padx=30)
                        combochar.set(". . .")
                        previousCharacter = ". . ."
                        combochar.bind('<<ComboboxSelected>>', onSelectCharacter)
                        errorbox('Created Character', (u.get() + " created!"))
                except:
                    errorbox('Cannot Create Character', "Invalid Level, try a value between 1 and 100")
            else:
                errorbox('Cannot Create Character', "Invalid Level, try a value between 1 and 100")
        else:
            errorbox('Cannot Create Character', "Please select a class")
    else:
        errorbox('Cannot Create Character', "Invalid name")
    k1.destroy()

def createChar():
    global k1
    global u
    global a
    global v
    k1 = tkinter.Tk()
    k1.title('New Character')
    k1.minsize(300, 50)
    tkinter.Label(k1, text='Name:').grid(row=0, column=0)
    u = tkinter.Entry(k1)
    u.grid(row=0, column=1)
    tkinter.Label(k1, text='Level(Defaults to 1):').grid(row=1, column=0)
    a = tkinter.Entry(k1)
    a.grid(row=1, column=1)
    tkinter.Label(k1, text='Class:').grid(row=2, column=0)
    v = ttk.Combobox(k1, width=20, values=("Siren", "Commando", "Gunzerker", "Assassin", "Mechromancer", "Psycho"))
    v.set(". . .")
    v.grid(row=2, column=1)
    tkinter.Button(k1, text='Create', width=10, command=cChar).grid(row=3, column=1)

def uChar():
    global cursor
    global connection
    global previousCharacter
    global previousSearch
    global e1
    global k2
    global v
    cursor.execute("SELECT * from vault_hunter join user on vault_hunter.user_id = user.user_id where "
    "username = \'" + e1 + "\' and name = \'" + previousCharacter + "\'")
    character = cursor.fetchall()
    cursor.execute("UPDATE vault_hunter set class = \'"+ v.get() +"\' where user_id = \'" +
    str(character[0][1]) +"\' and hunter_id = \'"+ str(character[0][0]) +"\'")
    connection.commit()
    k2.destroy()
    if previousSearch == "Show Current Character Stats and Badass":
        query()

def updateChar():
    if previousCharacter != '. . .':
        global k2
        global v
        k2 = tkinter.Tk()
        k2.title('Update Class')
        k2.minsize(300, 50)
        tkinter.Label(k2, text='Class:').grid(row=0, column=0)
        v = ttk.Combobox(k2, width=20, values=("Siren", "Commando", "Gunzerker", "Assassin", "Mechromancer", "Psycho"))
        v.set(". . .")
        v.grid(row=0, column=1)
        tkinter.Button(k2, text='Update', width=10, command=uChar).grid(row=1, column=1)
    else:
        errorbox('Error', "No character selected for class update")
def update():
    global e1
    global cursor
    global money
    global eridium
    global keys
    global previousCharacter
    global connection
    if previousCharacter != '. . .':
        cursor.execute("SELECT * from vault_hunter join user on vault_hunter.user_id = user.user_id where username = \'" +
            e1 + "\' and name = \'" + previousCharacter + "\'")
        character = cursor.fetchall()
        cursor.execute("Update currency set money = "+ str(money.get()) + " where hunter_id = \'"
                       + str(character[0][0]) + "\'")
        cursor.execute("Update currency set eridium = " + str(eridium.get()) + " where hunter_id = \'"
                       + str(character[0][0]) + "\'")
        cursor.execute("Update currency set skeletonkeys = " + str(keys.get()) + " where hunter_id = \'"
                       + str(character[0][0]) + "\'")
        connection.commit()
        errorbox('Update Successful', (previousCharacter + " currency updated!"))
    else:
        errorbox('Error', 'No character selected for currency update')

def dChar():
    global confirm
    global cursor
    global connection
    global previousCharacter
    global e1
    confirm.destroy()
    if previousCharacter != '. . .':
        cursor.execute(
            "SELECT hunter_id, vault_hunter.user_id from vault_hunter join user on vault_hunter.user_id = user.user_id where "
            "username = \'" + e1 + "\' and name = \'" + previousCharacter + "\'")
        character = cursor.fetchall()
        cursor.execute("Delete from vault_hunter where user_id = " + str(character[0][1]) + " and hunter_id = " + str(character[0][0]))
        connection.commit()
        errorbox('Character Deleted', (previousCharacter + " deleted!"))
        cursor.execute("SELECT * from vault_hunter where user_id = \'" + str(user[0][0]) + "\'")
        characters = cursor.fetchall()
        names = []
        for (hid, cid, cass, level, name) in characters:
            names.append(name)
        combochar = ttk.Combobox(main, width=30, values=names)
        combochar.grid(row=4, column=0, columnspan=3, padx=30)
        combochar.set(". . .")
        previousCharacter = ". . ."
        combochar.bind('<<ComboboxSelected>>', onSelectCharacter)
    else:
        errorbox('Error', 'No character selected to delete')

def deleteChar():
    global previousCharacter
    if previousCharacter != '. . .':
        global confirm
        confirm = tkinter.Tk()
        confirm.title('Delete Character')
        tkinter.Label(confirm, text='ARE you sure you want to delete your current selected character?').grid(row=0)
        tkinter.Button(confirm, text='Yes', width=25, command=dChar).grid(row=1, column=0)
        tkinter.Button(confirm, text='No', width=25, command=confirm.destroy).grid(row=1, column=1)
    else:
        errorbox('Error', 'No character selected to delete')

def dAll():
    global confirm2
    global cursor
    global connection
    global previousCharacter
    global e1
    global main
    confirm2.destroy()
    cursor.execute(
        "SELECT hunter_id, vault_hunter.user_id from vault_hunter join user on vault_hunter.user_id = user.user_id where "
        "username = \'" + e1 + "\'")
    character = cursor.fetchall()
    cursor.execute("Delete from vault_hunter where user_id = " + str(character[0][1]))
    connection.commit()
    main.destroy()
    start()
    errorbox('Account Deleted', "Please log in again to create a new account!")

def deleteAll():
    global previousCharacter
    if previousCharacter != '. . .':
        global confirm2
        confirm2 = tkinter.Tk()
        confirm2.title('Delete User')
        tkinter.Label(confirm2, text='ARE you sure you want to delete your user? All Data will be lost.').grid(row=0)
        tkinter.Button(confirm2, text='Yes', width=25, command=dAll).grid(row=1, column=0)
        tkinter.Button(confirm2, text='No', width=25, command=confirm2.destroy).grid(row=1, column=1)
    else:
        errorbox('Error', 'No character selected to delete')

def initalize():
    global r
    global e1
    global user
    global characters
    global connection
    global cursor
    global main
    global listbox
    global previousSearch
    global previousCharacter
    global previousPreviousSearch
    global previousPreviousCharacter
    global var2
    global var3
    global var4
    global var5
    global gunAR
    global gunPistol
    global gunRocket
    global gunShotgun
    global gunSMG
    global gunSniper
    global money
    global keys
    global eridium
    global ammo1
    global ammo2
    global ammo3
    global ammo4
    global ammo5
    global ammo6
    global ammo7
    global list1
    global list2
    global list3
    global list4
    global list5
    list1 = None
    list2 = None
    list3 = None
    list4 = None
    list5 = None
    e1 = e1.get()
    r.destroy()
    cursor = connection.cursor()
    previousSearch = '. . .'
    previousCharacter = '. . .'
    previousPreviousSearch = '. . .'
    previousPreviousCharacter = '. . .'
    cursor.execute("SELECT * from user where username = \'" + e1 + "\'")
    user = cursor.fetchall()
    cursor.execute("SELECT * from vault_hunter where user_id = \'" + str(user[0][0]) + "\'")
    characters = cursor.fetchall()
    main = tkinter.Tk()
    main.title('BorderlandsDB User Interface')
    main.minsize(720, 500)
    #search commands '. . .' negates searches
    tkinter.Label(main, text='Search', relief=tkinter.RIDGE).grid(row=0, column=0)
    combo = ttk.Combobox(main, width=100, values=("Show Character Inventory", "Show Current Character Stats and Badass",
     "Show All Items(Ignore Checkboxes)", "Show All Items", "Show All Item Locations", "Show All Vehicles"))
    combo.set(". . .")
    combo.grid(row=1, columnspan=10, padx=30)
    combo.bind('<<ComboboxSelected>>', onSelectSearch)
    tkinter.Label(main, width=1).grid(row=2)
    tkinter.Label(main, text='Character', relief=tkinter.RIDGE).grid(row=3, column=0, columnspan=3)
    tkinter.Label(main, text='Guns', relief=tkinter.RIDGE).grid(row=3, column=2, columnspan=3)
    tkinter.Label(main, text='Ammo', relief=tkinter.RIDGE).grid(row=3, column=5, columnspan=3)
    ammo1 = tkinter.Label(main, width=5, relief=tkinter.RIDGE)
    ammo1.grid(row=4, column=5, columnspan=3)
    ammo2 = tkinter.Label(main, width=5, relief=tkinter.RIDGE)
    ammo2.grid(row=5, column=5, columnspan=3)
    ammo7 = tkinter.Label(main, width=5, relief=tkinter.RIDGE)
    ammo7.grid(row=5, column=7, sticky="E")
    ammo3 = tkinter.Label(main, width=5, relief=tkinter.RIDGE)
    ammo3.grid(row=6, column=5, columnspan=3)
    ammo4 = tkinter.Label(main, width=5, relief=tkinter.RIDGE)
    ammo4.grid(row=7, column=5, columnspan=3)
    ammo5 = tkinter.Label(main, width=5, relief=tkinter.RIDGE)
    ammo5.grid(row=8, column=5, columnspan=3)
    ammo6 = tkinter.Label(main, width=5, relief=tkinter.RIDGE)
    ammo6.grid(row=9, column=5, columnspan=3)
    tkinter.Label(main, text='Other Items', relief=tkinter.RIDGE).grid(row=3, column=8, columnspan=3)
    names = []
    for (hid, cid, cass, level, name) in characters:
        names.append(name)
    combochar = ttk.Combobox(main, width=30, values=names)
    combochar.grid(row=4, column=0, columnspan=3, padx=30)
    combochar.set(". . .")
    combochar.bind('<<ComboboxSelected>>', onSelectCharacter)
    #currency stuff
    tkinter.Label(main, text='Money', relief=tkinter.RIDGE).grid(row=5, column=0, sticky="E")
    money = tkinter.Entry(main)
    money.grid(row=5, column=1, sticky="W")
    tkinter.Label(main, text='Eridium', relief=tkinter.RIDGE).grid(row=6, column=0, sticky="E")
    eridium = tkinter.Entry(main)
    eridium.grid(row=6, column=1, sticky="W")
    tkinter.Label(main, text='Keys', relief=tkinter.RIDGE).grid(row=7, column=0, sticky="E")
    keys = tkinter.Entry(main)
    keys.grid(row=7, column=1, sticky="W")
    updateb = tkinter.Button(main, text='Update Currency', command=update)
    updateb.grid(row=8, column=1, sticky="W")
    tkinter.Label(main, width=10).grid(row=9, column=0)
    createc = tkinter.Button(main, text='Create Character', command=createChar)
    createc.grid(row=10, column=0, padx=10)
    deletec = tkinter.Button(main, text='Delete Character', command=deleteChar)
    deletec.grid(row=10, column=1)
    updatec = tkinter.Button(main, text='Update Class', command=updateChar)
    updatec.grid(row=10, column=2, sticky="W")
    deleteu = tkinter.Button(main, text='Delete User', command=deleteAll)
    deleteu.grid(row=10, column=9, sticky="W")
    #list of checkboxes for scope of search
    gunAR = tkinter.IntVar()
    tkinter.Checkbutton(main, text="Assault Rifle", variable=gunAR, anchor="w", command=query).\
        grid(row=4, column=3, columnspan=3, sticky="W")
    gunSMG = tkinter.IntVar()
    tkinter.Checkbutton(main, text="Submachine Gun", variable=gunSMG, anchor="w", command=query). \
        grid(row=5, column=3, columnspan=5, sticky="W")
    gunShotgun = tkinter.IntVar()
    tkinter.Checkbutton(main, text="Shotgun", variable=gunShotgun, anchor="w", command=query). \
        grid(row=6, column=3, columnspan=3, sticky="W")
    gunSniper = tkinter.IntVar()
    tkinter.Checkbutton(main, text="Sniper Rifle", variable=gunSniper, anchor="w", command=query). \
        grid(row=7, column=3, columnspan=3, sticky="W")
    gunPistol = tkinter.IntVar()
    tkinter.Checkbutton(main, text="Pistol", variable=gunPistol, anchor="w", command=query). \
        grid(row=8, column=3, columnspan=3, sticky="W")
    gunRocket = tkinter.IntVar()
    tkinter.Checkbutton(main, text="Rocket Launcher", variable=gunRocket, anchor="w", command=query). \
        grid(row=9, column=3, columnspan=5, sticky="W")
    #other items
    var2 = tkinter.IntVar()
    tkinter.Checkbutton(main, text="Shields", variable=var2, anchor="w", command=query).\
        grid(row=4, column=8, columnspan=3, sticky="W")
    var3 = tkinter.IntVar()
    tkinter.Checkbutton(main, text="Grenades", variable=var3, anchor="w", command=query).\
        grid(row=5, column=8, columnspan=3, sticky="W")
    var4 = tkinter.IntVar()
    tkinter.Checkbutton(main, text="Class Mods", variable=var4, anchor="w", command=query).\
        grid(row=6, column=8, columnspan=3, sticky="W")
    var5 = tkinter.IntVar()
    tkinter.Checkbutton(main, text="Relics", variable=var5, anchor="w", command=query).\
        grid(row=7, column=8, columnspan=3, sticky="W")
    #sets up listbox and mousewheel scroll capabilities
    tkinter.Label(main, width=1).grid(row=11)
    tkinter.Label(main, text='Results', relief=tkinter.RIDGE).grid(row=12)
    scrollbar = tkinter.Scrollbar(main)
    listbox = tkinter.Listbox(main, width=100, yscrollcommand=scrollbar.set)
    listbox.insert(tkinter.END, ". . .")
    listbox.grid(row=13, columnspan=10, rowspan=10, padx=30)
    scrollbar.config(command=listbox.yview)
    #button for list, add and destroy
    addb = tkinter.Button(main, text='Add/Duplicate to Character', command=addtochar)
    addb.grid(row=23, column=1)
    deleteb = tkinter.Button(main, text='Delete item from character', command=deletefromchar)
    deleteb.grid(row=23, column=7)
    main.mainloop()

def login():
    global e1
    global e2
    global connection
    global r
    try:
        connection = mysql.connector.connect(
        host='ethan.cikeys.com',
        user=e1.get(),
        password=e2.get(),
        #user='ethancik_charles',
        #password='Borderlands2019!',
        database='ethancik_borderlands',
        auth_plugin='mysql_native_password')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            errorbox('Error', 'user name or password is incorrect')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            errorbox('Error', 'database does not exist')
        else:
            errorbox('Error', err)
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
