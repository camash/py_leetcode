# 暴力解法

直接转换str类型，然后进行逆序后再转换为int。
进行幂指运算使用`pow()`函数。

# 整数求余

通过求余依次获得高位，然后判断`n-1`位时的值来判断是否溢出，这样也避免了整数转换后就出现溢出的情况。