def add(*args):
    return sum(args)


def main():
    print(add(1,2))                     #Output: 3
    print(add(1,2,3,4,5))               #Output: 15
    print(add(1,2,3,4,5,6,7,8,9,10))    #Output: 55
    

if __name__ == '__main__':
    main()