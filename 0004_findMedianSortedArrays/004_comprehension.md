# 最直接

因为使用Python，然后又是求中位数，一开始便想到了调numpy。
所以一句话就可以返回结果`return np.median(nums1 + nums2)`

当然这样子，可能不符合性能要求，也没有利用到输入数组是已经排序的条件。


# 对两个数组排序组合

利用有序的特性进行组合，需要处理数组为空和提前遍历完成的情况。
循环次数为(len(nums1)+ len(nums2)), 所以空间复杂度为O(m+n)

# 在第二步的基础上，减少组合新数组的步骤

通过直接记录中间两个元素的值实现中位数的计算，在两个数组都有序的情况下，
不用遍历完全部的数组元素。

# 寻找第k小的数

要实现`log(m+n)`，必须使用二分法，需要使用递归的方式实现，
通过寻找数组中中间位置的数据，基于有序的规则，每次在不同的数组中获取`k/2`的数，
小的整个被排除，在剩下的继续寻找，同时k也得到缩减。


递归的退出条件是k=1时获得最小的元素，或者其中一个数组遍历完成后，直接取另一个数组中第K小的数。