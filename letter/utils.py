__author__ = 'max'

import random


def get_next_letter():
    alfabet = range(ord('a'), ord('z') + 1)
    return chr(random.choice(alfabet))