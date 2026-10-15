from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Return the indices of the two distinct elements in `nums` that sum to `target`.
        Args:
            nums: List of integers (length >= 2).
            target: The required sum.

        Returns:
            A list [i, j] with i < j such that nums[i] + nums[j] == target.

        Time:  O(n), one pass, and each hash map lookup/insert is O(1) on average.
        Space: O(n), the map stores up to n entries in the worst case.
        """
        seen: dict[int, int] = {}  # value -> index where it was first seen

        for i, num in enumerate(nums):
            complement = target - num

            # Look up before inserting so an element can't pair with itself
            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        raise ValueError("No two elements sum to the target.")