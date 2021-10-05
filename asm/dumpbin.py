#!/bin/env python3
import sys

if len(sys.argv) < 3:
    print(sys.argv[0], "<input>", "<output>")
    exit(1)

with open(sys.argv[1], "rb") as infile:
    with open(sys.argv[2], "wb") as outfile:
        assert infile.read(4) == b"embo", "Not an object file"

        infile.read(12) # skip over boring stuff

        length = int.from_bytes(infile.read(4), "little")
        outfile.write(infile.read(length))
