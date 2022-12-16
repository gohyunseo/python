class Car:
    def ride(self):
        print("Run")


class FlyingCar(Car):
    def ride(self):
        super().ride()
        print("Fly")


if __name__ == "__main__":
    # car = Car()
    # car.ride()

    my_car = FlyingCar()
    my_car.ride()
