class HasPrivate:
    def __init__(self):
        self.public1 = "public1"
        self.__private1 = "private1"
        self.__private2_ = "private2"
        self.__public2__ = "public2"

    def print_from_internal(self):
        print(self.public1)
        print(self.__private1)
        print(self.__private2_)
        print(self.__public2__)

if __name__=="__main__":
    obj = HasPrivate()
    obj.print_from_internal()

    print("=====================")

    print(obj.public1)
    # print(obj.__private1) : error - private
    # print(obj.__private2_) : error - private
    print(obj.__public2__)


