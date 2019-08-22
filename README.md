## Objective
Spell Correction Task
1) Train a Custom Spell Correction Model
2) Make a Rest API in Flask APP

**Assumptions** -
1) English only spell correction

**Output** :
1) Custom Spell Correction Model
2) Rest API in Flask APP

**Constraints / Notes** ::
1) Handled Cases - 
    - Merging of 2 words eg: homeAssignment, schoolbag etc. [capitalization can be there or not]
    - Word joined by emojis or Latin or Greek character
    - Word joined by special chars special character, punctuation and space
    - One word two meaning - inlawmight be in law or in-law 

2) Fast Alogrithem -
    Algorithm are based on min-edit functions because brute force comparisons will be time consuming

3) No Context Data -
     - No Context Data is given in form of sentance so as to use neural network for correction
     - No Dictionary is given for specific type of spell correction to reduce error rate
     - Real Word Errors is hard to correct without context. It is word which are in english dictionary but not suitable to use in sentance

4) No pretrained Model or inbuilt library is used like pattern.en.suggest so that customisation can be done depending on use of application

**** 
**Note**: Python code is pep8 compliant

## Tools use 
> Python 3

> Main Libraries Used -
1) numpy
2) flask
3) pandas

**** 

## Installing and Running

```sh
$ cd spell_correction_flask_application
$ pip install -r requirements.txt
``` 

For Running Flask Application
```sh
$ python webserver.py
```
Use http://0.0.0.0:5000/spellCorrect/text for web application

****
## Various Steps in approach are -

1) For removing emojis -
     - Used encoding -
    Removed word having emoji, latin or greek words by striping all non-ASCII characters

2) For removing special character, punctuation and space -
     - Used Regex -
    Removed special character punctuation and space in string and replace it with empty character

3) For removing long slang word which are used in chating like amazinggggg or finallllly. 
    - Assume in english 3 same character not occur together

4) Match of the word -
    - Cross-validate extracted word against English dictionary words
    use open source file to genrate dictionary from it and compare  
    source https://www.gutenberg.org/browse/scores/top

5) Words that didn’t match (non-dictionary words) are corrected 
    - Damerau-Levenshtein distance measures is used. 
    - It measures distance between two strings (a word and its misspelling) in terms of minimum number of basic edit operations required to transform one string to the other. Edit operations are:
    - Substitution: Substitute a single character by another (e.g, pwned →owned)
    - Deletion: Delete a single character (e.g., thew →the)
    - Addition: Add a single character (e.g., langage →language)
    - Transposition: Transpose or exchange a single pair of adjacent characters (e.g., recieve → receive)
    - 1, 2, 3 or n number of edition can be allowed depending on our error analysis
    - The amount of computations increases with number of edits allowed.
    - Assumed 2 mistakes at most can be done by user



6) Flask Application is made for requesting API
    It has following folder 
    - templates - For web application to use rest API.
        - text_read - For sending text
        - text_result - For showing result
    - data - For sample dataset
    - model - For model

****
## Future result Can be improve -
1) If context sentence is given then spell correction can be improve. It will be helpful in cases where after wrong spelling we have word which is in indian dictionary but it is not suitable to use it in sentance. It is called Real Word Errors. 
Like piece peace can be corrected 
inlaw might be in law or in-law can bd corrected
2) Dictionary of the words used in that application - mainly past words which user typed or can type depending on application if given result can be improved. These can be made in python using enchant. Custom dictionary mean like name of movies or character
3) Short form / slang type of correction can be improved more
4) Errors could be due to multiple factors including input device and ignorance of the language. Thus these factors can be used if given suitable data
5) Words with similar spelling and pronounciation can be corrected like tuf - tough