'''
AI USAGE!
AI was only used on freqs.py and notes.py!
'''
from machine import Pin, PWM
import time
import freqs, notes
# Replace this when needed
#      |  THIS |
import bad_apple as s

freq = freqs.freq
notes = notes.notes
song = s.song
bpm = s.bpm

buzzer = PWM(Pin(23))
# Works
def note_ms(bpm, note):
    if note == '':
        return 0
    else:    
        t_q = 60_000 / bpm
        return t_q * notes[note]
    
def play_tone(note):
    buzzer.freq(freq[note])
    time.sleep_ms(int(note_ms(bpm,x[1])))

for x in song:
    play_tone(x[0])
buzzer.deinit()