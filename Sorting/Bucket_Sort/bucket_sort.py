def bucketSort(array):
    if len(array) == 0:
        return array

    # Find min and max
    min_val, max_val = min(array), max(array)

    # Number of buckets
    bucket_count = len(array)
    bucket = [[] for _ in range(bucket_count)]

    # Normalize values into bucket index
    for num in array:
        index = (num - min_val) * (bucket_count - 1) // (max_val - min_val)
        bucket[index].append(num)

    # Sort each bucket
    for i in range(bucket_count):
        bucket[i].sort(reverse=True)  # descending

    # Merge results
    result = []
    for b in bucket:
        result.extend(b)

    return result


array = [42, 32, 33, 52, 37, 47, 51]
print("Sorted Array in descending order is")
print(bucketSort(array))
