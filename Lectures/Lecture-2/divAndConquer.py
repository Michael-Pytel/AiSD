def min_max(l, st, end):
    if st == end:
        minEl = l[st]
        maxEl = l[st]

    elif st + 1 == end:
        if l[st] < l[end]:
            minEl = l[st]
            maxEl = l[end]
        else:
            minEl = l[end]
            maxEl = l[st]
    else:
        mid = int(st + (end - st) / 2)
        leftMinMax = min_max(l, st, mid)
        rightMinMax = min_max(l, mid + 1, end)
        if leftMinMax[1] > rightMinMax[1]:
            maxEl = leftMinMax[1]
        else:
            maxEl = rightMinMax[1]
        if leftMinMax[0] < rightMinMax[0]:
            minEl = leftMinMax[0]
        else:
            minEl = rightMinMax[0]

    output = [minEl, maxEl]
    return output


if __name__ == "__main__":
    l = [70, 250, 50, 80, 140, 12, 14, -5]
    print(min_max(l, 0, len(l) - 1))
