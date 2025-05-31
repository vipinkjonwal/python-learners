import math

def printArrays(arr):
    r = len(arr)
    for i in range(r):
        c = len(arr[i])
        if i%2 == 0:            
            for j in range(c):
                print(arr[i][j], end=" ")
        else:
            for j in range(c-1,-1,-1):
                print(arr[i][j], end=" ")
        print()
        
def transpose(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
    print(arr)

def setZeroes(matrix):
    m,n = len(matrix), len(matrix[0])
    row = set()
    col = set()
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)
    
    for i in range(m):
        for j in range(n):
            if i in row or j in col:
                matrix[i][j] = 0
    
    print(matrix)
                
def coinChange(coins: list[int], amount: int) -> int:
    dp = [math.inf]*(amount+1)
    dp[0] = 0
    
    for n in range(1,amount+1):
        for a in coins:
            if n-a >= 0:
                dp[n] = min(dp[n], 1+dp[n-a])
    return dp[amount] if dp[amount] != math.inf else -1
    
def lenLIS(nums):
    lis = [1]*len(nums)
    
    for i in range(len(nums)-1,-1,-1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                lis[i] = max(lis[i], 1+lis[j])
    return max(lis)
    
def reformatDate(date):
    dateList = date.split(' ')
    monthMap = {
        'Jan':'01',
        'Feb':'02',
        'Mar':'03',
        'Apr':'04',
        'May':'05',
        'Jun':'06',
        'Jul':'07',
        'Aug':'08',
        'Sep':'09',
        'Oct':'10',
        'Nov':'11',
        'Dec':'12'
    }
    day = dateList[0][:-2]
    day = day if len(day) == 2 else '0'+day
    month = monthMap[dateList[1]]
    year = dateList[2]
    return '-'.join([year, month, day])

def arrangeWords(text):
    sortedText = sorted(text.lower().split(' '), key=len)
    firstWord = list(sortedText[0])
    firstWord[0] = chr(ord(firstWord[0])-32)
    sortedText[0] = ''.join(firstWord)
    return ' '.join(sortedText)

def main():
    print(arrangeWords('Keep calm and code on'))

if __name__ == '__main__':
    main()
    