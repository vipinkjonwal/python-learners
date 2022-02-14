def interchangeableRectangles(rectangles):
    ratioCount = {}
    resultCount = 0
    for i in range(len(rectangles)):
        ratio = rectangles[i][0]/rectangles[i][1]
        if ratio in ratioCount:
            ratioCount[ratio] += 1
        else:
            ratioCount[ratio] = 1

    for _,v in ratioCount.items():
        resultCount += v*(v-1)/2

    return int(resultCount)

def main():
    rectangles = [[2,8],[3,6],[10,20],[15,30]]
    print(interchangeableRectangles(rectangles))

if __name__ == '__main__':
    main()
    
        
        
                