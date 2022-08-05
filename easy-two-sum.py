# Para descobrir os números que somados são igual ao valor do target, podemos fazer um loop duplo, que analisará item por item.
# Este é um método com o tempo de complexidade O(n²), pois a complexidade aumenta ao quadrado a cada item incluído na lista

nums = [3, 3]
target = 6

indexes = []
      
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums [j] == target:
            indexes.append(i)
            indexes.append(j)
            
print(indexes)
