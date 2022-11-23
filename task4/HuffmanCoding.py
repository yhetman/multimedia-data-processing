from scipy.io import wavfile
import numpy as np
from json import dumps
from collections import Counter
from math import log, ceil
import heapq
from copy import deepcopy

class Heap:
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value
        self.flag = None

    def __gt__(self, other):
        if other == None or (not isinstance(other, Heap)):
            return -1
        return self.value > other.value

    def __lt__(self, other):
        if other == None or (not isinstance(other, Heap)):
            return -1
        return self.value < other.value
    
    
class TreePath:
    def __init__(self):
        self.temp_dict_var = {}

    def paths(self, root):
        path = []
        self.path_recursion(root, path, 0)

    def path_recursion(self, root, path, path_len):
        if root is None:
            return
        if(len(path) > path_len):
            path[path_len] = root.flag
        else:
            path.append(root.flag)
        path_len += 1
        if root.left is None and root.right is None:
            self.temp_dict_var[int(root.key)] = deepcopy(
                ''.join(str(char) for char in path[1:]))
        else:
            self.path_recursion(root.left, path, path_len)
            self.path_recursion(root.right, path, path_len)
            
            
class HuffmanCoding:
    def __init__(self, orignal_signal):
        self.orignal_signal = orignal_signal
        self.frequencies = self.frequencies_counter()
        self.codes = dict()
        self.keys = dict()
        self.compressed_signal = list()
        self.decompressed_signal = []

    def frequencies_counter(self):
        frequencies = {}
        for value in self.orignal_signal:
            if value not in frequencies:
                frequencies[value] = 0
            frequencies[value] += 1
        return frequencies

    
    def create_codes(self, heap):
        treePath = TreePath()
        treePath.paths(heap)
        self.keys = treePath.temp_dict_var
        self.compressed_signal = [self.keys[i] for i in self.orignal_signal]
        for key in self.keys :
            self.codes[self.keys[key]] = key
        return self.compressed_signal, self.codes
    
    
    def build_huffman_tree(self):
        freq_dict = {key: value for key, value in sorted(
            self.frequencies.items(), key = lambda item: item[1])}
        heap = []
        for key in freq_dict:
            node = Heap(key, freq_dict[key])
            heapq.heappush(heap, node)
        counter = 0
        while(len(heap) > 1):
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)
            node1.flag = 0
            node2.flag = 1
            merged = Heap(None, node1.value + node2.value)
            merged.flag = (counter % 2)
            counter += 1
            merged.left, merged.right = node1, node2
            heapq.heappush(heap, merged)
        return heap
 

    def compress(self):
        heap = self.build_huffman_tree()
        return self.create_codes(heap[0])
        
        
    def decompress(self):
        self.decompressed_signal = \
        np.array([self.codes[i]for i in self.compressed_signal])
        return self.decompressed_signal
    
    
    def save_codes(self):
        with open("compressed.json", "wb") as file:
            file.write(dumps(self.keys).encode("utf-8"))
        print('--->Compressed codes of signal were saved to compressed.json!')


if __name__ == '__main__':
    print('--->Huffman Coding for Lossless Data Compression <---')
    fs, orignal_signal = wavfile.read('../task3/song.wav')
    orignal_signal = list(orignal_signal)
    print('--->First 5 values of the original signal:', orignal_signal[:5])
    
    HuffCodeObj = HuffmanCoding(orignal_signal)
    HuffCodeObj.compress()
    print('--->First 5 compressed values:', HuffCodeObj.compressed_signal[:5])
    HuffCodeObj.save_codes()
    
    decompressed_signal = HuffCodeObj.decompress()
    print('--->First 5 decompressed values:', decompressed_signal[:5])
    print('--->Decompressed signal was saved to decompressed.wav!')
    wavfile.write('decompressed.wav', fs, decompressed_signal.astype(np.int16))

    
    