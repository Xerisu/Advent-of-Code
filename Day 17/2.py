# x=20..30, y=-10..-5
# 282 314 -80 -45

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

print(x_min_yeet, x_max_yeet, y_min_yeet, y_max_yeet)
good_yeets = 0

for x in range(x_min_yeet, x_max_yeet+1):
    for y in range(y_min_yeet, y_max_yeet+1):
        x_speed = x
        y_speed = y
        changing_x = x
        changing_y = y
        while True:
            if x_speed > 0:
                x_speed -= 1
            y_speed -= 1
            if x_min <= changing_x <= x_max and y_min <= changing_y <= y_max:
                good_yeets += 1
                print(x, y)
                break
            elif changing_x > x_max or changing_y < y_min:
                break
            changing_x = changing_x + x_speed
            changing_y = changing_y + y_speed


print('reaching throws =', good_yeets)