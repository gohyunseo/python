class Base:
    def __init__(self):
        print(self)  # 메모리의 주소값 확인
        self.message = "Hello, World."

    def print_message(self):
        print(self.message)

# Java에서 클래스 상속방법 class Derived extends Base

#Python에서 클래스 상속방법
class Derived(Base):
    pass

if __name__ == "__main__":
    base = Base()
    base.print_message()

    derived = Derived()
    derived.print_message()

