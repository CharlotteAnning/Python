def largest_element(numbered_list):
	largest_number = 0                                                                      # set largest_number as a variable with value 0
	for x in range(0, len(numbered_list)-1):                                                # set range to start with 0 and not include the last number
		if numbered_list[x] > numbered_list[x+1] and numbered_list[x] > largest_number:     # if the query number is greater than the next number in the list and also the largest number,
			largest_number = numbered_list[x]                                               # set that number as the largest number
		else:                                                                               # if not, continue with the loop
			continue
	if numbered_list[-1] > largest_number:                                                  # check if the last number is the largest number by comparing with largest number
		largest_number = numbered_list[-1]                                                  # can't include last number in loop as can't compare it to a next number in the list
	print(f'the largest number in your list is {largest_number}!')                          # print the largest number