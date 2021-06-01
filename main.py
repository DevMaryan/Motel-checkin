from datetime import datetime
import sqlite3
guests = []

con = sqlite3.Connection('example.db')
c = con.cursor()



class Guest():
    def __init__(self, room, name, surname, date):
        self.room = room
        self.name = name
        self.surname = surname
        self.date = date
    

def addGuest():
    print('Enter guest room number: ')
    guestRoom = input()
    print('Enter guest name:')
    guestName = input()
    print('Enter guest surname:')
    guestSurname = input()

    newGuest = Guest(guestRoom, guestName, guestSurname, datetime.utcnow())
    print(newGuest.name + ' is our new guest')
    Repository(newGuest)

def delGuest():
    viewGuests()
    print('Which guest would you like to delete?')
    print('Enter guest room number: ')
    userChoice = input()
    try:
        query = ("DELETE FROM Guest WHERE room = ?")
        data_Tuple = (userChoice,)
        c.execute(query,data_Tuple)
        con.commit()
        print(userChoice, ' has been deleted!')
    except sqlite3.Error as e:
        print(e)


def viewGuests():
    try:
        cur = con.cursor()
        cur.execute("SELECT * FROM Guest")
        rows = cur.fetchall()
        print("ROOM", "\tNAME", "\tSURNAME")
        for row in rows:
            print(row[0], ' \t',row[1], "\t",row[2])
    except sqlite3.Error as e:
        print(e)

def Repository(guest):
    guests.append(guest)
    for guest in guests:
        print(guest.name, ' checked at ', guest.date)
    room = guest.room
    name = guest.name
    surname = guest.surname
    date = guest.date
    
    try:
        query = ("INSERT INTO Guest(room,name,surname,date) VALUES (?, ?, ?, ?)")
        data_Tuple = (room, name, surname, date)
        c.execute(query,data_Tuple)
        con.commit()
    except sqlite3.Error as e:
        print(e)


stop = "";

while(stop != "y"):
    print('Please choose one of the following options:')
    print('1. Add Guests')
    print('2. Delete Guests')
    print('3. View all Guests')
    userChoice = input()
    if userChoice == "1":
        addGuest()
    elif userChoice == "2":
        delGuest()
    elif userChoice == "3":
        viewGuests()
    else:
        print('Invalid Input')
    print('Would you like to exit, Press y to exit?')
    exitorNot = input()
    if exitorNot == "y":
        break;
  
    