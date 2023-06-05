# Countdown 
def countdown(number):
    return list(range(number, -1, -1))
print(f"\nCountdown output: {countdown(5)}\n")

# Print and Return
def print_and_return(array):
    print(f"\n{array[0]}")
    return array[1]
print(f"\nPrint and Return Output: {print_and_return([1, 2])}\n")

# First Plus Length
def first_plus_length(array):
    return array[0] + len(array)
print(f"\nFirst Plus Length Output: {first_plus_length([1, 2, 3, 4, 5])}\n")

# Values Greater than Second
def values_greater_than_second(array):
    if len(array) < 2:
        return False
    result = list(filter(lambda number: number > array[1], array))
    print(f"\n{len(result)}")
    return result
print(f"\nValues greater than second output: {values_greater_than_second([5,2,3,2,1,4])}\n")
print(f"Values greater than second output: {values_greater_than_second([3])}\n")

def length_value(size, value):
    return [value] * size
print(f"\nThis Length, That Value Output: {length_value(4, 7)}\n")
print(f"This Length, That Value Output: {length_value(6, 2)}\n")