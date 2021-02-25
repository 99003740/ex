# Author: Rajendra L Hanagodi
# Date of creation:23/02/2021
import re
class search_word:

    def __init__(self):
        print("This is init")

    def operation(self):
        input_file = open("input.txt", "r")                                   
        count = 0

        input_search = input("Enter the Word to be search:\n")  


        input_file2 = input_file.read()        
        input_file1 = input_file2.split()
        input_file3 = re.split(r'\W',str(input_file1))

        user_input_search_word = input_search + '.txt'

        user_input_file = open(user_input_search_word, 'a')                              
        for i in range(len(input_file1)):
            word = re.match(input_search, input_file1[i], re.M | re.I)         
            if word:
                count += 1
                user_input_file.write(input_file1[i-1]+' '+input_file1[i]+' '+input_file1[i+1]+'\n')
        user_input_file.write("Number of times word appered in file:  " + str(count))
        input_file.close()
        user_input_file.close()

obj=search_word()
obj.operation()