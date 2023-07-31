class A:
    def do_something(self):
        print("Method define in A")


class B(A):
    def do_something(self):
        print("Method define in B")
        super().do_something()


class C(A):
    def do_something(self):
        print("Method define in C")


class D(B, C):
    def do_something(self):
        print('Method defined in D')
        return super().do_something()


# getting more info about class D
# help(D)

# finding MRO or Method Resolution Order
print(D.mro())
print(D.__mro__)


thing = D()
thing.do_something()
