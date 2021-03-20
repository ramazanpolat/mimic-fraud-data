from datetime import datetime
import time
from mimix.person import Person
from mimix.number import Number
from mimix.reference import Ref

d = {
    "a": 1190,
    "b": Number().between(ax=800, bx=Ref('a')),
    "first_name": Person().first_name(),
    "last_name": Person().last_name(),
    "full_name": Person().full_name(),
    "email": Person().email(),
    # "email2": Person().email2(first_name=Ref('first_name'), last_name=Ref('last_name')),
    "age": Number().between3(500, Ref('a')),
    "year": Number().between3(x=1, y=Ref('age'))
}


def generate(template: dict, count: int):
    for _ in range(count):
        row = {}
        for key, generator in template.items():
            if callable(generator):
                g = generator()
                refs = next(g)
                send_refs = {}
                for ref_key, ref_value in refs.items():
                    send_refs[ref_key] = row[ref_value]
                    # if 'a' in refs:
                    #     send_refs['a'] = d['a']
                result = g.send(send_refs)
            else:
                result = generator
            row[key] = result
        yield row


# for x in generate(d, count=10):
#     print(x)


def add(a, b, c):
    return a + b + c


def square(a):
    return a * a


def my_partial(method, param1):
    def inner():
        return method(param1)

    return lambda: inner()


def my_partial2(method, *params):
    def inner(*xx):
        return method(*params, *xx)

    return inner


def save_call(func, *params):
    def inner():
        print(datetime.now())
        return func(*params)

    return inner


square_2 = my_partial(square, 3)

print(square_2())

add_2_3 = my_partial2(add, 2, 3)

print(add_2_3(11))

row1 = save_call(add, 2, 3, 4)
print("SAVED CALLS")
print(row1())
time.sleep(1)
print(row1())
