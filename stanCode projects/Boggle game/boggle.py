"""
File: boggle.py
Name:Thomas
----------------------------------------
Boggle games!
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	This program find English words with >= 4 letters in a 4*4 letter matrix.
	"""
	dic1 = {}
	lst1 = []
	for i in range(4):  # Save the input letters in the data structure "dic", with x and y coordinates as the key.
		row = input(str(i + 1) + " row of letters: ").lower()
		# Constraints.
		if len(row) != 7:
			print("illegal format")
			break
		if not row[0].isalpha() or row[1] != " " or not row[2].isalpha() or row[3] != " " and not row[4].isalpha() or \
			row[5] != " " or not row[6].isalpha():
			print("illegal format")
			break
		count = 1
		for char in row:
			if char is not " ":
				lst1.append(char)
				if count in dic1:
					if i + 1 in dic1[count]:
						dic1[count][i + 1] = char
					else:
						dic1[count][i + 1] = char
				else:
					dic1[count] = {i + 1: char}
				count += 1
		if i == 3:
			start = time.time()
			dic = read_dictionary(lst1)
			results = find_boggle(dic1, dic)
			print("There are " + str(len(results)) + " words in total.")
			end = time.time()
			print('----------------------------------')
			print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_boggle(dic1, dic):
	"""
	This function determine the starting letter, and pass it's coordinate to helper function.
	:param dic1: dic, the input 4 * 4 letters.
	:param dic: dic, the organized dictionary.
	"""
	results = []
	for i in range(4):
		for j in range(4):
			starting_word = dic1[i+1][j+1]
			a = dic1[i+1][j+1]
			del dic1[i+1][j+1]
			n = find_boggle_helper(i+1, j+1, dic1, starting_word, dic, [])
			dic1[i + 1][j + 1] = a
			if len(n) >= 1:
				for k in range(len(n)):
					results.append(n[k])
	return results


def find_boggle_helper(starting_x, starting_y, dic1, current_word, dic, results):
	"""
	This function finds the possible combination using back-tracking method.
	:param starting_x: int, the x coordinate of the starting point.
	:param starting_y: int, the y coordinate of the starting point.
	:param dic1: dic, the input 4 * 4 letters.
	:param current_word: str, the currently operating word.
	:param dic: dic, the organized dictionary.
	:param results: lst, the list stored the final results.
	"""
	if len(dic1) == 0:  # No elements left in dic indicates the end of permutation.
		pass
	else:
		for i in range(-1, 2):  # Loop over the neighbors.
			if starting_x + i in dic1:
				for j in range(-1, 2):
					if i == j == 0:
						pass
					else:
						if len(current_word) >= 3:  # If word length > 3, check prefix.
							if not has_prefix(current_word, dic):
								break
						if len(current_word) >= 4:  # If word length > 4, check in dictionary.
							if searching(current_word, dic):
								if current_word not in results:
									results.append(current_word)
									print("Found \"" + current_word + "\"")
						if starting_y + j in dic1[starting_x + i]:
							# Choose
							current_word += dic1[starting_x + i][starting_y + j]
							a = dic1[starting_x + i][starting_y + j]
							del dic1[starting_x + i][starting_y + j]
							# Explore
							find_boggle_helper(starting_x + i, starting_y + j, dic1, current_word, dic, results)
							# Un-choose
							dic1[starting_x + i][starting_y + j] = a
							current_word = current_word[:-1]
	return results


def read_dictionary(lst1):
	"""
	This function transfer the dictionary file to the data structure dic with the first three letters as key.,
	Notice that the dic only transfer:
	1. The words having same length with the target word.
	2. The word contains at least 4 letters in lst1.
	:param lst1: lst, all the input letters
	:return: dic, the arranged dictionary.
	"""
	dic = {}
	with open(FILE, 'r') as f:
		for line in f:
			if 5 <= len(line) <= 16:
				count = 0
				for word in lst1:
					if word in line.strip():
						count += 1
				if count >= 4:
					b = (line.strip())[0:3]
					if b in dic:
						dic[b].append(line.strip())
					else:
						dic[b] = [line.strip()]
	return dic


def searching(word, dic):
	"""
	:param word: str, the searching word.
	:param dic: dic, the organized dictionary.
	:return: boolean.
	"""
	if word[0:3] in dic:
		if word in dic[word[0:3]]:
			return True
		else:
			return False


def has_prefix(sub_s, dic):
	"""
	:param sub_s: str, the prefix.
	:param dic: dic, the organized dictionary.
	:return: boolean.
	"""
	if len(sub_s) == 3:
		if sub_s in dic:
			return True
	else:
		for word in dic[sub_s[0:3]]:
			if word.startswith(sub_s):
				return True
	return False


if __name__ == '__main__':
	main()
