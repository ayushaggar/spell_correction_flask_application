import numpy as np
import requests

import logging
import os
import time

from flask import (Flask, request, url_for, render_template, abort,
                   send_from_directory)
# spell correction model
from model import spell_correction
app = Flask(__name__)
app.config['PATH_TO_SAMPLE_DATA'] = os.path.join(os.getcwd(), 'data')


@app.route('/spellCorrect/text', methods=['GET', 'POST'])
def text_read():
    return render_template('text_read.html')


@app.route('/spellCorrect/result', methods=['POST'])
def process_text_result():
    """
    Handles HTTP request by saving and processing text.

    Returns:
        method call to `show_text_success` that calls to render our results'
        template with the request result
    """
    text_result = {}
    request_timestamp = int(time.time() * 1000)
    text_result['timestamp'] = request_timestamp

    input_text = request.form['text']
    if input_text == '':
        abort(406, "No text provided")
    elif ' ' in input_text:
        abort(406, "more than one word is provided")

    text_result['text_input'] = input_text

    # pre process input data
    path_to_sample = os.path.join(
        app.config['PATH_TO_SAMPLE_DATA'],
        "sample_text_books.txt")
    processed_text_output = spell_correction.main(input_text, path_to_sample)
    print('Pre-processing done! \n')
    text_result['text_output'] = processed_text_output
    return show_text_result(text_result)


def show_text_result(text_result):
    """
    Handles successful text detection
    and returns the render_template for Flask

    Args:
        text_result (dict): Request processing and result information

    Returns:
        (:obj:`flask.render_template`)
    """
    return render_template('text_result.html', **text_result)


def main():
    app.run(host="0.0.0.0", port=5000, debug=False)


if __name__ == '__main__':
    main()
