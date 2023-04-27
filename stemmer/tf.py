
import glob
import os


def calculateTf(words):
    index = {}
    sorted_tf = {}
    for word in words:
        term_count = words.count(word)
        total_words = len(words)
        tf = term_count
        index[word] = tf
    return index
