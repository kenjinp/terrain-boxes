#!/usr/bin/env python3
from PIL import Image
import numpy as np
import sys


def main():
    if len(sys.argv) <= 1:
        print(f"usage: {sys.argv[0]} <image.tiff>")
        sys.exit(1)
    file = sys.argv[1]
    no_ext = "./"+ ''.join(file.split(".")[:-1])
    im = Image.open(file).resize((2048, 2048))
    a = np.array(im)
    int16 = a.astype('int16')
    int16.tofile(no_ext+".raw")
    Image.fromarray(int16).save(no_ext+".png")

if __name__ == "__main__":
    main()
