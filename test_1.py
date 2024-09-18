# import time

# start = time.time()

# t=(1,2,3,5,5,5,5,5,5,5,55,5,5,55,)

# l=[*range(15)]

# i -str

# Input :This is python
# output: Python is This

def sentence_rev(s: str) -> None:
    res = ' '.join(s.split(' ')[::-1])
    print(res)


sentence_rev('This is python')


group_data = {
    "propData": {
        "A1": {
            "subscribers": {
                "5140": "361934",
                "8993": "361872",
                "7860": "361902",
                "7861": "361894"

            },
            "members": {
                "A2": {
                    "260052": "122992",
                    "401699": "581",
                    "306837": "584",
                    "345416": "3976"
                },

                "A3": {
                    "242425": "329000",
                    "161858": "284371",
                    "112843": None,
                    "269506": None
                }
            }
        }
    }
}

# res = group_data['propData']['A1']['members']['A2'].keys()

# print(res)


# if else condition, compare 2 no. -> 1. a>b 2. b>a 3. else

# a=34
# b=43

# if a>b:
#     print(f'{a} is greater')
# elif b>a:
#     print(f'{b} is greater')
# else:
#     print(f'Both are same')


# 1st 10 no. fibo
# 0,1,1,2,3,5,8,13
# a=0
# b=1
# for i in range(2,10):
#     a,b=b,a+b
#     print(a)

# class calculator add, sub
# class Calculator:
#     def __init__(self, num_1: int, num_2: int) -> None:
#         self.num_1 = num_1
#         self.num_2 = num_2

#     def add(self):
#         return self.num_1+self.num_2

#     def sub(self): lambda :self.num_1-self.num_2


# cal = Calculator(2, 3)
# res = cal.add()
# sub = cal.sub()

# print(res)
# print(sub)
# print(cal.__doc__)


# def decor(func:object)->object:
#     def wrapper():
#         print('Before function')
#         func()
#         print('After function')
#     return wrapper

# @decor
# def my_space():
#     print('Inside my space')

# my_space()