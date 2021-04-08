

def two_sum_basic(nums, target):
    len_nums = len(nums)
    for i in range(len_nums):
         for j in range(i+1, len_nums):
             if nums[i] + nums[j] == target:
                 return [i, j]


if __name__ == '__main__':
     input_list = [2,7,11,15]
     sum_int = 9
     print(two_sum_basic(input_list, sum_int))
