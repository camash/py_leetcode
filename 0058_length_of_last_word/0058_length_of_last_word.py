def lengthOfLastWord(s: str):
    str_list = s.split(' ')
    for i in range(len(str_list)-1,-1, -1):
        if len(str_list[i]) > 0:
            return len(str_list[i])
    return 0


if __name__ == "__main__":
    input = "   fly me   to   the moon  "
    output = lengthOfLastWord(input)
    print(output)