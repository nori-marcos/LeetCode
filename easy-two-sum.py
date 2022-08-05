nums = [3, 3]
target = 6

indexes = []
      
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums [j] == target:
            indexes.append(i)
            indexes.append(j)
            
print(indexes)
