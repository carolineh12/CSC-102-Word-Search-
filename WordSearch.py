###############################################################################
# Word Search
# Dr. Jean Gourd
# Last modified on 2020-11-05
#
# A template for the main program for the programming assignment Word Search
#  (part 2).
# Requires Word.py and Grid.py.
###############################################################################

# import libraries
from Word import Word
from Grid import Grid
from sys import stdin
from random import sample, choice

# define constants
NUM_WORDS = 15              # how many words to randomly select
GRID_SIZE = 25              # the height/width of the grid
DISPLAY_SOLUTION = True     # display the solution?

######
# MAIN
######
# read the words from stdin
with open("animals.txt", "r") as f:
    words = f.read().upper().splitlines()
    
# grab a sampling of the specified number of words
words = sample(words, NUM_WORDS)

# initialize the grid

# process the words
    # randomly select an orientation for the current word

    # position the current word at the chosen orientation in the grid

# display stats (i.e., "Successfully placed X of Y words.")

# display the grid

# display the words

# if specified, display the solution

