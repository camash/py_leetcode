def merge(nums1, m,  nums2 , n):
    sorted_num = []
    p1, p2 = 0, 0
    while p1 < m or p2 < n:
        if p1 == m:
            sorted_num.append(nums2[p2])
            p2 += 1
        elif p2 == n:
            sorted_num.append(nums1[p1])
            p1 += 1
        elif nums1[p1] <= nums2[p2]:
            sorted_num.append(nums1[p1])
            p1 += 1
        else:
            sorted_num.append(nums2[p2])
            p2 += 1
    nums1[:] = sorted_num



if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)