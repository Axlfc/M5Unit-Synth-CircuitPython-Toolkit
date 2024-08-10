import asyncio

import board, time, sys, supervisor

import busio
import synthio
import audiomixer

import displayio
import terminalio


from adafruit_display_text import label
from adafruit_displayio_layout.layouts.grid_layout import GridLayout
from adafruit_display_shapes.circle import Circle


from music_midi.music_functions import *


def main(midi):
    print("Default output MIDI channel:", midi.out_channel + 1)
    
    reset_midi(midi)
    
    set_volume(midi, 127)

    # Example usage:
    change_instrument(midi, "Grand Piano")
    play_note(midi, 60)  # Middle C
    time.sleep(0.5)
    
    change_instrument(midi, "Violin")
    play_note(midi, 67)  # G
    time.sleep(0.5)
    
    play_drum(midi, "Kick drum1")
    time.sleep(0.5)
    
    # Uncomment the following line to run the full test
    # test_midi_synth(midi)


if __name__ == '__main__':
    uart = busio.UART(tx=board.D2, baudrate=31250, bits=8, parity=None, stop=1)
    midi = adafruit_midi.MIDI(midi_out=uart, out_channel=0)
    main(midi)
