import random
from tkinter import *

class Scale():
    def __init__(self):
        scales = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
        modes = ["Ionian", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian", "Locrian"]
        scales_picker = random.randint(0, 11)
        modes_picker = random.randint(0, 6)
        scale = scales[scales_picker]
        mode = modes[modes_picker]
        self.play = "The scale to be played is the " + str(scale) + " " + str(mode)

def update_scale(label):
    scale_chosen = Scale()
    label['text'] = scale_chosen.play