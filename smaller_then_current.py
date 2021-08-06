nums = [8,1,2,2,3]
res = []


for num in nums:
    count = 0
    for n in nums:
        if num > n:
            count += 1
    res.append(count)
print(res)