print("\nNumber One - First Solution\n")

print(list(range(1, 51)))

print("\nNumber One - Second Solution\n")

for integer in range(1, 51):
    print(integer)

print("\nNumber Two - First Solution\n")

print(list(range(5, 1001, 5)))

print("\nNumber Two - Second Solution\n")

for integer in range(5, 1001, 5):
    print(integer)

print("\nNumber Three Solution\n")

for integer in range(1, 101):
    result = ""

    if integer % 5 == 0:
        result += "Coding "
    
        if integer % 10 == 0:
            result += "Dojo"

        print(result)  

    else:
        print(integer)

print("\nNumber Four - First Solution\n")

numbers = range(1, 500001)

# https://www.cuemath.com/sum-of-integers-formula/
def add_numbers(array = numbers):
    return int((len(numbers) * (numbers[0] + numbers[-1])) / 2)

print(add_numbers())

print("\nNumber Four - Second Solution\n")

sum = 0
for integer in numbers:
    sum += integer
print(sum)

print(f"Sanity Check: {add_numbers() == sum}")

print("\nNumber Five - First Solution\n")

print(list(range(2018, 0, -4)))

print("\nNumber Five - Second Solution\n")

for integer in range(2018, 0, -4):
    print(integer)

print("\nNumber Six - First Solution\n")

def print_multiples(lowNum = 2, highNum = 9, mult = 3):
    return [num for num in range(lowNum, highNum + 1) if num % mult == 0]

print(print_multiples())

print("\nNumber Six - Second Solution\n")

lowNum, highNum, mult = 2, 9, 3
for integer in range(lowNum, highNum + 1):
    if integer % mult == 0:
        print(integer)
print()