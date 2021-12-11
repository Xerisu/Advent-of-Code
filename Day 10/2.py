import queue
import statistics

input_file = open("./error.txt","r")

error = input_file.readlines()
error = [elem.strip() for elem in error]

input_file.close()

matching_symbols = {
  "[" : "]",
  "{" : "}",
  "(" : ")",
  "<" : ">"
}

points = {
  "(" : 1,
  "[" : 2,
  "{" : 3,
  "<" : 4
}

scores = []

for row in error:
    symbols = [x for x in row]
    stack = queue.LifoQueue()
    for symbol in symbols:
        if symbol in ['<', '{', '[', '(']:
            stack.put(symbol)
        else:
            a = stack.get()
            if symbol != matching_symbols[a]:
                stack = queue.LifoQueue()
                break
    sum_symbols = 0
    while stack.empty() == False:
        b = stack.get()
        sum_symbols *= 5
        sum_symbols += points[b]
    if sum_symbols != 0:
        scores.append(sum_symbols)

print(statistics.median(scores))
