#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

from collections import Counter

global dictionary
global max_word_count
global total_words


def get_word(text):
    return re.findall('[a-z]+', text.lower())


def prob_word(word):
    global dictionary
    global total_words
    return dictionary[word] / total_words


def dl_measure(word):
    return max(diff_reorder(word), key=prob_word)


def diff_reorder(word):
    # Different combination of  spelling corrections for word
    return (
        known(
            [word]) or known(
            edition_1(word)) or known(
                edition_2(word)) or [word])


def known(words):
    # check if word in dictionary or not
    global dictionary
    return set(w for w in words if w in dictionary)


def edition_1(word):
    # for all first edit in text
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edition_2(word):
    # for all second edit in text.... can do more depending on user type
    return (e2 for e1 in edition_1(word) for e2 in edition_1(e1))


def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')


def remove_special_character(inputString):
    # return re.sub('[^A-Za-z0-9]+', '', inputString)
    return re.sub('[^A-Za-z]+', '', inputString)


def reduce_lengthening(inputString):
    # assuming in english 3 same character not occur together
    pattern = re.compile(r"(.)\1{2,}")
    return pattern.sub(r"\1\1", inputString).lower()

# Given dictionary of words with their frequencies, function splits text
# at positions that give overall most likely words.
def find_words(text):
    global max_word_count
    probs, lasts = [1.0], [0]
    for i in range(1, len(text) + 1):
        prob_k, k = max((probs[j] * prob_word(text[j:i]), j)
                        for j in range(max(0, i - max_word_count), i))
        probs.append(prob_k)
        lasts.append(k)
    words = []
    i = len(text)
    while 0 < i:
        words.append(text[lasts[i]:i])
        i = lasts[i]
    words.reverse()
    return words

def main(input_text, path_to_sample):
    global dictionary
    global max_word_count
    global total_words
    dictionary = Counter(get_word(open(path_to_sample).read()))
    max_word_count = max(map(len, dictionary))
    total_words = float(sum(dictionary.values()))
    words = find_words(
        dl_measure(
            reduce_lengthening(
                remove_special_character(
                    deEmojify(input_text)))))
    result_list = []
    for word in words:
        result_list.append(dl_measure(word))
    return result_list
