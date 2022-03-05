import random
from tkinter import *

from matplotlib.pyplot import step

class Scale():
    def __init__(self):
        self.scales = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
        self.modes = ["Ionian", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian", "Locrian"]
        self.general_scale = {"i":"tonic", "ii":"supertonic", "iii":"mediant", "iv":"subdominant", "v":"dominant", "vi":"submediant", "vii":"subtonic"}
        self.scales_picker = random.randint(0, 11)
        self.modes_picker = random.randint(0, 6)
        self.scale = self.scales[self.scales_picker]
        self.mode = self.modes[self.modes_picker]
        self.play = "The scale to be played is the " + str(self.scale) + " " + str(self.mode)
    def generate_scale(self):
        root = self.scales[self.scales_picker]
        self.general_scale["i"] = root
        return self.general_scale
    def step_function(self, step, note):
        if step == "whole":
            self.step = self.scales.index(note) + 2
            self.whole_step = self.scales[self.step%12]
            return self.whole_step
        elif step == "half":
            self.step = self.scales.index(note) + 1
            self.half_step = self.scales[self.step%12]
            return self.half_step

def update_scale(label):
    scale_chosen = Scale()
    label['text'] = scale_chosen.play