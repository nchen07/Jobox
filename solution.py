#Author: Nolan Chen
#Date: 11 March 2019
#Subject: Jobox Coding Challenge

#import statements
import urllib.request
import re
#open and import dictionary
f = urllib.request.urlopen('https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt')
#store dictionary words
d = []
for line in f:
	#import words into dictionary
	temp = (re.sub(r'^b\'', "", str(line.rstrip())))
	d.append(re.sub(r'\'$', "", temp))

#for testing purposes
sample_input = '''3
				  c j e
				  e a o
				  i t e'''

#main function
def boggle(input_string):
	split = input_string.split('\n')
	size = split[0]
	grid = []
	#keep track of all words
	final_word_list = []
	#build the grid in a 2x2 matrix
	for i in range(1, len(split)):
		grid.append(re.sub(r'\s*', '', split[i]))
	#helper function to recursively find the words by searching letter by letter
	#accepts curr - current sequence of letters, last_in - an array containing the cubes that have been used
	#and pos - current position to search for words from 
	def helper(curr, last_in, pos):
		x = pos[0]
		y = pos[1]
		word = curr
		word_list = []
		#test the full grid, left up diagonal
		#if statement ensures that left up diagonal exists, and that it hasn't already been used
		if x-1 >= 0 and y-1 >= 0 and [x-1, y-1] not in last_in:
			#add the new letter to the word
			new_word = word + grid[x-1][y-1]
			#make sure the word is at least 3 letters long and is a word before appending it to the list of words
			if len(new_word) >= 3:
				if new_word in d:
					word_list.append(new_word)
			#add all words found in recursive search of more positions
			word_list += helper(new_word, last_in + [pos] ,[x-1, y-1])
		#above
		if y-1 >= 0 and [x, y-1] not in last_in:
			new_word = word + grid[x][y-1]
			if len(new_word) >= 3:
				if new_word in d:
					word_list.append(new_word)
			word_list += helper(new_word,  last_in + [pos] , [x, y-1])
		#right up diagonal
		if y-1 >= 0 and x+1 < len(grid) and [x+1, y-1] not in last_in:
			new_word = word + grid[x+1][y-1]
			if len(new_word) >= 3:
				if new_word in d:
					word_list.append(new_word)
			word_list += helper(new_word,  last_in + [pos] , [x+1, y-1])
		#right
		if x+1 < len(grid) and [x+1, y] not in last_in:
			new_word = word + grid[x+1][y]
			if len(new_word) >= 3:
				if new_word in d:
					word_list.append(new_word)
			word_list += helper(new_word,  last_in + [pos] , [x+1, y])
		#right down diagonal
		if y+1 < len(grid) and x+1 < len(grid) and [x+1, y+1] not in last_in:
			new_word = word + grid[x+1][y+1]
			if len(new_word) >= 3:
				if new_word in d:
					word_list.append(new_word)
			word_list += helper(new_word,  last_in + [pos] , [x+1, y+1])
		#down
		if y+1 < len(grid) and [x, y+1] not in last_in:
			new_word = word + grid[x][y+1]
			if len(new_word) >= 3: 
				if new_word in d:
					word_list.append(new_word)
			word_list += helper(new_word,  last_in + [pos] , [x, y+1])
		#left down diagonal
		if x-1 >= 0 and y+1 < len(grid) and [x-1, y+1] not in last_in:
			new_word = word + grid[x-1][y+1]
			if len(new_word) >= 3:
				if new_word in d:
					word_list.append(new_word)
			word_list += helper(new_word,  last_in + [pos] , [x-1, y+1])
		#left 
		if x-1 >= 0 and [x-1, y] not in last_in:
			new_word = word + grid[x-1][y]
			if len(new_word) >= 3:
				if new_word in d:
					word_list.append(new_word)
			word_list += helper(new_word,  last_in + [pos] , [x-1, y])
		return word_list
	#for each position on the grid, search for words you can create
	for i in range(0, len(split)-1):
		for j in range(0, len(split)-1):
			curr = grid[i][j]
			final_word_list += helper(curr, [[-1, -1]], [i, j])
	return set(final_word_list)

boggle(sample_input)
