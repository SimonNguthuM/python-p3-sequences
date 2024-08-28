#!/usr/bin/env python3

def print_fibonacci(length):
    seq = []
    if length == 0:
        print(seq)
        return

    if length >= 1:
        seq.append(0)

    if length >= 2:
        seq.append(1)

    for i in range(2, length):
        next_num = seq[-1] + seq[-2]
        seq.append(next_num)
        
    print(seq)

