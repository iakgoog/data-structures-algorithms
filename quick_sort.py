from typing import List

def quick_sort(collection: list) -> list:
	if len(collection) < 2:
		return collection
	pivot = collection.pop()
	greater: List[int] = []
	lesser: List[int] = []
	for element in collection:
		(greater if element > pivot else lesser).append(element)
	return quick_sort(lesser) + [pivot] + quick_sort(greater)

unsorted = [9,6,5,0,8,2,4,7]
print(quick_sort(unsorted))
