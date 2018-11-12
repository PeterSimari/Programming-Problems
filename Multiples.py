


def main():
    n=1000
    print('All multiples of 3 and 5 for', n)
    n=n-1
    s=0
    
    while n>1:
        if (n%3==0):
            print(n)
            s = n + s
            n = n-1
        elif (n%5==0):
            print(n)
            s = n + s
            n=n-1
        else:
            n=n-1
    print("The sum of all the multiples is:", s)
    
main()
