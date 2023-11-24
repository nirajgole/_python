'''
default, parameterized
'''

class DefaultCon:
    def __init__(self) -> None:
        self.default_args='This is default arg'

default_arg=DefaultCon().default_args

class ParaCons:
    def __init__(self,para_args:str)->None:
        self.para_args = para_args

paras = ParaCons('This is a parameter')

class ItReturns:
    # def __init__(self):
    #     self.name = 'ItReturns'

    # TypeError: __init__() should return None, not 'str'
    def __init__(self):
        return 'ItReturns'


res=ItReturns()

print(res)