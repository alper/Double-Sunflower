#!/usr/bin/env python

import itertools

numbers = [-61, -60, -58, -57, -26, -16, 8, 12, 48, 91]

def check(numbers):
    correct = 10
    
    # The position between 44 and -32 is assumed to be position 0
    # counted clock wise from there.
    if numbers[0] != 44+41+numbers[1]-32+numbers[-1] -78:
        correct -= 1
    if numbers[1] != 41+numbers[2]+52+numbers[6]-32+numbers[0]:
        correct -= 1
    if numbers[2] != -85-68+numbers[3]+52+numbers[1]+41:
        correct -= 1
    if numbers[3] != -68+30-29+numbers[4]+52+numbers[2]:
        correct -= 1
    if numbers[4] != numbers[3]-29-27+33+numbers[5]+52:
        correct -= 1
    if numbers[5] != 52 + numbers[4] + 33 -90 -15 + numbers[6]:
        correct -= 1
    if numbers[6] != numbers[1] + 52 + numbers[5] -15 + numbers[7] -32:
        correct -= 1
    if numbers[7] != -32 + numbers[6] -15 + 49 -49 + numbers[8]:
        correct -= 1
    if numbers[8] != numbers[9] -32 + numbers[7] -49 + 77 + 61:
        correct - 1
    if numbers[9] != -78 + numbers[0] -32 + numbers[8] + 61 + 44:
        correct -= 1
    
    return correct

for perm in itertools.permutations(numbers):
    if check(perm) == 10:
        print perm