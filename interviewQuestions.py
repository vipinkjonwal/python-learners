def missingNumber(arr, n) -> int:
    return int((n+1)*(n+2)/2 - sum(arr))

def twoSum(arr, x) -> bool:
    return True if len([arr[i]+arr[j] == x for i in range(len(arr)) for j in range(i+1, len(arr)) if arr[i]+arr[j]==x])>=1 else False 

def reversePartialList(arr, start, end) -> list[int]:
    i = start if start > 0 else 0
    j = end if end <= len(arr)-1 else len(arr)-1
    while(i<j):
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j-=1
    return arr
    
def swap(a,b):
    return b,a
    


def main():
    print(reversePartialList([1,2,3,4,5,6,7,8,9], 2, 9))
    # print(swap(1,2))

if __name__ == '__main__':
    main()