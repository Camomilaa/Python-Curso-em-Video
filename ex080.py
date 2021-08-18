nums = []
for c in range(0,5):
    n = int(input('Digite um número: '))
    if c == 0:
        nums.append(n)
    else:
        if n < min(nums):
            nums.insert(0,n)
        elif n in nums:
            find = nums.index(n)
            nums.insert(find + 1, n)
        else:
            nums.append(n)
print(nums)