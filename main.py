import tkinter as tk
from tkinter import filedialog
from pygame import mixer
from pygame import USEREVENT
from pygame import event

win = tk.Tk()
win.geometry("800x800")
win.title("Music Player")
SONG_END = USEREVENT + 1

mixer.init(44100, -16, True, 4096)
def choose():
    song = filedialog.askopenfilename(initialdir="C:\\Users\\ofero\\Music", title="Select Song", filetype=(("MP3", "*.mp3"), ("All files", "*")))
    mixer.music.load(song)
def play():
    mixer.music.set_volume(0.7)
    mixer.music.play()
    mixer.music.set_endevent(SONG_END)
    while True:
        for events in event.get():
            if events.type == SONG_END:
                song = filedialog.askopenfilename(initialdir="C:\\Users\\ofero\\Music", title="Select Song", filetype=(("MP3", "*.mp3"), ("All files", "*")))
                mixer.music.load(song)
def stop():
    mixer.music.pause()

choose_button = tk.Button(text="choose song", font=("Roboto Light", 12), height=4, width=14, command=choose)
choose_button.place(x=50, y=60)
play_button = tk.Button(text="play song", font=("Roboto Light", 12), height=4, width=14, command=play)
play_button.place(x=200, y=60)
stop_button = tk.Button(text="stop song", font=("Roboto Light", 12), height=4, width=14, command=stop)
stop_button.place(x=350, y=60)

win.mainloop()