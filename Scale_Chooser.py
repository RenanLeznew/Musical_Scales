import random
from tkinter import *

from matplotlib.pyplot import step

class Scale():
    def __init__(self):
        self.scales = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
        self.modes = ["Ionian", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian", "Locrian"]
        self.general_scale = {"i":"tonic", "ii":"supertonic", "iii":"mediant", "iv":"subdominant", "v":"dominant", "vi":"submediant", "vii":"subtonic"}
        self.major_chords = {"C": "C E G", "Db":"Db F Ab", "D":"D Gb A", "Eb":"Eb G Bb", "E":"E Ab B", "F":"F A C", "Gb":"Gb Bb Db", "G":"G B D", "Ab":"Ab C Eb", "A":"A Db E", "Bb":"Bb D F", "B":"B Eb Gb"}
        self.root_picker = random.randint(0, 11)
        self.modes_picker = random.randint(0, 6)
        self.root = self.scales[self.root_picker]
        self.mode = self.modes[self.modes_picker]
        self.play = "The scale to be played is the " + str(self.root) + " " + str(self.mode)
    def generate_scale(self):
        self.general_scale["i"] = self.root
        tone_value = self.root
        for tone in self.general_scale:
            if tone != "i":
                if tone != "iv":
                    tone_value = self.step_function("whole", tone_value)
                    self.general_scale[tone] = tone_value 
                else:
                    tone_value = self.step_function("half", tone_value)
                    self.general_scale[tone] = tone_value
        if self.mode == "Lydian":
            self.general_scale["iv"] = self.sharp_function(self.general_scale.get("iv"))            
        if self.mode == "Mixolydian" or self.mode == "Dorian" or self.mode == "Phrygian" or self.mode == "Aeolian" or self.mode == "Locrian":
            self.general_scale["vii"] = self.flat_function(self.general_scale.get("vii"))
        if self.mode == "Dorian" or self.mode == "Phrygian" or self.mode == "Aeolian" or self.mode == "Locrian":
            self.general_scale["iii"] = self.flat_function(self.general_scale.get("iii"))
        if self.mode == "Phrygian" or self.mode == "Aeolian" or self.mode == "Locrian":
            self.general_scale["vi"] = self.flat_function(self.general_scale.get("vi"))
        if self.mode == "Phrygian" or self.mode == "Locrian":
            self.general_scale["ii"] = self.flat_function(self.general_scale.get("ii"))
        if self.mode == "Locrian":
            self.general_scale["v"] = self.flat_function(self.general_scale.get("v"))    
        return self.general_scale

    def generate_chords(self):
        self.scale = self.generate_scale(self)
        self.chord_family = []
        return 0

    def step_function(self, step, note):
        if step == "whole":
            self.step = self.scales.index(note) + 2
            self.whole_step = self.scales[self.step%12]
            return self.whole_step
        elif step == "half":
            self.step = self.scales.index(note) + 1
            self.half_step = self.scales[self.step%12]
            return self.half_step

    def flat_function(self, note):
        self.flat = self.scales.index(note) - 1
        self.flattened_note = self.scales[self.flat]
        return self.flattened_note

    def sharp_function(self, note):
        self.sharp = self.scales.index(note) + 1
        self.sharpened_note = self.scales[self.sharp%12]
        return self.sharpened_note

def update_scale(label):
    global scale_chosen
    scale_chosen = Scale()
    label['text'] = scale_chosen.play

def show_scale(label):
    note_dictionary = scale_chosen.generate_scale()
    scale_string = ""
    for note in note_dictionary.values():
        scale_string += note + ", " 
    label['text'] = scale_string + scale_chosen.root