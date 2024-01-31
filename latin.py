import tkinter as tk
from tkinter import Button, Tk, Widget, ttk, filedialog, ACTIVE
import pygame
import bossa_nova
import main_page
import rock

# initialized pygame
pygame.init()
LARGE_FONT = ("Verdana", 12)


class Latin(tk.Frame):
    def __init__(self, parent, controller, latin=None):
        tk.Frame.__init__(self, parent)

        # makes the page label
        label = tk.Label(self, text="Latin Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        # button to go to the main page
        button = tk.Button(self, text="Main Page",
                           command=lambda: controller.show_frame(main_page.MainPage))
        button.pack()
        # Rock page button
        button2 = tk.Button(self, text="Go to Rock", command=lambda: controller.show_frame(rock.Rock))
        button2.pack()
        # Bossa Nova page button
        button3 = tk.Button(self, text="Go to Bossa Nova", command=lambda: controller.show_frame(bossa_nova.Bossa))
        button3.pack()
        # these are the buttons that let you control the songs
        play_button = tk.Button(self, text="Play Song", command=self.start_song, font=("Helvetica", 10))
        stop_button = tk.Button(self, text="Stop Song", command=self.stop_song, font=("Helvetica", 10))
        pause_button = tk.Button(self, text="Pause", command=self.pause, font=("Helvetica", 10))
        resume_button = tk.Button(self, text="Resume Song", command=self.resume_song, font=("Helvetica", 10))
        stop_button.pack()
        resume_button.pack()
        # this makes the list that all the songs will be placed in
        self.songs = tk.Listbox(self, bg='black', fg='red', width=80)
        self.songs.pack()
        pause_button.pack()
        play_button.pack(pady=20)
        add_song_button = tk.Button(self, text="Add Song", command=self.add_song)
        add_song_button.pack()

    # this function adds the songs
    def add_song(self):
        song = filedialog.askopenfilename(initialdir='music/Latin/', title='Select Song',
                                          filetypes=(("mp3 Files", "*.mp3"),))
        print(song)
        song = song.replace('C:/Users/adria/PycharmProjects/GUI Project/music/Latin/', "")
        song = song.replace('.mp3', "")
        self.songs.insert(tk.END, song)

    # this function starts the songs
    def start_song(self):
        song = self.songs.get(ACTIVE)
        song = f'C:/Users/adria/PycharmProjects/GUI Project/music/Latin/{song}.mp3'
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

    # this lets you resume the song after it is paused
    def resume_song(self):
        pygame.mixer.music.unpause()

    # this completely kills the song off
    def stop_song(self):
        pygame.mixer.music.stop()

    # this pauses the song
    def pause(self):
        pygame.mixer.music.pause()

    # this prints out if the button was pressed
    def is_pressed(self):
        print("it was pressed")