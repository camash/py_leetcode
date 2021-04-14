def findMedianSortedArrays(nums1, nums2):
    len_1 = len(nums1)
    len_2 = len(nums2)
    total_len = len_1 + len_2
    nums = []

    # 针对数组1为空的情况
    if len_1 == 0:
        if len_2%2 == 0:
            return (nums2[len_2//2 - 1] + nums2[len_2//2])/2
        else:
            return nums2[len_2//2]

    # 针对数组2为空的情况
    if len_2 == 0:
        if len_1%2 == 0:
            return (nums1[len_1//2 -1] + nums1[len_1//2])/2
        else:
            return nums1[len_1//2]


    # 对两个数组进行归并组合
    i = 0
    j = 0
    while len(nums) != total_len:
        # 遍历完数组1, 而数组2还有元素
        # 在比较过程中都会多加1，所以最后比较时即为长度，无需减1
        if i == len_1 and j < len_2:
            print(i,j)
            nums = nums + nums2[j:]
            break
        if j == len_2 and i < len_1:
            nums = nums + nums1[i:]
            break
        # 进行元素比较
        if nums1[i] < nums2[j]:
            nums.append(nums1[i])
            i = i+1
        else:
            nums.append(nums2[j])
            j = j+1

    if total_len%2 == 0:
         #print(total_len)
         return (nums[total_len//2 -1] + nums[total_len//2])/2
    else:
         return nums[total_len//2]


if __name__ == '__main__':
    nums1 = [4,5,6]
    nums2 = [1, 2, 3, 8]
    res = findMedianSortedArrays(nums1, nums2)
    print(res)
