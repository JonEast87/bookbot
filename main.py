def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() 
        # Book is split into an array of it's words
        words = file_contents.split() 
        word_report = count_words(words)
        letter_report = count_letters(words)
        print_report(word_report, create_list(letter_report))

def bubbleSort(letters):
    # Capturing length needed for the loops
    sorted_letters = len(letters)
    # The outer loop will increment after each pass through
    # n-1 is to ensure loop stops at the second to last index for the final check
    for i in range(sorted_letters-1):
        for j in range(sorted_letters-i-1):
            # Standard conditional check for greater than
            if letters[j]["num"] > letters[j + 1]["num"]:
                # Swapping of larger for smaller
                letters[j]["num"], letters[j + 1]["num"] = letters[j+1]["num"], letters[j]["num"]

    return letters

def count_words(words):
    return len(words)

def count_letters(words):
    # storing all characters/counts in dictionary
    count_letters = dict() 
    for word in words:
        # lowercase to ensure all matching characters are counted
        lowercase_word = word.lower() 
        # list will split each word into an array for easy iteration
        letters = list(lowercase_word) 
        for letter in letters:
            # if the character exists at index
            if letter in count_letters and letter.isalpha(): 
                # then increment
                count_letters[letter] += 1 
            elif letter.isalpha(): 
                # else we will create a new one for the first instance
                count_letters[letter] = 1 
    return count_letters

# Repalcing dictionary/values to list of dictionary/values for an easy sort
def create_list(letters):
    count_letters_list = []
    for letter in letters:
        # dictionaries will be added. they contain the l and value
        new_dict = {"letter": letter, "num": letters[letter]} 
        count_letters_list.append(new_dict)

    # Implemented a bubbleSort to replace .sort()
    sorted_letters = bubbleSort(count_letters_list)
    return sorted_letters

def print_report(words, letters):
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    for letter in letters:
        print(f"The {letter['letter']} character was found {letter['num']} times")
    print("--- End report ---")

main()