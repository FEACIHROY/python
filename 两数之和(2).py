nums = [3,3]
target = 6
for i in range(0,len(nums)):
    a = target - nums[i]
    for n in range(0,len(nums)):
        if a == nums[n]:
            if i > n:
                print([i,n])