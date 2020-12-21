"""
File: boggle.py
Name:
----------------------------------------
This program recursively find all the possible answers (which length of word is longer than 4 letters)
in 4*4 boggle game
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dict = []
row1 = []
row2 = []
row3 = []
row4 = []
game_rows = {}


def main():
	"""
	TODO:
	"""
	read_dictionary()
	rows()
	build_rows()
	find_word()


def find_word():
	current = ''
	answer = []
	for x in range(4):
		for y in range(4):
			find_word_helper(x, y, current, [], answer)
	print('There are', len(answer), 'words in total.')


def find_word_helper(x, y, current, lst, answer):
	if has_prefix(current) is False:
			return

	else:
		if len(current) >= 4:
			if current in dict and current not in answer:
				print('Found', '"', current, '"')
				answer.append(current)

		for i in range(-1, 2):
			for j in range(-1, 2):
				if 0 <= x+i < 4 and 0 <= y+j < 4:
					if (x+i, y+j) not in lst:
						# choose
						lst.append((x+i, y+j))
						# explore
						find_word_helper(x+i, y+j, current+game_rows[(x+i)][y+j], lst, answer)
						# unchoose
						lst.pop()


def build_rows():
	global game_rows
	game_rows[0] = row1
	game_rows[1] = row2
	game_rows[2] = row3
	game_rows[3] = row4


def rows():
	global row1, row2, row3, row4
	#create 1st row
	s1 = input('1 row or letters: ')
	s1 = s1.lower()
	for i in range(len(s1)):
		if i+1 < len(s1) and s1[i].isalpha() and s1[i+1].isalpha():
			print('Illegal Input')
			return
	for j in range(len(s1)):
		if s1[j].isalpha():
			row1.append(s1[j])
	if len(row1) != 4:
		print('Illegal Input')
		return


	#create 2nd row
	s2= input('2 row or letters: ')
	s2 = s2.lower()
	for i in range(len(s2)):
		if i + 1 < len(s2) and s2[i].isalpha() and s2[i + 1].isalpha():
			print('Illegal Input')
			return
	for j in range(len(s2)):
		if s2[j].isalpha():
			row2.append(s2[j])
	if len(row2) != 4:
		print('Illegal Input')
		return


	#create 3rd row
	s3 = input('3 row or letters: ')
	s3 = s3.lower()
	for i in range(len(s3)):
		if i + 1 < len(s3) and s3[i].isalpha() and s3[i + 1].isalpha():
			print('Illegal Input')
			return
	for j in range(len(s3)):
		if s3[j].isalpha():
			row3.append(s3[j])
	if len(row3) != 4:
		print('Illegal Input')
		return

	#create 4th row
	s4 = input('4 row or letters: ')
	s4 = s4.lower()
	for i in range(len(s4)):
		if i + 1 < len(s4) and s4[i].isalpha() and s4[i + 1].isalpha():
			print('Illegal Input')
			return
	for j in range(len(s4)):
		if s4[j].isalpha():
			row4.append(s4[j])
	if len(row4) != 4:
		print('Illegal Input')
		return


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dict
	with open(FILE, 'r') as f:
		for line in f:
			word = line.split()
			word_s = word[0].strip()
			dict.append(word_s)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dict:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
