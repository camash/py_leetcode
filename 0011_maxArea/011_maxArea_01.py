def minArea(height):
    area = 0
    if len(height) < 2:
        return area

    i = 0
    j = len(height) - 1
    area = j * min(height[j], height[i])
    while i<j:
        # 面积的大小由短轴决定，并且移动短轴才可能获得更大的面积
        if height[i] < height[j]:
            area = max(area, (j - i)*height[i])
            i = i + 1
        else:
            area = max(area, (j - i)*height[j])
            j = j - 1

        if area == 56:
            print (i, j)

    return area

# 采用两轮循环，O(N^2)，解题超时
if __name__ == "__main__":
    print(minArea([1,8,6,2,5,4,8,3,7]))
