class Underscore:

    def __init__(self):
        pass

    def map(self, iterable, callback):
        return [callback(value) for value in iterable]

    def find(self, iterable, callback):
        for value in iterable:
            if callback(value):
                return value

    def filter(self, iterable, callback):
        return [value for value in iterable if callback(value)]

    def reject(self, iterable, callback):
        return [value for value in iterable if not callback(value)]

if __name__ == "__main__":
    _ = Underscore()

    print(_.map([1,2,3], lambda x: x*2))
    print(_.find([1,4,3], lambda x: x > 2))
    print(_.filter([1,2,3], lambda x: x >= 2))
    print(_.reject([3,4,5], lambda x: x <= 3))