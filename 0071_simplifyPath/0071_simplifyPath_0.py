def simplifyPath(path):
    path_list = path.split('/')
    print(path_list)
    res_list = []
    for item in path_list:
        if item == '':
            continue
        # .. 往前退一格
        elif item == '..':
            res_list = res_list[:-1]
        elif item == '.':
            continue
        else:
            res_list.append(item)

    print(res_list)
    return '/' + '/'.join(res_list)


if __name__ == '__main__':
    input = '/a/./b/../../c/'
    output = simplifyPath(input)
    print(output)



