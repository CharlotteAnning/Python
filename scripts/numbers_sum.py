def numbers_sum(input_sum, input_list):
	input_sum = int(input_sum)                                                      # convert input sum to an integer just in case
	input_list = sorted(set(input_list))                                            # puts the list in numerical order without repeats
	diff = 0                                                                        # create an object 'diff' with starting value 0
	while diff < len(input_list):                                                   # while the difference between the first and last value is still lower than the input_sum
		try:
			for x in range(len(input_list)):
				if x+diff >= len(input_list):                                       # if the index of the value you are comparing the first to is out of range break and set new value of diff
					break
				elif input_list[x] + input_list[x+diff] == input_sum:               # compares two numbers in the list in a matrix format
					print(f'{input_list[x]} + {input_list[x+diff]} = {input_sum}')
				else:
					continue
			diff = diff + 1                                                         # increase the difference by one
		except IndexError:               
			print(f'x: {x} diff: {diff}')                                           # good for troubleshooting where in the loop the function is getting stuck
		except KeyboardInterrupt:
			print('command c activated')                                            # back out option
