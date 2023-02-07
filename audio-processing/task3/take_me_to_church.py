import synthesizer
import numpy as np
from scipy.io import wavfile

notes = ['C5', 'B4', 'A4',
         'A4', 'A4', 'E4', 'E4', 'A4', 'G4',
         'A4', 'E4', 'E4', 'B4', 'C5', 'B4',
         'B4','B4', 'B4', 'A4', 'B4',
         'B4', 'A4','B4', 'A4','B4', 'A4', 'B4',
         'C5', 'C5', 'G4', 'G4', 'A4', 'C5',
         'E5', 'G4', 'A4', 'G4', 'C5']

# duration = [0.5, 0.5, 1,
#             1, 1, 0.5, 0.5, 0.5, 0.5,
#             1, 0.5, 0.5, 0.5, 0.5, 1,
#             1, 1, 0.5, 0.5, 1,
#             0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1,
#             1, 0.5, 0.5, 0.5, 0.5, 1,
#             1, 1, 0.5, 0.5, 1]

duration = [0.25, 0.25, 0.5,
            0.5, 0.5, 0.25, 0.25, 0.25, 0.25,
            0.5, 0.25, 0.25, 0.25, 0.25, 0.5,
            0.5, 0.5, 0.25, 0.25, 0.5,
            0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5,
            0.5, 0.25, 0.25, 0.25, 0.25, 0.5,
            0.5, 0.5, 0.25, 0.25, 0.5]

song_data = synthesizer.get_song_data(notes, duration, 1)

# data = left_hand + right_hand

data = song_data * (4096 / np.max(song_data))

wavfile.write('take_me_to_church.wav', 44100, data.astype(np.int16))

