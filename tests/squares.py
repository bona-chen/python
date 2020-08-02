squares = [square ** 2 for square in range(1,11)]
print(squares)
for number in range(1,21):
    print(number, end=(","))
numbers = []
for digit in range(1,1000001):
    print(digit)
    numbers.append(digit)
print(numbers)
the_mini = min(numbers)
the_max = max(numbers)
the_sum = sum(numbers)
print(the_mini)
print(the_max)
print(the_sum)