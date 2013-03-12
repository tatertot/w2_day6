# open file and read it
from sys import argv
script, fileinput = argv

f = open(fileinput)
read_txt = f.read()
txt = read_txt.lower()
# split the text to create a list of words
split_txt = txt.split()

# create empty dict
word_dict = {}

# loop through each word in the split_txt list, store the word and count in a dict
for v in split_txt:
	# for each word, remove punctuation from beginning and end of words
	stripped_word = v.rstrip('.,:-_;!?"()\'')
	stripped_word = stripped_word.lstrip('.,:_-"()\'')
	# test if word is already in the dict, increase count if found
	if stripped_word in word_dict:
		word_dict[stripped_word] = word_dict[stripped_word] + 1
	else:
		# otherwise add the word and word count to dict
		word_dict.setdefault(stripped_word, 1)

# word_dict now contains the word and frequency of that word as a key=>value pair
# use .items() method to create a list of tuples containing the word and count
# this results in a list of tuples (ie [('word1, 3','word2', 1)])
tupled_list = word_dict.items()

# need to reassign the values in the tuple so it's (count,value) because it's storted by the first value
# create an empty list to store the switched values of the tuples
new_list = []

for word, count in tupled_list:
	# reassign the contents of the tuple so the count is the first item and word as the second
 	new_tuple = (count, word)
 	# add the reorganized tuple to the new list
 	new_list.append(new_tuple)

# in order to sort by 2 values, need to use lambda    
# sort by secondary key (the word)
new_list.sort(key=lambda x:x[1])
# then sort by the first key (the count) and reverse
new_list.sort(key=lambda x:x[0], reverse=True)

for count, word in new_list:
	print count,word

