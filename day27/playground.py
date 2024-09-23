

def add(*args):
    print(args[1])
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3,5,6,7,8,9,1,2,3))


def calculate(**kwargs):
    print(type(kwargs))
    print(kwargs)

    for key, value in kwargs.items():
        print(key)
        print(value)

calculate(add=3, multiply=6)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"] # if we try to print make without providing a make it will crash
        self.model = kw.get("model") # if we try to print model without providing a model it will None
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GTR")
print(my_car.model)