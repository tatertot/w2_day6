#open file and read it
from sys import argv

script, fileinput = argv

opened = open(fileinput)

read_txt = opened.read()

txt = read_txt.lower()

split_txt = txt.split()

word_dict = {}
# split the text 

for i, v in enumerate(split_txt):
	stripped_word = v.rstrip('.,:-;')
	stripped_word = stripped_word.lstrip('.,:-')
	if stripped_word in word_dict:
		word_dict[stripped_word] = word_dict[stripped_word] + 1
	else:
		word_dict.setdefault(stripped_word, 1)
	print stripped_word, word_dict[stripped_word]

#words as keys
#values as count		



# iterate over list of words

# strip the text to remove punctuation


# test if key(word) exists

# if it doesn't exists create set default

# if it does, increase the value by one



# string.split()
# string.strip()
# dict.setdefault()
# dict.iteritems()

