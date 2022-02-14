def offeringsOffered(templeHeights):
    numberOfTemples = len(templeHeights)
    increasingHeightList = [0 for _ in range(numberOfTemples)]
    decreasingHeightList = [0 for _ in range(numberOfTemples)]
    result = [0 for _ in range(numberOfTemples)]

    increasingHeightList[0] = 1
    decreasingHeightList[-1] = 1

    # update increasingHeights
    for i in range(1, len(templeHeights)):
        if templeHeights[i] > templeHeights[i-1]:
            increasingHeightList[i] = increasingHeightList[i-1] + 1
        else:
            increasingHeightList[i] = 1

    print(increasingHeightList)

    # update decreasingHeights
    for i in range(len(templeHeights)-2, -1, -1):
        if templeHeights[i] > templeHeights[i+1]:
            decreasingHeightList[i] = decreasingHeightList[i+1] + 1
        else:
            decreasingHeightList[i] = 1

    print(decreasingHeightList)

    # populate result
    for i in range(len(result)):
        if increasingHeightList[i] > decreasingHeightList[i]:
            result[i] = increasingHeightList[i]
        else:
            result[i] = decreasingHeightList[i]

    print(result)


def main():
    templeHeights = list(map(int, input().split()))
    offeringsOffered(templeHeights)


if __name__ == '__main__':
    main()
