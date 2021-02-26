# Author: Rajendra L Hanagodi
# Contact: rajendra.hanagodi@ltts.com
# Date of creation:23/02/2021

'''This program performs the grep operation ,n i.e. user needs to provide word
that he / she wants to search from the given file . The final output the
opeartion is a file is created with the count and instances of
the desired
'''
import re
# assigned in the class declaration


class search_word:
    # init method or constructor
    def __init__(self):
        print("This is init")

    @staticmethod
    def opera():
        # assigned number of words
        num = int(input('enter the number input words :'))
        n = 0
        while num > n:
            # opened input file
            input_file = open("input.txt", "r")
            count = 0
            # user input words
            input_search = input("Enter the Word to be search:\n")
            input_file2 = input_file.read()
            input_file3 = re.sub(r'\W+', ' ', input_file2)
            # spliting of word by word
            file1 = input_file3.split()
            user_input_search_word = input_search + '.txt'
            # opened user input words file
            user_input_file = open(user_input_search_word, 'a')
            # to iterate on the input file
            for i in range(len(file1)):
                # using "Regular Expression"
                # able to search in user input in input file
                word = re.fullmatch(input_search, file1[i], re.M | re.I)
                # Statements to execute if user word is present
                if word:
                    count += 1
                    # writing in the user input file
                    # to write the user input word , perivious word and post word 
                    user_input_file.write(file1[i - 1] + ' ' + file1[i] + ' ' + file1[i + 1] + '\n')
            user_input_file.write("Number of times word appered in file:  ")
            user_input_file.write(str(count))
            # closed input file
            input_file.close()
            # closed user_input_file
            user_input_file.close()
            n += 1

# creating object of the class
obj = search_word()
# perform operation
obj.opera()
