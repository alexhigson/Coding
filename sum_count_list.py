def count_positives_sum_negatives(arr):
    if not arr:
        return []
    else:
        positive_count = len([i for i in arr if i > 0])
        negative_sum = sum(i for i in arr if i < 0)
        return [positive_count, negative_sum]
print(count_positives_sum_negatives([11, 9, 3]))