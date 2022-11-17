import synthesizer
from scipy.io import wavfile
import numpy as np


right_hand_notes = ['C4', 'C4', 'G4', 'G4',
                   'A4', 'A4', 'G4',
                   'F4', 'F4', 'E4', 'E4',
                   'D4', 'D4', 'C4',
                   'G4', 'G4', 'F4', 'F4',
                   'E4', 'E4', 'D4',
                   'G4', 'G4', 'F4', 'F4',
                   'E4', 'E4', 'D4',
                   'C4', 'C4', 'G4', 'G4',
                   'A4', 'A4', 'G4',
                   'F4', 'F4', 'E4', 'E4',
                   'D4', 'D4', 'C4',]

right_hand_duration = [0.5, 0.5, 0.5, 0.5,
                       0.5, 0.5, 1]*6
right_hand = synthesizer.get_song_data(right_hand_notes, right_hand_duration, 2)

left_hand_notes = ['C3',
                  'A3',
                  'F3',
                  'D3', 'C3',
                  'G3', 'F3',
                  'E3', 'D3',
                  'G3', 'F3',
                  'E3', 'D3',
                  'C3', 'E3', 'G3', 'C4',
                  'A3', 'A3', 'G3',
                  'F3', 'B2', 'E3', 'C3',
                  'D3', 'D3', 'C3']

left_hand_duration = [2,
                      2,
                      2,
                      1, 1,
                      1, 1,
                      1, 1,
                      1, 1,
                      1, 1,
                      0.5, 0.5, 0.5, 0.5,
                      0.5, 0.5, 1,
                      0.5, 0.5, 0.5, 0.5,
                      0.5, 0.5, 1]


left_hand = synthesizer.get_song_data(left_hand_notes, left_hand_duration, 2)
data = left_hand + right_hand

data = data * (4096 / np.max(data))

wavfile.write('piano_song.wav', 44100, data.astype(np.int16))

