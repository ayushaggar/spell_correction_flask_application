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


def main(input_text, path_to_sample):
    global dictionary
    dictionary = Counter(get_word(open(path_to_sample).read()))

