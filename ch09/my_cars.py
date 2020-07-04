from car import Car
from electric_car import ElectricCar as EC

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

my_telsa = EC('telsa', 'model s', 2019)
print(my_telsa.get_descriptive_name())
my_telsa.fill_gas_tank()
my_telsa.battery.describe_battery()
my_telsa.battery.get_range()
