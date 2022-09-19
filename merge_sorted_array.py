nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

new_list = []

if m == 0:
    new_list = nums2

elif n == 0:
    new_list = nums1

else:
    i = 0
    j = 0

    while i <= m and j <= n:

        if i == m:
            new_list += nums2[j:n]
            break

        elif j == n:
            new_list += nums1[i:m]
            break

        elif nums1[i] >= nums2[j]:
            new_list.append(nums2[j])
            j += 1

        else:
            new_list.append(nums1[i])
            i += 1

print(new_list)
