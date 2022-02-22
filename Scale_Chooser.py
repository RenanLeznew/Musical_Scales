import random

from numpy import place

def random_scale():
    Scales = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
    Modes = ["Ionian", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian", "Locrian"]
    Scales_Picker = random.randint(0, 11)
    Modes_Picker = random.randint(0, 6)
    Scale = Scales[Scales_Picker]
    Mode = Modes[Modes_Picker]
    Play = "The scale to be played is a " + str(Scale) + " " + str(Mode)
    return Play