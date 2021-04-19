import __init__ as b

import ast
import types

class testClass():
    def __init__(self):
        self.x = self.random_function()
        self.b = 12

    def random_function(self):
        print('You\'re crazy!')

    def show_attributes(self):
        return dir(self)

    def save_state(self):
        result = []
        for attr in dir(self):
            if not attr.startswith('__'):
                if not isinstance(self.__getattribute__(attr), types.MethodType):
                    result.append(attr)
        with open(f'testing_savestate.txt', 'w+') as f:
            for r in result:
                attr_to_save = {r:self.__getattribute__(r)}
                f.write(str(attr_to_save)+'\n')


AAPL = b.IEXStock('AAPL')
AAPL.save_state()

"""AAPL = b.IEXStock('AAPL')
AAPL.get_company()
print(type(AAPL.company))
with open('testwrite.json', 'w+') as file:
    thing_to_write = {'company':AAPL.company}
    file.write(str(thing_to_write))

with open('testwrite.json', 'r') as file:
    data = file.read()
    print(type(data))
    print(type(ast.literal_eval(data)))"""
