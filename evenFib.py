
p=0

def fib(n):
    if n <= 1:
        return n
    else:
        if ((fib(n-1) + fib(n-2))%2==0) & ((fib(n-1) + fib(n-2))%2==0) < 4000000:
            p=p+(fib(n-1) + fib(n-2))
        return(fib(n-1) + fib(n-2))
    

def main():
    n=15
    if n <= 0:
       print("Error: Negative number")
    else:
       print("Fibonacci sequence:")
       for i in range(n):
           print(fib(i))
    count()

def count():
    print(p)

main()

