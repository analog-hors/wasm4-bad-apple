import pretty_midi

def filter_notes(notes: list[pretty_midi.Note]):
    for i in range(len(notes)):
        note = notes[i]
        if i != len(notes) - 1:
            in_front = notes[i + 1]
            if round(in_front.start - note.start, 1) == 0.4:
                yield note
        if (63.5 < note.start and note.start < 64) or (153 < note.start and note.start < 154):
            for i in range(32):
                offset = 0.4 * (i + 1) - 0.19
                yield pretty_midi.Note(note.velocity, note.pitch, note.start + offset, note.end + offset + 0.1)
            tick_start = 25.77916666666666
            b1 = 37.78020833333333
            b2 = 38.18020833333333
            yield pretty_midi.Note(note.velocity, note.pitch, note.start + tick_start, tick_start + note.end + 0.1)
            if (63.5 < note.start and note.start < 64):
                yield pretty_midi.Note(note.velocity, note.pitch, note.start + b1, b1 + note.end + 0.1)
                yield pretty_midi.Note(note.velocity, note.pitch, note.start + b2, b2 + note.end + 0.1)
            else:
                yield pretty_midi.Note(note.velocity, note.pitch, 191.721875 + 0.1, 191.721875 + 0.1 + note.end - note.start + 0.1)

our_instrument = pretty_midi.Instrument(program=87, is_drum=False, name="Bad Apple")
midi_data = pretty_midi.PrettyMIDI("orig.mid")
# print(midi_data.tick_to_time(184053))
# print(midi_data.tick_to_time(97902))
# exit()
instrument = midi_data.instruments[0]
for note in filter_notes(instrument.notes):
    new_note = pretty_midi.Note(note.velocity, 77, note.start + 0.19, note.end + 0.19 + 0.02)
    our_instrument.notes.append(new_note)
midi_data.instruments.append(our_instrument)
midi_data.write('music.mid')
