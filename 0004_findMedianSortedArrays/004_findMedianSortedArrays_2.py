def findMedianSortedArrays(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    total_len = m + n
    pos_1 = 0
    pos_2 = 0
    # 记录中间值
    left = right = None
    
    # 遍历到一半多1个即可（从0开始计数）
    for i in range(total_len//2+1):
        left = right
        if (pos_1 < m and (pos_2 >= n or nums1[pos_1] < nums2[pos_2])):
            right = nums1[pos_1]
            pos_1 += 1
        else:
            right = nums2[pos_2]
            pos_2 += 1

    if total_len%2 == 0:
         return (left+right)/2
    else:
        return right


if __name__ == '__main__':
    nums1 = [4,5,6]
    nums2 = [1, 2, 3, 8]
    res = findMedianSortedArrays(nums1, nums2)
    print(res)
