class Calculator:

    @staticmethod
    def plus(x1, x2):  #범용적으로 사용하기 때문에 self는 없어야 한다. / self는 한정적으로 사용할 경우 사용
        return x1 + x2

    @staticmethod
    def minus(x1, x2):
        return x1 - x2

    @staticmethod
    def multiply(x1, x2):
        return x1 * x2

    @staticmethod
    def divide(x1, x2):
        return x1 / x2

if __name__ == "__main__":
    print("{0} + {1} = {2}".format(7, 4, Calculator.plus(7, 4)))
    print("{0} - {1} = {2}".format(7, 4, Calculator.minus(7, 4)))
    print("{0} * {1} = {2}".format(7, 4, Calculator.multiply(7, 4)))
    print("{0} / {1} = {2}".format(7, 4, Calculator.divide(7, 4)))
