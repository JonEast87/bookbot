def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() 
        words = file_contents.split() # Book is split into an array of it's words
        word_report = count_words(words)
        letter_report = count_letters(words)
        print_report(word_report, letter_report)

def count_words(words):
    return len(words)

def count_letters(words):
    count_letters = dict() # storing all characters/counts in dictionary
    for word in words:
        lowercase_word = word.lower() # lowercase to ensure all matching characters are counted
        letters = list(lowercase_word) # list will split each word into an array for easy iteration
        for letter in letters:
            if letter in count_letters and letter.isalpha(): # if the character exists at index
                count_letters[letter] += 1 # then increment
            elif letter.isalpha(): 
                count_letters[letter] = 1 # else we will create a new one for the first instance
    return count_letters

def print_report(words, letters):
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    for letter in letters:
        print(f"The {letter} character was found {letters[letter]} times")
    print("--- End report ---")

main()