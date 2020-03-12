import os
import random
import string
import sys
import time
def write_random_lines(filename, num_of_lines, size_of_words):
    """
    Adds lines with random words to a file
    :param filename: the filename
    :param num_of_lines: number of lines to be added
    :param size_of_words: size of words in each line
    :return: void
    """
    i=0
    with open(filename,'a') as f:
        while(i < num_of_lines):
            f.write(''.join([random.choice(string.ascii_letters) 
                                   for i in range(random.randrange(0,size_of_words))])+'\n')
            i=i+1
filename = "temp_words_3.txt"
write_random_lines(filename, 5000000, 40)
while(os.path.getsize(filename) < 1*1024*1024*1024):
    write_random_lines(filename,5000000, 40)
print("Done")
