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
	stripped_word = v.rstrip('.,:-;!?')
	stripped_word = stripped_word.lstrip('.,:-')
	if stripped_word in word_dict:
		word_dict[stripped_word] = word_dict[stripped_word] + 1
	else:
		word_dict.setdefault(stripped_word, 1)
	# print stripped_word, word_dict[stripped_word]



tupled_list = word_dict.items()
new_list = []
print new_list


# #print sorted(tupled_list)
# sorted_word_list = {}
for word, count in tupled_list:
 	print word, count



 	
# 	#print i, v
# 	for index, tupleval in enumerate(v):
# 		count = v[1]
# 		word = v[0]
# 		#tuple2 = word
# 		sorted_word_list[count] = word

# new_sorted_list = sorted_word_list.items()
# #print new_sorted_list
# print new_sorted_list[::-1]
# final_sort = sorted(new_sorted_list)
# final_sort = new_sorted_list.sort()

	#print tuple1,tuple2
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

