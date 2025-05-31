from collections import defaultdict, deque
from functools import reduce
import heapq
from itertools import zip_longest
from operator import xor

def test(v1, v2) -> int:
    l1 = [1,2,3,7,8,9]
    l2 = [4,5]
    print(list(zip_longest(l1,l2,fillvalue=0)))
    for rev1, rev2 in zip_longest(l1, l2, fillvalue=0):
        print(rev1, rev2)
    return 0

def sortColors(arr):
    low = 0
    mid = 0
    high = len(arr)-1
    while(mid<=high):
        if arr[mid] == 0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high -=1
    print(arr)
    return arr
      
def groupAnagrams(strs):
    map = defaultdict(list)     
    
    for s in strs:
        count = [0]*26
        for ch in s:
            count[ord(ch)-97] += 1
        map[tuple(count)].append(s)
    print(map.values())
             
def kMostFrequent(nums, k):
    map = defaultdict(int)
    res = []
    
    for i in nums:
        map[i] += 1
    
    sortedMap = dict(sorted(map.items(), key= lambda x: x[1], reverse=True))
    keys = list(sortedMap.keys())

    for i in range(k):
        res.append(keys[i])
    
    print(res)          
    
def findRelativeRanks(score):
    sortedScore = sorted(score, reverse=True)
    map = defaultdict(int)
    
    for i,v in enumerate(sortedScore):
        map[v] = i
    
    medals = ["Gold Medal","Silver Medal","Bronze Medal"]
    res = [medals[map[i]] if map[i] < 3 else str(map[i]+1) for i in score]
    
    
    print(res)
    
def kthSmallestPrimeFraction(arr, k):
    map = defaultdict(float)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            map[tuple([arr[i], arr[j]])] = arr[i]/arr[j]
    
    sortedMap = dict(sorted(map.items(), key=lambda x:x[1]))
    print(list(list(sortedMap.keys())[k]))
            
def productExceptSelf(nums):
    n = len(nums)
    res = [1]*n
    
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(n-1,-1,-1):
        res[i] *= postfix
        postfix *= nums[i]
    
    print(res)
    
def threeSum(nums):
    res = []
    nums.sort()
    
    for i,a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        
        l,r = i+1, len(nums)-1
        while(l<r):
            s = a + nums[l] + nums[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l<r:
                    l += 1
    return res

def countOnes(n):
    count = 0
    while(n>0):
        n &= n-1
        count += 1
    return count

def countBits(n):
    res = []
    for i in range(n+1):
        res.append(countOnes(i))
    return res        

def isPower(n):
    return n&n-1 == 0

def isSubsequence(s,t):
    m,n = len(s), len(t)
    
    if n == 0 and m == 0:
        return True
    if n != 0 and m == 0:
        return True
    if n == 0 and m != 0:
        return False
    
    i,j = 0,0
    while(i < m and j < n):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1
    return i == m

def longestPalindrome(s):
    map = defaultdict(int)
    for c in s:
        map[c] += 1
    
    maxOdd = 1
    res = 0
    for k,v in map.items():
        if v%2 == 0:
            res += v
        if v%2 != 0:
            maxOdd = max(maxOdd, v)
    return res + maxOdd

def main():
    arr = [1,2,2,3,4,4,5,6,7,7,8,9,9,10]
    x = filter(lambda x:x%2 == 0, arr)
    print(list(x))
    

    

if __name__ == '__main__':
    main()
    
        
        
                