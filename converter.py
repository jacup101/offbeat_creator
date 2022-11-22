from mido import MidiFile

song = MidiFile('bohemian_rhapsody.mid', clip=True)
print(song)