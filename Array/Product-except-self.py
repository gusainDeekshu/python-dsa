def ProductExceptSelf(nums):
    n=len(nums)
    answer=[1]*n
    
    # Step 1: multiply all elements **to the left** of i
    #    nums = [1, 2, 3, 4]
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]

    

    right_product = 1
    for i in reversed(range(n)):
        answer[i] *= right_product
        right_product *= nums[i]

    return answer




nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]

print(ProductExceptSelf(nums))