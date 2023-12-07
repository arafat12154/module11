class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        self.current_speed = max(0, min(self.current_speed, self.maximum_speed))

    def drive(self, hours):
        distance_traveled = self.current_speed * hours
        self.travelled_distance += distance_traveled


class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume


def main():
    electric_car = ElectricCar(registration_number="ABC-15", maximum_speed=180, battery_capacity=52.5)
    gasoline_car = GasolineCar(registration_number="ACD-123", maximum_speed=165, tank_volume=32.3)
    electric_car.accelerate(20)
    gasoline_car.accelerate(15)
    electric_car.drive(3)
    gasoline_car.drive(3)
    print(f"Electric Car Kilometer Counter: {electric_car.travelled_distance:.2f} km")
    print(f"Gasoline Car Kilometer Counter: {gasoline_car.travelled_distance:.2f} km")
if __name__ == "__main__":
    main()