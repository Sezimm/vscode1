import random
def gen_number():
    a = [1, 4, 5, 7, 9, 0]
    n = [0,4,4,4]
    i = 0
    while i < 6:
        y = a[random.randint(0,5)]
        n.append(y)
        i+=1
    num = ''
    for i in n:
        num = num + str(i)
    print(num)

gen_number()
    
