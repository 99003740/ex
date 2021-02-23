#

import re
input_file= open("input.txt","r")                                   #reading the input file

input_search=input("Enter the Word to be search:\n")                #user input requried word

word=(re.findall(input_search,input_file.read(),re.M|re.I))         #finding all the user input requried word from the input file

number_of_times_word_appered=len(word)                              #counting the number of times input word is repeating
#print(word)
#print(number_of_times_word_appered) 
   
user_input_search_word=input_search+'.txt'

user_input_file=open(user_input_search_word,"w+")

user_input_file.writelines(str(word )+"\n" )

user_input_file.write(str(number_of_times_word_appered))