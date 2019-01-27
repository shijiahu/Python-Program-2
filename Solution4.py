# 4) In order to win the prize for most cookies sold, my friend Alice and I 
# are going to merge our Girl Scout Cookies orders and enter as one unit.
# Each order is represented by an "order id" (an integer).
# We have our lists of orders sorted numerically already, in lists. 
# Write a function to merge our lists of orders into one sorted list.
# For example:
my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19] print merge_lists(my_list, alices_list)

def merge_lists(l1, l2):
	result = []
	l1_index = 0
	l2_index = 0
	while l1_index < len(l1) and l2_index < len(l2):
		if l1[l1_index] < l2[l2_index]:
			result.append(l1[l1_index])
			l1_index += 1
		else:
			result.append(l2[l2_index])
			l2_index += 1
	if l1_index == len(l1):
		result.extend(l2[l2_index:])
	elif l2_index == len(l2):
		result.extend(l1[l1_index:])
	return result

# test1
print(merge_lists(my_list, alices_list))

# test2
my_list = [3, 4, 6, 10, 11, 15, 35]
alices_list = [1, 5, 8, 12, 14, 19, 20, 21, 22, 25]
print(merge_lists(my_list, alices_list))


