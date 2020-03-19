import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from pygame import mixer
from pygame import error as pyerror
import sqlite3
import pyautogui
import json

win = tk.Tk()
win.geometry("800x800")
win.title("Music Player")

# hex_colors = {'black': '#000000'}
def connect():
    global connection
    connection = sqlite3.connect("D:\\OFER\\Python\\Projects\\music player\\datebase\\musicplayer.db")
    global cursor
    cursor = connection.cursor()
def add():
    file = filedialog.askopenfilename(initialdir="C:\\Users\\ofero\\Music", title="Select Song", filetype=(("MP3", "*.mp3"), ("All files", "*")))
    name = pyautogui.prompt(title='Enter Name', text='Enter the name of the song', default='unknown')
    #text_to_execute = "INSERT INTO songs (name, path) VALUES (" + name + ", " + file + ");"
    #print(text_to_execute)
    text = "INSERT INTO songs (name, path) " \
           "VALUES (\'{}\', \'{}\');".format(name, file)
    #print(text)
    #cursor.execute("INSERT INTO songs (name, path) VALUES (\'{}\', \'{}\');".format(name, file))
    cursor.execute(text)
    connection.commit()
    getnames()

def getnames():
    songs_listbox.delete('0', 'end')
    cursor.execute("SELECT name from songs")
    rows = cursor.fetchall()
    for row in rows:
        songs_listbox.insert('end', row[0])
        #print(row)
def play():
    try:
        mixer.music.play()
    except pyerror:
        pyautogui.alert(title='Select a song', text='Select a song first!')
    else:
        play_button.config(image=pause_photoimage, command=pause)
def pause():
    play_button.config(image=play_photoimage, command=play)
    mixer.music.pause()
def backwards():
    print("backwards\nthe process is to first to stop and then start again")
def forwards():
    pass
    ind = songs_listbox.get([10])
    index = songs_listbox.get(0, "end").index("Hymn for the weekend")
    #print(index)

def click(evt):
    name = songs_listbox.get(songs_listbox.curselection())
    cursor.execute("SELECT path FROM songs WHERE name = \'{}\'".format(name))
    rows = cursor.fetchall()
    rows = rows[0]
    song = rows[0]
    mixer.music.load(song)
    index = songs_listbox.get(0, "end").index(name)
    i = 0
    print("index is {}".format(index))
    for song in range(index + 1, songs_listbox.size() + 1):
        song_name = songs_listbox.get(song)
        cursor.execute("SELECT path FROM songs WHERE name = \'{}\'".format(song_name))
        row = cursor.fetchall()
        #print("row is {}".format(row))
        try:
            row = row[i]
            print("row (new) is {}".format(row))
            queue_song = row[i]
        except IndexError:
            break
        print(queue_song)
        mixer.music.queue(queue_song)
        print(song_name)
        print("I is {}".format(i))
        i += 1
def test():
    #cursor.execute('SELECT path FROM songs WHERE name = \'Congratulations\'')
    #rows = cursor.fetchall()
    #rows = json.dumps(rows)
    #rows = json.load(rows)
    #rows = rows[0]
    #print(rows)
    #rows = rows[0]
    #song = rows[0]
    #print(song)
    #mixer.music.load(song)
    mixer.music.set_volume(0.7)
    #mixer.music.play()
    #print(song)
    #for row in rows:
        #print(row)
    #print(rows[0])
    #new_cursor = connection.cursor()
    #text = 'INSERT INTO songs (name, path) VALUES (\'Straightjacket\', \'' + r'C:\Users\ofero\Documents\Ofer\Barcelona Music\Quinn XCII - Straightjacket.mp3' + '\');'
    #print(text[63:65])
    #cursor.execute('INSERT INTO songs (name, path) VALUES (\'Straightjacket\', \'C:\Users\ofero\Documents\Ofer\Barcelona Music\Quinn XCII - Straightjacket\'')
    #new_cursor.execute(text)
    #connection.commit()
    cursor.execute("SELECT path FROM songs WHERE name = \'Hymn for the weekend\'")
    row = cursor.fetchall()
    row = row[0]
    song = row[0]
    mixer.music.load(song)
    mixer.music.play()
    mixer.music.get_pos()

# mixer.init(44100, -16, True, 4096)
mixer.init(22050, -16, True, 8192)

# ---------------------- buttons images set ----------------------------
# ---------- play button image set ---------
play_photo = PhotoImage(file="D:\\OFER\\Python\\Projects\\music player\\images and resources\\play sign.png")
play_photoimage = play_photo.subsample(11, 11)
# ---------- pause button (play button) image set -----------
pause_photo = PhotoImage(file="D:\\OFER\\Python\\Projects\\music player\\images and resources\\pause sign.png")
pause_photoimage = pause_photo.subsample(11, 11)
# ----------- backwards button image set --------------
backwards_photo = PhotoImage(file="D:\\OFER\\Python\\Projects\\music player\\images and resources\\backwards sign.png")
backwards_photoimage = backwards_photo.subsample(6, 6)
# ----------- forwards button image set --------------
forwards_photo = PhotoImage(file="D:\\OFER\\Python\\Projects\\music player\\images and resources\\forwards sign.png")
forwards_photoimage = forwards_photo.subsample(12, 10)
# -----------------------------------------------------------------------


song_name = ""
# --------- LABEL ----------
song_playing = tk.Label(text="Song Playing: ", font=("Roboto Light", 16))
song_playing.place(x=200, y=660)
song_playing_name = tk.Label(text=song_name, font=("Roboto Light", 16))
song_playing_name.place(x=200, y=700)
# --------- Buttons --------
play_button = tk.Button(height=100, width=100, image=play_photoimage, command=play)
play_button.place(x=340, y=400)
backwards_button = tk.Button(height=100, width=100, image=backwards_photoimage, command=backwards)
backwards_button.place(x=230, y=400)
forwards_button = tk.Button(height=100, width=100, image=forwards_photoimage, command=forwards)
forwards_button.place(x=450, y=400)
test_button = tk.Button(text="test me!", width=16, height=6, font=("Roboto Light", 12), command=test)
test_button.place(x=50, y=60)
add_button = tk.Button(text="Add Songs", font=("Robot Light", 12), height=4, width=14, command=add)
add_button.place(x=600, y=390)
# ---------- list box ----------
songs_listbox = tk.Listbox(height=16, width=30)
songs_listbox.place(x=600, y=120)
songs_listbox.bind('<<ListboxSelect>>', click)

connect()
getnames()
win.mainloop()

connection.close()
# TODO drop the # from the mixer.init() when you want to sound music
# TODO add a queue to the songs (try to find the index of an item in the listbox and continue from there)
# TODO check a bit more about the parameters of mixer.init()
