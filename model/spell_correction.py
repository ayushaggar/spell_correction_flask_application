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


def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')


def remove_special_character(inputString):
    # return re.sub('[^A-Za-z0-9]+', '', inputString)
    return re.sub('[^A-Za-z]+', '', inputString)


def reduce_lengthening(inputString):
    # assuming in english 3 same character not occur together
    pattern = re.compile(r"(.)\1{2,}")
    return pattern.sub(r"\1\1", inputString).lower()


def main(input_text, path_to_sample):
    global dictionary
    global max_word_count
    global total_words
    dictionary = Counter(get_word(open(path_to_sample).read()))
    max_word_count = max(map(len, dictionary))
    total_words = float(sum(dictionary.values()))
    reduce_lengthening(
                remove_special_character(
                    deEmojify(input_text)))
