import random

Scales = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
Modes = ["Ionian", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian", "Locrian"]
rerun = ""
while rerun != "Stop":
    Scales_Picker = random.randint(0, 11)
    Modes_Picker = random.randint(0, 6)
    Scale = Scales[Scales_Picker]
    Mode = Modes[Modes_Picker]
    Play = str(Scale) + " " + str(Mode)
    print("The scale to be played is a " + Play)
    rerun = input("\n If you wish to stop the program, type 'Stop': \n")
print("Goodbye!")