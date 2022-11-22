from scipy.io import wavfile
import numpy as np   
from collections import Counter
from math import log, ceil
import json

class HuffmanCoding:
    def __init__(self, orignal_signal):
        self.orignal_signal = orignal_signal
        self.frequencies = self.freq_counter()
        self.codes = dict()
        self.keys = dict()
        self.compressed_signal = list()
        self.decompressed_signal = []

    def freq_counter(self):
        freq_dict = {}
        for value in self.orignal_signal:
            if value not in freq_dict:
                freq_dict[value] = 0
            freq_dict[value] += 1
        return freq_dict

    def compress(self):
        length = ceil(log(len(self.frequencies), 2))
        counter = 0
        for key in self.frequencies:
            self.keys[int(key)] = bin(counter)[2:].zfill(length)
            self.codes[bin(counter)[2:].zfill(length)] = key
            counter += 1
        self.compressed_signal = [self.keys[value] for value in self.orignal_signal]
        return self.compressed_signal, self.codes
    
    def decompress(self):
        self.decompressed_signal = np.array([self.codes[value] for value in self.compressed_signal])
        return self.decompressed_signal
    
    def save_codes(self):
        with open("compressed.json", "wb") as file:
            file.write(json.dumps(self.keys).encode("utf-8"))
        print('--->Compressed codes of signal were saved to compressed.json!')
        



if __name__ == '__main__':
    print('\n--->Fixed Length Huffman Coding<---')
    fs, orignal_signal = wavfile.read('../task3/song.wav')
    orignal_signal = list(orignal_signal)
    print('--->First 20 values of the orignal signal:', orignal_signal[:20])
    
    HuffCodeObj = HuffmanCoding(orignal_signal)
    HuffCodeObj.compress()
    print('--->First 20 compressed values:', HuffCodeObj.compressed_signal[:20])
    HuffCodeObj.save_codes()
    
    decompressed_signal = HuffCodeObj.decompress()
    print('--->First 20 decompressed values:', decompressed_signal[:20])
    print('--->Decompressed signal was saved to decompressed.wav!')
    wavfile.write('decompressed.wav', fs, decompressed_signal.astype(np.int16))

    
    