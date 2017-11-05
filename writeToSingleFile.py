'''
Reads in all the text files and writes them to a single file.
NOTE: This file must be in the same directory as the text files.
'''

import os
out_file = open("all_text.txt", 'w')
for filename in os.listdir(os.getcwd()):
	file = open(filename, 'r')
	text = file.read()
	out_file.write(text)
	file.close()

out_file.close()