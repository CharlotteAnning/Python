def reverse_string(string):
	my_dictionary = {}	                                                                              # create an empty dictionary
	for x in range(len(string)):                                                                      # for each letter in string, add it as a value in dictionary with keys 0 to n in reverse order
		my_dictionary[x] = string[-x]	                                                              # this is indexing! different to slicing
	my_dictionary.pop(0) 	                                                                          # remove the first key value pair as still first letter in string as there is no string[-0]
	my_dictionary[len(string)] = string[0]                                                            # add the first letter of string to new last key of dictionary
	temp = my_dictionary.values()                                                                     # assign a variable to just the letters in the dictionary
	reversed_string = str(temp).replace("dict_values([", "").replace("', '", "").replace("])", "")    # remove all characters to revert output back to string
	print(reversed_string)                                                                            # print result