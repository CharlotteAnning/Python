# Python
This is the repository showcasing some of my work with python :)

## 'longest_substring' is a function I wrote that takes any length string with special characters and returns the longest substring (word) without repeating letters
```
def longest_substring(string):
	string = string.replace(",", "").replace("'", "").replace("!", "").replace("?", "").replace("#", "").replace("(", "").replace(")", "")
	list_of_substrings = string.split()
	for i in range(len(list_of_substrings)):
		if len(list_of_substrings[i]) > 0:
			for x in range(len(list_of_substrings[i])): # e.g. hello = 5 so x goes up to 4
				try:
					if list_of_substrings[i].count(list_of_substrings[i][x]) > 1 and x < len(list_of_substrings[i]):
						temp_1 = list_of_substrings[i].replace(list_of_substrings[i][x], "")
						temp_2 = list(temp_1)
						temp_2.insert(x, list_of_substrings[i][x])
						list_of_substrings[i] = str(temp_2).replace("['", "").replace("', '", "").replace("']", "")
					else:
						continue
				except IndexError:
					continue
			else:
				continue
		else:
			continue
	largest_sub_string = max(list_of_substrings, key=len)
	position = list_of_substrings.index(largest_sub_string)
	undoctored_list_of_substrings = string.split()
	print(f'the longest substring in "{string}" without repeats is: "{undoctored_list_of_substrings[position]}"')
```
example usage:
```
>>>longest_substring("This is a test string!")
the longest substring in "This is a test string" without repeats is: "string"
```

## reverse_string is a function I used to reverse a string without using the reverse() built in function or slicing
```
def reverse_string(string):
	my_dictionary = {} 
	for x in range(0,len(string)):
		my_dictionary[x] = string[-x]	 # <- this is indexing ! (different to slicing)
	my_dictionary.pop(0)
	my_dictionary[len(string)] = string[0]   
	temp = my_dictionary.values()
	reversed_string = str(temp).replace("dict_values([", "").replace("', '", "").replace("])", "")
	print(reversed_string)
```
example usage:
```
>>> reverse_string("hello world")
'dlrow olleh'
```
