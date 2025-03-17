def anagram(input_string_1, input_string_2):
	string_1 = input_string_1.strip().lower().replace(" ","").replace("-","")                       # remove trailing tabs and spaces, convert to lowercase, remove spaces and hyphens 
	string_2 = input_string_2.strip().lower().replace(" ","").replace("-","")
	temp_string_1 = string_1                                                                        # create a temporary duplicate of string 1 to manipulate
	if len(string_1) != len(string_2):                                                              # if the strings aren't the same length then already know not anagrams
		print(f'{input_string_1} and {input_string_2} are not anagrams of eachother :(')
	else:
		while len(temp_string_1) > 0:                                                               # whilst the temporary duplicate of string 1 has atleast one letter in it:
			if string_2.find(temp_string_1[0]) < 0:                                                 # if the first letter of temp_string_1 isnt present in string_2 they aren't anagrams 
				print(f'{input_string_1} and {input_string_2} are not anagrams of eachother :(')
				break
			else:
				temp_string_1 = temp_string_1[1:]                                                   # if the letter is present, remove the first letter and repeat the comparison
		else: print(f'{input_string_1} is an anagram of {input_string_2}!')                         # once the temporary duplicate is empty then it's confirmed the strings are anagrams!