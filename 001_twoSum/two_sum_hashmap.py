
def two_sum_hashmap(nums, target):
    # init a hashmap, put num value as key, return postion as value
    pos_dict = {}
    for i in range(len(nums)):
        anticipate_val = target - nums[i]
        if anticipate_val in pos_dict:
            return [i, pos_dict[anticipate_val]]
        # for each item, revesed key and value, put into dict
        pos_dict[nums[i]] = i



if __name__ == '__main__':
     input_list = [3, 4, 3]
     sum_int = 6
     print(two_sum_hashmap(input_list, sum_int))
