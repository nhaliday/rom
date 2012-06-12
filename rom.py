#!/usr/bin/env python
### ROM Manipulation Module ###


from itertools import *
from collections import deque


SMILEY = ["00000000",
          "01100110",
          "01100110",
          "00000000",
          "00011000",
          "00000000",
          "01100110",
          "00111100"]


def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)


def str_chunk(n, str_):
    grouped = grouper(n, str_)
    for group in grouped:
        yield ''.join(takewhile(lambda o: o is not None, group))


def byteform(zero_one_string):
    return map(lambda s: chr(int(s, 2)), str_chunk(8, zero_one_string))


def writebytes(file, sarray):
    for byte in byteform(''.join(sarray)):
        file.write(byte)


def bin2hex(binary_str):
    return hex(int(binary_str, 2))[2:]


def niceform(sarray):
    sarray = list(sarray)
    l = max(len(line) for line in sarray)
    hexl = (l + 3) / 4
    for line in sarray:
        yield (line, bin2hex(line).zfill(hexl))


def writetuples(file, array):
    for t in array:
        file.write(' '.join(t))
        file.write('\n')


def frames(n, sarray):
    l = len(sarray)
    for i in range(l - n + 1):
        yield sarray[i:i + n]


def main():
    with open('smiley.hex', 'wb') as fout, open('smiley.txt', 'w') as debug:
        repeatsmiley = [item for sublist in list(frames(8, list(islice(cycle(SMILEY), 263)))) for item in sublist]
        writebytes(fout, repeatsmiley)
        writetuples(debug, niceform(repeatsmiley))


if __name__ == "__main__":
    main()
