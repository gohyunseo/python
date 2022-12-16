# 다중 상속

class A:
    def method(self):
        print("A")


class B(A):
    def method(self):
        print("B")


class C(A):
    def method(self):
        print("C")


class D(B, C):
    pass


if __name__ == "__main__":
    obj = D()
    obj.method()

