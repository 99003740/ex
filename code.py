# Author: Rajendra L Hanagodi
# Date of creation:23/02/2021

import re
input_file = open("input.txt", "r")                                   # reading the input file
count = 0
input_file2 = input_file.read()
input_search = input("Enter the Word to be search:\n") # user input required word
input_file1 = input_file2.split()
user_input_search_word = input_search + '.txt'
user_input_file = open(user_input_search_word, "w+")
for i in range(len(input_file1)):
    word = re.match(input_search, input_file1[i], re.M | re.I)         # finding all the user input required word from the input file
    if word:
        count += 1
        user_input_file.write(input_file1[i-1]+' '+input_file1[i]+' '+input_file1[i+1]+'\n')


user_input_file.write(str(count))













#number_of_times_word_appered = len(word)                              # counting the number of times input word is repeating
# print(word)
# print(number_of_times_word_appered)

#user_input_search_word = input_search+'.txt'

#user_input_file = open(user_input_search_word, "w+")

#user_input_file.writelines(str(word)+"\n")

#user_input_file.write(str(number_of_times_word_appered))
