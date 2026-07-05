# Import modules that allow us to use RegEx and libraries
import re 
import string


# Function that counts the number of occurences of a specific word in the article
def count_specific_word(text, word):
    words = text.split() # breaks texts into a list of words
    count = 0
    for w in words:
        if w == word:
            count += 1
    return count #Edge Case: If no matches are found will return 0

# Function  that identifies the most common word in the article
def identify_most_common_word(text):
    if not text:
        return None #Edge Case: Empty string should returns None
    words = text.split()
    frequencies = {} # Dictionary that tallys word count
    for w in words:
        if w in frequencies:
            frequencies[w] += 1 # Increases if a word has appeared before
        else:
            frequencies[w] = 1 # Registers a word for the first time

    most_common_word = None
    highest_count = 0
    for w, freq in frequencies.items():
        if freq > highest_count: # Tracks the highest count
            highest_count = freq
            most_common_word = w
    return most_common_word

# Function that calculates the average length of words in the article
def calculate_average_word_length(text):
    if not text:
        return 0 # Edge Case: If string is empty return 0
    
    words = text.split()
    total_length = 0
    for w in words:
        cleaned_word = ""
        for char in w:
            if char not in string.punctuation: #ignore punctuation before measuring length
                cleaned_word += char
        total_length += len(cleaned_word)
    return total_length / len(words) # Gives the average word length

# Function that count the number of paragraphs in the article
def count_paragraphs(text):
    if text == "":
        return 1 # Edge Case: If string is empty then return 1
    paragraphs = re.split(r'\n\s*\n', text.strip()) # Ignores blank lines
    return len(paragraphs) # Shows length of paragraph

# Function that that counts the number of sentences in the article
def count_sentences(text):
    if text =="":
        return 1 # Edge Case: If string is empty then return 1
    parts = re.split(r'[.!?]', text)
    sentences = [p for p in parts if p.strip() != ""] 
    return len(sentences) # Shows length of sentences

# Function that reads article text and displays results
def main ():
    with open('news_article.txt', 'r') as file:
        text = file.read() # Loads article as a string
    word = input("Enter a word to search for: ")
    while word != "": #Loop until a balnk input is entered
        result = count_specific_word(text, word)
        print(f"The word '{word}' appears {result} times.")
        word = input("Enter another word or press 'enter' to finish: ")

# Displays the remaining results once loop is exited      
    print(f"The most common word is: {identify_most_common_word(text)}")
    print(f"The average word length is: {calculate_average_word_length(text)}")
    print(f"The number of paragraphs is: {count_paragraphs(text)}")
    print(f"The number of sentences is: {count_sentences(text)}")

if __name__ == "__main__":
    main()


