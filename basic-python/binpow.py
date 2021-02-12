import time
def binpow(a,b):
    result = 1
    while(b):
        if b&1:
            result *= a
        a *= a
        b >>=1
    return result

def power(a,b):
    result = 1
    for _ in range(b):
        result *= a
    return result
    
    

def main():
    s_t = time.time()
    print(binpow(2,32))
    e_t = time.time()
    print((e_t-s_t)*10**3)
    s_t = time.time()
    print(power(2,32))
    e_t = time.time()
    print((e_t-s_t)*10**3)


if __name__ == '__main__':
    main()