print('x y z N')
for x in range(2):
    for y in range(2):
        for z in range(2):
            N = not(x or y or z) == ((not x) and (not y) and (not z))
            print(x, y, z, N)
