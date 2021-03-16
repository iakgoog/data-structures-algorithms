def merge_sort(collection: list) -> list:
	def merge(left: list, right: list) -> list:
		def _merge():
			while left and right:
				yield (left if left[0] <= right[0] else right).pop(0)
			yield from left
			yield from right

		return list(_merge())

	if len(collection) <= 1:
		return collection
	mid = len(collection) // 2
	return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))

unsorted = [1,2,3,4,8,10,3,5,7,9,11]
print(*merge_sort(unsorted), sep=",")
