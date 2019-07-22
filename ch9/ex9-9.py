# Battery Upgrade: Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). This method
# should check the battery size and set the capacity to 85 if it isn't
# already. Make an electric car with a default battery size, call get_range()
# once, and then call get_range a second time after upgrading the battery.
# You should see an increase in the car's range.

from car import Car
from electric_car import Battery, ElectricCar

my_tesla = ElectricCar(2019, 'Tesla', 'Model S')
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

