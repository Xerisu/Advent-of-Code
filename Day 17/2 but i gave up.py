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

# sad attempt for part 2:

# dictionaries containing numbers of x and y reaching the target area assigned to the number of steps it takes them to reach the target
# Last element of this dict is, for x: throw stopped in area (with number of steps instead of number of xes), and for y: throws longer than stopped x
# you know what? I give up. I'm not sure if that version is printing other things than error at this point.
matching_x = {}
matching_y = {}

for i in range(1, x_min_yeet):
    matching_y.update({i: 0})
    matching_x.update({i: 0})
matching_x.update({'perfect yeet': []})
matching_y.update({'longer than perfect yeet': 0})

for x in range(x_min_yeet, x_max_yeet+1):
    times_yeeted = 1
    x_speed = x
    while True:
        x_speed -= 1  # tu jest coś nie tak
        if x_speed == 0 and x_min <= x <= x_max:
            matching_x['perfect yeet'].append(times_yeeted)
            break
        elif x_min <= x <= x_max:
            matching_x[times_yeeted] += 1
        elif x_speed == 0 or x > x_max:
            break

        x = x + x_speed
        times_yeeted += 1

for y in range(y_min_yeet, y_max_yeet+1):
    y_speed = y
    times_yeeted = 1
    while True:
        y_speed -= 1
        if y_min <= y <= y_max and times_yeeted >= x_min_yeet:
            matching_y['longer than perfect yeet'] += 1
        elif y_min <= y <= y_max:
            matching_y[times_yeeted] += 1
        elif y < y_min:
            break
        y = y + y_speed
        times_yeeted += 1

print(matching_x)
print(matching_y)

# counting number of times the probe reaches the target area

good_yeets = 0

for i in range(1, x_min_yeet):
    good_yeets += matching_x[i] * matching_y[i]

good_yeets += len(matching_x['perfect yeet']) * matching_y['longer than perfect yeet']