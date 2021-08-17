def j_21():
    a = [2, 2, 4, 2, 3, 6, 2]
    for i in a:
        if a.count(i) >= len(a) / 2:
            print(i, "是主要元素")
            break


def j_21_2():
    nums = [1, 2, 3, 2, 3, 6, 2, 2, 2]

    # 对抗阶段
    major = nums[0]
    count = 0
    for each in nums:
        if count == 0:
            major = each
        if each == major:
            count += 1
        else:
            count -= 1

    # 统计阶段
    if nums.count(major) > len(nums) / 2:
        print("主要元素是：", major)
    else:
        print("不存在主要元素。")


def j_22():
    nums = [1, 2, 3, 2, 3, 2, 2, 2, 6]
    major = nums[0]
    count = 0
    for i in nums:
        if count == 0:
            major = i
        if i == major:
            count += 1
        else:
            count -= 1
    if nums.count(major) > len(nums) / 3:
        print("第一主要元素是", major)
        for each in nums:
            if each == major:
                nums.remove(each)
        nums.remove(major)
        major = nums[0]
        count = 0
        for i in nums:
            if count == 0:
                major = i
            if i == major:
                count += 1
            else:
                count -= 1
        if nums.count(major) > len(nums) / 3:
            print("第二主要元素是", major)
    else:
        print("不存在主要元素")


def j_23():
    import random
    matrix = [i for i in range(88)]
    for each in range(len(matrix)):
        matrix[each] = [i for i in range(88)]
    for each in range(88):
        for i in range(88):
            matrix[each][i] = random.randint(0, 1024)
    admit = int(input("请输入1个待匹配的整数： "))
    answer = []
    for each in matrix:
        for i in each:
            if i == admit:
                answer.append([matrix.index(each), each.index(i)])
    for each in answer:
        for i in each:
            print(i, end=" ")
        print()
    matrix = [[10, 36, 52],
              [33, 24, 88],
              [66, 76, 99]]
    for row in matrix:
        for col in row:
            compare = []
            for each in matrix:
                compare.append(each[row.index(col)])
            compare.remove(col)
            for i in compare:
                if col <= i:
                    break
                row_2 = row.copy()
                row_2.remove(col)
                for e in row_2:
                    if col > e:
                        break
                    print(col, "是幸运数字")


def j_24():
    words = ["Great", "FishC", "Brilliant", "Excellent", "Fantastic"]
    i = [each for each in words if each[0] == "F"]
    print(i)
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flatten = [col for row in matrix for col in row]
    print(flatten)
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    diag = [i * matrix[i][i] for i in range(len(matrix))]
    print(diag)
    diag_1 = [matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]
    print(diag_1)
    yang = [[1]]
    i = 1
    j = 0
    while i < 10:
        yang.append([])
        if j == 0:
            yang[i].append([])
            yang[i][j] = 1
            j += 1
        elif j == i:
            yang[i].append([])
            yang[i][j] = 1
            j = 0
            i += 1
        else:
            yang[i].append([])
            yang[i][j] = yang[i - 1][j - 1] + yang[i - 1][j]
            j += 1
    space = "  "
    count = 10
    for each in yang:
        print(end=space * count)
        for i in each:
            print(i, end="   ")
        print()
        count -= 1



j_24()
