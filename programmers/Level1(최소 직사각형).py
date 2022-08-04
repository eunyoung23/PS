#case1
def solution(sizes):
    arr1 = []
    arr2 = []

    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            arr1.append(sizes[i][0])
            arr2.append(sizes[i][1])
        else:
            arr1.append(sizes[i][1])
            arr2.append(sizes[i][0])

    return max(arr1) * max(arr2)
