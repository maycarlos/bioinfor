#!/usr/bin/env python3

import numpy as np
import os
from os.path import isdir, join, isfile

from numpy.lib.function_base import insert

sequence_1 = "aldusfkjfh"
sequence_2 = "adslçklsdk"


table = np.zeros((len(sequence_1), len(sequence_2)))
print(table)
print(table.shape)

match = 2
indel = 1
mismatch= 1


for i in range(10):
    for j in range(10):
        if sequence_1[j] == sequence_2[j]:
            table[i,j] += match
        else:
            table[i,j] += mismatch
print(table)

