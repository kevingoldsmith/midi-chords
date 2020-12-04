from midiutil import MIDIFile

chords = [
    {
        'name': 'maj',
        'offsets': [0,4,7]
    },
    {
        'name': 'min',
        'offsets': [0, 3, 7]
    },
    {
        'name': 'dim',
        'offsets': [0, 3, 9]
    },
    {
        'name': 'maj7',
        'offsets': [0, 4, 7, 11]
    },
    {
        'name': 'min7',
        'offsets': [0, 3, 7, 10]
    },
    {
        'name': 'dom7',
        'offsets': [0, 4, 7, 10]
    },
    {
        'name': 'sus2',
        'offsets': [0, 2, 7]
    },
    {
        'name': 'sus4',
        'offsets': [0, 5, 7]
    },
    {
        'name': 'aug',
        'offsets': [0, 4, 8]
    },
    {
        'name': 'dom9',
        'offsets': [0, 4, 7, 10, 14]
    },
    {
        'name': 'maj11',
        'offsets': [0, 4, 7, 11, 14, 17]
    }
]

notes = [
    'C', 'C#-Db', 'D', 'D#-Eb', 'E', 'F', 'F#-Gb', 'G', 'G#-Ab', 'A', 'A#-Bb', 'B'
]

start_note = 24

midi_note = start_note
for octave in range(0,9):
    for note in notes:
        for chord in chords:
            if midi_note + chord['offsets'][-1] < 128:
                print(f'{note} {octave} {chord["name"]}')
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
