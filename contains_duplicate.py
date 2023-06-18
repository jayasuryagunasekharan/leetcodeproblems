def contains_duplicate(nums: list[int]) -> bool:
    hash_set = set()

    for num in nums:
        if num in hash_set:
            return True
        else:
            hash_set.add(num)
    return False

if __name__ == '__main__':
    value = contains_duplicate([1,2,3,4])
    print(value)