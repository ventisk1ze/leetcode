jewels = "aA"
stones = "aAAbbbb"
count = 0
for jewel in jewels:
    for stone in stones:
        if jewel == stone:
            count += 1
print(count)