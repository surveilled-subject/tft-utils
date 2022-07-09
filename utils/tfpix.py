#!/usr/bin/env python3


# -- a python script to simulate tft champion shops
#    usage: from tfpix import *
#           tfpix(current level)


import numpy as np
import yaml
import random


def weighted_choice(objects, weights):
    weights = np.array(weights, dtype=np.float64)
    sum_of_weights = weights.sum()
    np.multiply(weights, 1 / sum_of_weights, weights)
    weights = weights.cumsum()
    x = random.random()
    for i in range(len(weights)):
        if x < weights[i]:
            return objects[i]


def tfpix(lvl):
    pix = []
    ones = []
    twos = []
    thrs = []
    fors = []
    fivs = []
    with open('../champions.yml') as f:
        chs = yaml.safe_load(f)
    for c in chs:
        if c['cost'] == 1:
            ones.append(c['name'])
        if c['cost'] == 2:
            twos.append(c['name'])
        if c['cost'] == 3:
            thrs.append(c['name'])
        if c['cost'] == 4:
            fors.append(c['name'])
        if c['cost'] == 5:
            fivs.append(c['name'])
    while len(pix) < 5:
        if lvl == 1 or lvl == 2:
            r = 1
        if lvl == 3:
            r = weighted_choice([1, 2], [.75, .25])
        if lvl == 4:
            r = weighted_choice([1, 2, 3], [.55, .30, .15])
        if lvl == 5:
            r = weighted_choice([1, 2, 3, 4], [.45, .33, .20, .02])
        if lvl == 6:
            r = weighted_choice([1, 2, 3, 4], [.25, .40, .30, .05])
        if lvl == 7:
            r = weighted_choice([1, 2, 3, 4, 5], [.19, .30, .35, .15, .01])
        if lvl == 8:
            r = weighted_choice([1, 2, 3, 4, 5], [.16, .20, .25, .35, .04])
        if lvl == 9:
            r = weighted_choice([1, 2, 3, 4, 5], [.9, .15, .30, .30, .16])
        if r == 1:
            pix.append(random.choice(ones))
        if r == 2:
            pix.append(random.choice(twos))
        if r == 3:
            pix.append(random.choice(thrs))
        if r == 4:
            pix.append(random.choice(fors))
        if r == 5:
            pix.append(random.choice(fivs))
    print(pix)
    return(0)

