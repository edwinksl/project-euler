#!/usr/bin/env python


def get_max_path_sum(args):
    tree = get_tree(args)
    n = len(tree)
    sums = [0]*n
    sums[0] = tree[0][0][0]  # get root
    for i in range(1,n):
        sums_copy = sums.copy()
        for j, node in enumerate(tree[i]):
            child = node[0]
            if j == 0:
                sums[j] = child + sums_copy[j]
            elif j == i:
                sums[j] = child + sums_copy[j-1]
            else:
                sums[j] = child + max(sums_copy[j], sums_copy[j-1])
    return max(sums)


def get_tree(args):
    tree = {}
    for i, row in enumerate(args):
        tree[i] = []
        if i == 0:
            tree[i].append(row)
            continue
        parents = args[i-1]
        for j in range(i+1):
            if j == 0:
                node = [row[j], parents[j]]
            elif j == i:
                node = [row[j], parents[j-1]]
            else:
                node = [row[j], parents[j-1], parents[j]]
            tree[i].append(node)
    return tree

# args = [[3],
#         [7, 4],
#         [2, 4, 6],
#         [8, 5, 9, 3]]
args = [[75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
print(get_max_path_sum(args))
