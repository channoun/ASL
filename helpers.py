from spellchecker import SpellChecker

import numpy as np


def one_hot_output(pred):
    """
    Takes the output of the neural network and returns a one-hot-encoded array based on the maximum weight of the input array
    """
    for i in range(len(pred)):
        if pred[i] == max(pred):
            pred[i] = 1
        else:
            pred[i] = 0
    return pred


def to_letter(arr):
    """
    Takes a one-hot-encoded numpy array and return the corresponding symbol (letter or white space) based on the training of the neural network
    """
    idx = np.where(arr == 1)[0][0]
    # "Empty" symbols are all represented as white spaces for user freedom of choice
    if idx > 25:
        return " "
    else:
        return chr(idx + ord("a"))


def check_spell(word):
    """
    Takes a word and return its closest correction if mispelled
    """
    if word == "":
        return word
    spell = SpellChecker()
    for mispelled in spell.unknown([word]):
        return spell.correction(mispelled)
    return word
