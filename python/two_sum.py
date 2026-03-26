def two_sum(nums, target):
    """
    Find indices of two numbers that add up to target.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_map:
            return [num_map[complement], i]

        num_map[num] = i

    return []
