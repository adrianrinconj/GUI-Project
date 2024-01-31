import tkinter as tk
import pygame
import bossa_nova
import latin
import rock

pygame.init()
LARGE_FONT = ("Verdana", 12)


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # makes the page label
        label = tk.Label(self, text="Main Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        frame = tk.Frame(controller, width=800, height=500)
        frame.pack()
        label.pack(pady=10, padx=10)
        # Latin page button
        button1 = tk.Button(self, text="Go to Latin", command=lambda: controller.show_frame(latin.Latin))
        button1.pack()
        # Rock page button
        button2 = tk.Button(self, text="Go to Rock", command=lambda: controller.show_frame(rock.Rock))
        button2.pack()
        # Bossa nova page button
        button3 = tk.Button(self, text="Go to Bossa Nova", command=lambda: controller.show_frame(bossa_nova.Bossa))
        button3.pack()
