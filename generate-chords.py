from midiutil import MIDIFile

chords = [
    {
        'name': 'major',
        'offsets': [0,4,7]
    },
    {
        'name': 'minor',
        'offsets': [0, 3, 7]
    },
    {
        'name': 'dim',
        'offsets': [0, 3, 9]
    }
]

notes = [
    'C', 'C#-Db', 'D', 'D#-Eb', 'E', 'F', 'F#-Gb', 'G', 'G#-Ab', 'A', 'A#-Bb', 'B'
]

start_note = 24

midi_note = start_note
for octave in range(0,5):
    for note in notes:
        for chord in chords:
            print(f'{note} {octave} {chord["name"]} {midi_note} {midi_note + chord["offsets"][1]} {midi_note + chord["offsets"][2]}')
            track    = 0
            channel  = 0
            time     = 0    # In beats
            duration = 4    # In beats
            tempo    = 120  # In BPM
            volume   = 100  # 0-127, as per the MIDI standard

            MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created automatically)
            MyMIDI.addTempo(track, time, tempo)
            for offset in chord['offsets']:
                MyMIDI.addNote(track, channel, midi_note + offset, 0, duration, volume)

            with open(f"{note} {octave} {chord['name']}.mid", "wb") as output_file:
                MyMIDI.writeFile(output_file)
        midi_note += 1
