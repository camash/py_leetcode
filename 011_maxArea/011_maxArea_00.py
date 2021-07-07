def minArea(height):
    area = 0
    if len(height) < 2:
        return area
    else:
        for i in range(len(height) - 1):
            for j in range(i+1, len(height)):
                if area < (j - i) * min(height[j], height[i]):
                    area = (j - i) * min(height[j], height[i])

    return area

# 采用两轮循环，O(N^2)，解题超时
if __name__ == "__main__":
    print(minArea([1,2,1]))