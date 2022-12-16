class Car:
    def __init__(self):
        self.color = 0xFF0000  # 차량 색상(빨강)
        self.wheel_size = 16 # 바퀴의 크기
        self.displacement = 2000 # 엔진 배기량

    def forward(self):    # 전진
        pass

    def backward(self):    # 후진
        pass

    def turn_left(self):    # 좌회전
        pass
    
    def turn_right(self):    # 우회전
        pass
    

if __name__ == "__main__":
    my_car = Car()   #Car 클래스의 객체 생성

    print('0x{:02X}'.format(my_car.color)) # :02 2자리 정수(2자리가 안되면 0으로 채워짐) X 16진수
    print(my_car.wheel_size)
    print(my_car.displacement)

    my_car.forward()  # my_car 멤버메서드 접근
    my_car.backward()
    my_car.turn_right()
    my_car.turn_left()
