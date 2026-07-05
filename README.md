## Analyze a News Article
This is a Python program designed for a tech start up specialising in Natural Language Processing (NLP). It performs various text analysis tasks on a given news article to extract valuable insights.

## The tasks include: 
* Counting the number of times a specific word is used.
* Identifying the most common word.
* Calculating the average length of words.
* Counting the number of paragraphs.
* Counting the number of sentences in the text.

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

## Usage
* Place the article you want to analyze in a file named news_article.txt in the same directory as pythonAssessment.py, 
* In the terminal, run "python3 pythonAssessment.py"
* You'll be prompted to enter a word to search for. Enter as many words as you'd like, one at a time. 
* Submit a blank input to finish and print the remaining results.