from sys import argv
script, filename = argv

text = open(filename).read()

text_dict = {}
#split each line into a list
line_split = text.split('\n')
line_split_sorted = sorted(line_split)

for value in line_split:
	#split line into pairs
	pair = value.split(':')

	#assign key
	restaurant_name = pair[0]
	#assign value
	rating = pair[1]
	#create new key,value pair in dictionary
	text_dict[restaurant_name] = rating

#sorted restaurant name (key) variable

#this creates a list of the sorted keys(restaurants) in the dictionary
sorted_list = sorted(text_dict)


#we need to take the list to find the sorted keys
#use the sorted key to find the value in the dictionary

for restaurant in sorted_list:
	score = text_dict[restaurant]
	print "Restaurant '%s' is rated at %s." % (restaurant, score)

