def keyWordArguments(*args,**kwargs):
    print("Type of args: ",type(args))
    print("Type of kwargs: ",type(kwargs))

    for i in args:
        print(i,end=' ')

    print('\n')

    for k,v in kwargs.items():
        print(k,v)
    

def main():
    keyWordArguments(1,2,3,a='a',b='b',c='c')


if __name__ == "__main__":
    main()