def fib(n):
    first = 0
    second = 1

    if n < 1:
        print("Invalid input. Please enter a positive integer.")
        return
    
    if n == 1:
        print(f"The Fibonacci series up to {n} terms: {first}")
        return 
    
    if n == 2:
        print(f"The Fibonacci series up to {n} terms: {first}, {second}")
        return
    
    series = [first, second]
    count = 3
    while count <= n:
        fib_n = first + second
        series.append(fib_n)
        first = second
        second = fib_n
        count += 1
    
    print(f"The Fibonacci series up to {n} terms: {', '.join(map(str, series))}")


fib(5)