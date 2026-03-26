def contains_duplicate(nums):
    """
    Check if array contains duplicates.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return len(nums) != len(set(nums))
