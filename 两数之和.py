nums = [2,7,11,15]
target = 9
for i in nums:
        for j in nums:
                if i + j == target:
                        if i < j:
                                a = i
                                b = j
                        else:
                                b = i
                                a = j
c = nums.index(a)
e = c
nums[e] = 'x'
d = nums.index(b)
lists = [c,d]
print(lists)
