## Analyze a News Article
This is a Python program designed for a tech start up specialising in Natural Language Processing (NLP). It performs various text analysis tasks on a given news article to extract valuable insights.

## The tasks include: 
* Counting the number of times a specific word is used.
* Identifying the most common word.
* Calculating the average length of words.
* Counting the number of paragraphs.
* Counting the number of sentences in the text.

## Functions used to complete the tasks above:
* count_specific_word(text, word) — takes the text to search and a target word, returning how many times it occurs as an integer. Returns 0 if there's no match.
* identify_most_common_word(text) — takes the text and returns the most frequently occurring word as a string. Returns None for an empty string.
* calculate_average_word_length(text) — takes the text and returns the average word length as a float, excluding punctuation and special characters. Returns 0 for an empty string.
* count_paragraphs(text) — takes the text and returns the number of paragraphs as an integer, where paragraphs are defined by blank lines separating blocks of text. Returns 1 for an empty string.
* count_sentences(text) — takes the text and returns the number of sentences as an integer, where sentences are defined by periods, exclamation marks, and question marks. Returns 1 for an empty string.

## Project Structure
├── pythonAssessment.py
├── news_article.txt
├── requirements.txt

## Requirements
* Python 3
* No external dependencies are required to run the program. Imports 're' and 'string' which are both part of the Python standard library.

## Installation of Python Environment
* python3 -m venv .venv
* source .venv/bin/activate 
* pip install -r requirements.txt

## Usage and testing
* Place the article you want to analyze in a file named news_article.txt in the same directory as pythonAssessment.py.
* In the terminal, run "python3 pythonAssessment.py"
* You'll be prompted to enter a word to search for. Enter as many words as you'd like, one at a time. 
* Submit a blank input to finish and print the remaining results.

## Author
Eddie Njeru
