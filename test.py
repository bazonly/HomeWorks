

nums = [2, 11, 15, 7]
nums.sort()
nums_dict = {}
for num in nums:
    nums_dict[nums.index(num)] = num
print(nums_dict)

if 9-nums[0] in nums:
    print(nums[0], nums[nums.index(9-nums[0])])