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


@MyDecorator  # @기호를 사용하여 class의 __call__() 함수를 바로 적용하여 호출 할 수 있다.
def print_hello():
    print("Hello.")


if __name__ == "__main__":
   print_hello()