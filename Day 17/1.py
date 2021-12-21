x_min = 282
x_max = 314

y_min = -80
y_max = -45


x_min_yeet = 0

for x in range(x_max):
    if x_min <= (1+x)*x//2 <= x_max:
        x_min_yeet = x
        break
x_max_yeet = x_max

y_min_yeet = y_min
y_max_yeet = -(y_min+1)

# part 1:

print('max height =', (1 + y_max_yeet) * y_max_yeet // 2)




