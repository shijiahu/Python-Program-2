# 1) Count Capital Letters
# Write a one-liner that will count the number of capital letters in a file. 
# Your code should work even if the file is too big to fit in memory.
# Assume you have an open file handle object, such as: with open(SOME_LARGE_FILE) as fh:
# count = # your code here

with open('testfile_1.txt') as fh:
	count = len([letter for letter in fh.read() if letter.isupper()])

print(count)