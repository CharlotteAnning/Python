def longest_substring(string):
	string = string.replace(",", "").replace("'", "").replace("!", "").replace("?", "").replace("#", "").replace("(", "").replace(")", "")  # remove all special characters
	list_of_substrings = string.split()                                                                                                     # create a list of words from the input string
	for i in range(len(list_of_substrings)):                                                                                                # for word in list of words
		if len(list_of_substrings[i]) > 0:                                                                                                  # if the word isnt empty, 
			for x in range(len(list_of_substrings[i])):                                                                                     # for each character in that word,
				try:                                                                                                                        # try: if the count of the character in the word is 
					if list_of_substrings[i].count(list_of_substrings[i][x]) > 1 and x < len(list_of_substrings[i]):                        # greater than 1 and the word still isn't empty
						temp_1 = list_of_substrings[i].replace(list_of_substrings[i][x], "")                                                # remove that character entirely from the word
						temp_2 = list(temp_1)                                                                                               # convert string to a list
						temp_2.insert(x, list_of_substrings[i][x])                                                                          # so can then add just one of that character back in
						list_of_substrings[i] = str(temp_2).replace("['", "").replace("', '", "").replace("']", "")                         # convert back to a string and repeat
					else:
						continue
				except IndexError:                                                                                                          # once there is an index error i.e. the word is empty,
					continue                                                                                                                # continue 
			else:
				continue
		else:
			continue
	largest_sub_string = max(list_of_substrings, key=len)                                                                                   # retrieve the largest word in the now edited list
	position = list_of_substrings.index(largest_sub_string)                                                                                 # get the index of the largest word in the edited list
	undoctored_list_of_substrings = string.split()                                                                                          # create a new list of non edited words
	print(f'the longest substring in "{string}" without repeats is: "{undoctored_list_of_substrings[position]}"')                           # print the longest non edited word which is at the 
 	                                                                                                                                        # same position in the non edited list                                                