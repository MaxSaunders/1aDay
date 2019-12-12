"""
Write a program that takes a list as an input and then returns the a sorted list with
only unique values meaning if there is more than one of a value the copies are removed
"""

def unique_sort(lst):
	lst.sort()
	if len(lst) == 0 or len(lst) == 1:
		return lst
	temp = []
	j = 0
	n = len(lst)
	for i in range(n - 1):
		if lst[i] != lst[i + 1]:
			temp.append(lst[i])
			
	temp.append(lst[n - 1])
	return temp
			
			
print(unique_sort([1,1,2,2,4,3,5,7,7]))