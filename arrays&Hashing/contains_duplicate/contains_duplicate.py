# Brute Force
def containsDuplicate_BF(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def containsDuplicate_sorting(nums: list[int]) -> bool:
    nums.sort()
    for i in range(len(nums)):
        if i == 0:
            continue
        if nums[i] == nums[i - 1]:
            return True
    return False


def containsDuplicate_set(nums: list[int]):
    return len(nums) != len(set(nums))


def containsDuplicate(nums: list[int]):
    return containsDuplicate_BF(nums)
    # return containsDuplicate_sorting(nums)
    # return containsDuplicate_set(nums)


print(containsDuplicate([1, 2, 3, 1]))
print(containsDuplicate([1, 2, 3, 4]))
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
print(containsDuplicate([1, 11, 3, 4, 13, 2, 14, 12, 1]))
