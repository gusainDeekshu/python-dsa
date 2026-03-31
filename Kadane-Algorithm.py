def max_subarray(nums):
    if not nums:
        return 0

    max_current = max_global = nums[0]

    for num in nums[1:]:
        print("num:", num, "max_current + num:", max(num, max_current + num))  # Debug

        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)
        print("num:", num, "max_current:", max_current, "max_global:", max_global)  # Debug

    return max_global

# Example usage
nums = [-2,1,-3,4,-1,2,1,-5,4]
print("Maximum Subarray Sum:", max_subarray(nums))