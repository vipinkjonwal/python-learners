from pip import main


def print_pattern():
    n = 8
    while(n>0):
        print(" "*(8-n),"* "*n)
        n -= 1
    n=1
    while(n<9):
        print(" "*(8-n),"* "*n)
        n+=1
    
    
def main():
    print_pattern()    
    
if __name__ == '__main__':
    main()
    