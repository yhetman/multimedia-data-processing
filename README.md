# multimedia-data-processing

_____


## Task 1

###  Implementation of program that generates gamma in any tonality using twelve-tone equal temperament approach.

`f(i) = f_0 * 2^(i/12)`
`f(i)` - the pitch, or frequency (usually in hertz), we need to find;
`f_0` - the frequency of the reference pitch.

The reference pitch also known as Stuttgart pitch is A4, the 49th key from the left end of a piano, tuned to 440 Hz.

_____


## Task 2

### Implementation of sound effects.

**1.    Flanger effect** <br />

Flanging is a delay effect that has been available in recording studios since at least the 1960s. <br />
<br />
The term "flanging" comes from how the effect was originally achieved by two tape recorders set to play the same tape in unison, with their output mixed equally.
<br />
The flanging is modeled quite accurately as a forward-feedback comb filter in which the delay `M` varies with time. <br />
The input-output ratio for a basic flanger can be written as:
`y(n)=x(n)+gx [ n - M(n)]`, where <br />
`x(n)` - the amplitude of the input signal at the moment of time `n = 0,1,2...`; <br />
`y(n)` - the output signal at time `n`; <br />
`g` - depth of flanging effect; <br />
`M(n)` is the length of the delay at time `n`.

*****

**2.    Echo effect** <br />

An echo effect can be modeled as a weakened, delayed copy of the original signal added to itself. <br />
<br />
Here it can be considered as an FIR filtering operation.  <br />

An FIR filter has the form <br />

`[1, delayed_sec * Fs - 1, a]`, <br />

<br />
where `delayed_sec` is the number of seconds the echo should take, and `0 < a <= 1`.

_____


## Task 3

###  Implement elements of your own musical instrument synthesizer. <br />

Using the tools created in the previous practicals, it is easy to generate the frequencies of all the notes that have their representation on the piano keyboard. <br />
<br />
However, the resulting sound is rather boring and can hardly be called melodic. <br />
<br />
It lacks many of the characteristics associated with the sound of musical instruments and is too consistent across the range. <br />
<br />
So the same note will sound differently on the piano and on the violin. <br />
<br />
Here was added such characteristics: overtones, ADSR model, delay_pedal.

_____

## Task 4

### Implement one of the compression algorithms. <br />

Huffman coding is a lossless data compression algorithm. <br />

The idea is to assign variable-length codes to input characters. <br />
<br />
The length of the defined codes is based on the frequencies of the corresponding symbols. <br />

The most frequent symbol gets the smallest code, and the least frequent symbol gets the largest code. <br />
<br />
Variable length codes assigned to input characters are prefix codes. <br />

That is, the codes (bit sequences) are assigned in such a way that the code assigned to one symbol is not a prefix of the code assigned to any other symbol. <br />
<br />
In this way, Huffman coding ensures the absence of ambiguity during decoding of the generated bit stream.
<br /> 

<br /> Huffman coding consists of two main parts:
1. building a Huffman tree from the entered symbols;
2. traversing the Huffman tree and assigning codes to symbols.


