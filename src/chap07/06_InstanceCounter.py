class InstanceCounter:
    count = 0

    def __init__(self):
        InstanceCounter.count += 1

    @classmethod
    def print_instance_counter(cls):
        print(cls.count)

if __name__ == "__main__":
    x = InstanceCounter()
    x.print_instance_counter()

    InstanceCounter.print_instance_counter()

    y = InstanceCounter()
    y.print_instance_counter()

    InstanceCounter.count = 10
    InstanceCounter.print_instance_counter()
