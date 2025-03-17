def missing_number(query_list):
	actual_length = len(query_list) + 1                                     # create list length including the missing number
	if query_list[1] - query_list[0] == query_list[2] - query_list[1]:      # find the increment if the missing number isnt one of the first 3 numbers
		increment = query_list[1] - query_list[0]                           # difference between two numbers you know aren't the missing number
	elif query_list[2] - query_list[1] == query_list[3] - query_list[2]:    # if the missing number is one of the first three numbers, 
		increment = query_list[2] - query_list[1]                           # use the 2nd, 3rd and 4th numbers to find the increment
	actual_list = []                                                        # create an empty list
	for x in range(1,query_list[-1]+1,increment):                           # set the range from 1 to last list element (included) works even with no missing number - don't use len()
		actual_list.append(x)                                               # create list including missing number, with the increment found earlier
	for x in range(1,len(actual_list)):                                     # don't use actual_length as if no missing number will be indexing error
		if query_list[x] == actual_list[x]:                                 # iterate through lists until the numbers don't match
			continue
		else:
			print('The missing number is:', actual_list[x])                 # print the missing number
			break
	else:
		print("There is no missing number!")                                # handle the instance of no missing number