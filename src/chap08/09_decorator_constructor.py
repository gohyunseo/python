#데코레이터 사용 용도(생성자)

class MyDecorator:
    def __init__(self, f):
        print("Initializing MyDecorator...")
        self.func = f

    def __call__(self):
        print("Begin:{}".format(self.func.__name__))

        self.func()  # __call__() 메서드가 호출되면
                     # 생성자에서 저장해둔 함수(데이터속성)를 호출.

        print("End:{}".format(self.func.__name__))

def print_hello():
    print("Hello.")


if __name__ == "__main__":
    hello = MyDecorator(print_hello)
            # MyDecorator의 인스턴스가 만들어지며,
            # __init__() 메서드가 호출.
            # print_hello 식별자는 앞에서 정의한 함수가 아닌 MyDecorator의 객체.

    hello()  # __call__(self) 메서드가 MyDecorator 객체를 호출하듯 사용할 수 있음.