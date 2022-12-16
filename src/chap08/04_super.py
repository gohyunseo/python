class A:
    def __init__(self):
        print("A.__init__()")
        self.message="Hello"

class B(A):
    def __init__(self):
       # A.__init__(self)  -- 사용은 가능하지만 지양한다.
        super().__init__()
        print("B.__init__()")

        print("self.message is " + self.message)

if __name__ == "__main__":
    obj = B()
    print(obj.message)


############################################################################

class Base:
    def __init__(self):
        print("Base")

class Derived(Base):
    pass

    #def __init__(self):  생성자 함수를 초기화 해주지 않아도 defualt로 이런구조의 생성자를 초기화해준다.
    #    super().__init__()


print("=================================")

d = Derived()
