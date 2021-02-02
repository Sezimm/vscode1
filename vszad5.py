def name_file(a):
    y = open(f'{a}.txt', 'w') 
    y.close()

x = input()
y = name_file(x)
y