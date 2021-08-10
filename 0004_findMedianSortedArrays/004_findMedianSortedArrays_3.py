def findMedianSortedArrays(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    # 初始化需要的中位数位置
    # 奇数是同一个结果，偶数是两个值
    left = (m + n + 1) // 2
    right = (m + n + 2) // 2

    # 测量的初始位置
    pos_1 = 0
    pos_2 = 0

    # 寻找第K小的数
    val_left = get_kth(nums1, nums2, pos_1, m - 1, pos_2, n - 1, left)
    val_right = get_kth(nums1, nums2, pos_1, m - 1, pos_2, n - 1, right)

    return (val_left + val_right) / 2


# 递归函数

def get_kth(num_list_1, num_list_2, start_1, end_1, start_2, end_2, k):
    # 保证num_list_1 一定是长于 num_list_2
    len_1 = end_1 - start_1 + 1
    len_2 = end_2 - start_2 + 1
    if len_1 < len_2:
        return get_kth(num_list_2, num_list_1, start_2, end_2, start_1, end_1, k)

    # len_2 耗尽的情况, 退出
    if len_2 == 0:
        return num_list_1[start_1 + k - 1]

    # 只找一个数的退出条件
    if k == 1:
        if num_list_1[start_1] <= num_list_2[start_2]:
            return num_list_1[start_1]
        else:
            return num_list_2[start_2]

    # 进行值的比较
    # 先获得比较的位置
    i = start_1 + min(len_1, k // 2) - 1
    j = start_2 + min(len_2, k // 2) - 1

    # i位置的值<位置的值，i被排除，继续递归, 同时k也缩减
    if num_list_1[i] < num_list_2[j]:
        return get_kth(num_list_1, num_list_2, i + 1, end_1, start_2, end_2, k - (i - start_1 + 1))
    else:
        return get_kth(num_list_1, num_list_2, start_1, end_1, j + 1, end_2, k - (j - start_2 + 1))


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    res = findMedianSortedArrays(nums1, nums2)
    print(res)

