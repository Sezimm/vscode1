def fibonachi():
    i = 0
    a = 1
    b = 1
    fib = [a, b]
    while i < 8:
        c = a + b
        a = b
        b = c
        fib.append(c)
       
        i += 1
    print(fib)
        
fibonachi()

