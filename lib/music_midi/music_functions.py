import time
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_midi.pitch_bend import PitchBend
from adafruit_midi.control_change import ControlChange
from adafruit_midi.program_change import ProgramChange
from adafruit_midi.system_exclusive import SystemExclusive

from music_midi.music_test import instruments


def play_note(midi, note, velocity=120, duration=0.5):
    midi.send(NoteOn(note, velocity))
    time.sleep(duration)
    midi.send(NoteOff(note, velocity))


def change_instrument(midi, instrument_name, sound_set="GENERAL_MIDI"):
    instrument_index = instruments[sound_set].index(instrument_name)
    midi.send(ProgramChange(instrument_index))
    

def bend_pitch(amount, channel=0):
    midi.send(PitchBend(amount, channel=channel))


def control_change(controller, value, channel=0):
    midi.send(ControlChange(controller, value, channel=channel))


def play_drum(midi, drum_name, drum_set="STANDARD_SET", velocity=120, duration=0.5):
    for note, name in instruments["DRUM_SETS"][drum_set].items():
        if name == drum_name:
            play_note(midi, note, velocity, duration)
            break
           
           
# Function to play a sequence of notes (a simple melody)
def play_melody(melody, channel=0):
    for note, velocity, duration in melody:
        play_note(note, velocity, duration, channel)


def test_midi_synth(midi):
    # Test General MIDI instruments
    for instrument in instruments["GENERAL_MIDI"]:
        change_instrument(midi, instrument)
        play_note(midi, 60)  # Middle C
        time.sleep(0.5)

    # Test MT-32 instruments
    for instrument in instruments["MT32"]:
        change_instrument(midi, instrument, "MT32")
        play_note(midi, 60)  # Middle C
        time.sleep(0.5)

    # Test drum sets 
    midi.send(ProgramChange(0))  # Set to standard drum kit
    for drum_set in instruments["DRUM_SETS"]:
        for drum in instruments["DRUM_SETS"][drum_set].values():
            play_drum(midi, drum, drum_set)
            time.sleep(0.25)


def set_volume(midi, volume):
    """
    Sends a System Exclusive message to change the volume on the MIDI device.
    
    Parameters:
    midi: MIDI interface object that can send messages.
    volume (int): The volume level to set (0-127).
    """
    # Ensure volume is within the valid range (0-127)
    if volume < 0 or volume > 127:
        raise ValueError("Volume must be between 0 and 127")
    
    volume_message = SystemExclusive([0x7f, 0x7f, 0x04], [0x01, 0x00, volume & 0x7f])
    midi.send(volume_message)
    print(f"MIDI Volume set to {volume}.")


def reset_midi(midi):
    """
    Sends a System Exclusive message to reset the MIDI device.
    
    Parameters:
    midi: MIDI interface object that can send messages.
    """
    reset_message = SystemExclusive([0x7e, 0x7f], [0x09, 0x01])
    midi.send(reset_message)
    print("MIDI Reset sent.")