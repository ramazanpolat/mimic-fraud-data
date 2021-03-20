import random

from .reference import Ref


class Number:
    def __init__(self):
        self.auto_increment_params = {
            'start': None
        }

    @staticmethod
    def between(ax, bx):
        def inner(a, b):
            ref_params = {}
            if isinstance(a, Ref):
                ref_params['a'] = a.ref_key

            if isinstance(b, Ref):
                ref_params['b'] = b.ref_key

            ref_values = yield ref_params

            if 'a' in ref_values:
                a = ref_values['a']

            if 'b' in ref_values:
                b = ref_values['b']

            yield random.randint(a, b)

        return lambda: inner(ax, bx)

    @staticmethod
    def between3(x, y):
        def inner(xx, yy):
            ref_params = {}

            if isinstance(xx, Ref):
                ref_params['xx'] = xx.ref_key

            if isinstance(yy, Ref):
                ref_params['yy'] = yy.ref_key

            ref_values = yield ref_params

            if 'xx' in ref_values:
                xx = ref_values['xx']

            if 'yy' in ref_values:
                yy = ref_values['yy']
            print('xx:', xx, 'yy:', yy)

            yield random.randint(xx, yy)

        return lambda: inner(x, y)

    # def auto_increment(self, start):
    #     self.auto_increment_params['start'] = start - 1
    #
    #     def auto_increment_gen():
    #         self.auto_increment_params['start'] += 1
    #         return self.auto_increment_params['start']
    #
    #     return auto_increment_gen
