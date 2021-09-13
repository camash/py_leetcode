import math
def numberOfBoomerangers(points: list):
    res = 0
    for i in range(len(points)):
        dist_dict = {}
        for j in range(len(points)):
            # 确定i后，j为其余点
            if i == j:
                continue
            tmp_dist = cal_dist2(points[i],points[j])
            if tmp_dist in dist_dict.keys():
                dist_dict[tmp_dist] += 1
            else:
                dist_dict[tmp_dist] = 1
        # 以i为端点的回旋距离，可互换位置，因此是排列
        for y in dist_dict.values():
            if y>1:
                res += math.perm(y,2)

    return res



def cal_dist2(a: list, b: list):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2


if __name__ == '__main__':
    input = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
    output = numberOfBoomerangers(input)
    print(output)

