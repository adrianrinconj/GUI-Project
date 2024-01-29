import tkinter as tk
from tkinter import filedialog
import pygame

import main_page
import latin
import rock
import bossa_nova

pygame.init()

# I got parts of this code from here:
# https://www.javatpoint.com/tkinter-application-to-switch-between-different-page-frames-in-python
# as well as both the pygame official documentation and tkinter documentation.
class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        # uses a tuple and cycles through all the frames
        for F in (main_page.MainPage, latin.Latin, bossa_nova.Bossa, rock.Rock):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(main_page.MainPage)

    # this shows the actual frames by placing them on top of one another
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
