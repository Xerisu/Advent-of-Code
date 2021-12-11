import queue

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
  ")" : 3,
  "]" : 57,
  "}" : 1197,
  ">" : 25137
}

sum_errors = 0

for row in error:
    symbols = [x for x in row]
    stack = queue.LifoQueue()
    for symbol in symbols:
        if symbol in ['<', '{', '[', '(']:
            stack.put(symbol)
        else:
            a = stack.get()
            if symbol != matching_symbols[a]:
                sum_errors += points[symbol]
                break

print(sum_errors)
            



