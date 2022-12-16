# Overriding

class A:
    def method(self):
        print("A")


class B(A):
    def method(self):
        print("B")


class C(A):
    def method(self):
        print("C")

def overriding(overriding):
    overriding.method()

if __name__ == "__main__":
    a = A()
    # a.method()

    b = B()
    # b.method()

    c = C()
    # c.method()

    overriding(a)
    overriding(b)
    overriding(c)