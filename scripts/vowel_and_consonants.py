def vowel_and_consonants(word):
	word = word.strip()                                                                       # remove trailing spaces and tabs
	word = word.lower()                                                                       # convert to lowercase for comparison to vowels
	vowel_count = 0                                                                           # set vowel count to zero 
	consonant_count = 0                                                                       # set consonant count to zero
	other_character_count = 0                                                                 # set other character count to zero
	vowels = 'a','e','i','o','u'                                                              # create tuple with vowels
	for character in word:                                                                    # loop through characters in input word
		if character.isalpha():                                                               # if the character is alphabetical
			if character in vowels:                                                           # if the character is also in vowels tuple,
				vowel_count += 1                                                              # add 1 to vowel count
			else:
				consonant_count += 1                                                          # if not in vowel tuple add to consonant count
		else:
			other_character_count += 1                                                        # if not alpabetical add to other character count
			print("your word has", other_character_count, "non alphabetical characters :)")   # print the results
	print("your word has", vowel_count, "vowels and", consonant_count, "consonants")