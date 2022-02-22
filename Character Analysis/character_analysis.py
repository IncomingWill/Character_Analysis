# Title: Character Analysis Program
# Program created by William Schaeffer
# CPS 313
# P. 463, Exercise 7, Character Analysis Program
# 02.08.22

# This program will read a file's contentes and determine:
    # The number of uppercase letters, lowercase numbers, digits, and whitespace characters

# imports for functions

import re                                               # import to keep whitespace on .split() function

# Main Function

def main():
    
    sentence_file = open('text.txt')                    # open text.txt

    total_word_count = 0                                # initialize count variables
    line = 0
    upper_case_count = 0
    lower_case_count = 0
    digit_count = 0
    whitespace_count = 0

    fileInput = sentence_file.readline()                # read line and store in file Input

    # while loop to read through file

    while fileInput != '':                              # while fileInput is not an empty string
        sentence_list = re.split(r'(/s_)', fileInput)   # split the sentence into a list
        word_count = len(sentence_list)                 # count the elements of the list for word count
       
        #print lines for testing
        #print('Line: ', line)
        #print(sentence_list)
        
        for word in sentence_list:                      # iterate over the list of words in sentence
            for letter in word:                         # iterate over the letters in each word
                if letter.isupper():
                    upper_case_count += 1
                if letter.islower():
                    lower_case_count += 1
                if letter.isdigit():
                    digit_count += 1
                if letter.isspace():
                    whitespace_count += 1
        
        fileInput = sentence_file.readline()            # read the next line
        
    # print total counts

    print('Upper Case: ', upper_case_count)
    print('Lower Case: ', lower_case_count)
    print('Digits: ', digit_count)
    print('Whitespace: ', whitespace_count)

main()                                                  # call main function

