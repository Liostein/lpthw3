cars = 100
space_in_a_car = 4.0   # 4.0 is a float number
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capicity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "can drive.")
print("There will be ", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capicity, "people today.")
print("We have", passengers, "passengers to carpool today.")
print("We need to put about", average_passengers_per_car, "people in each car.")

# using variables to assign values then print(value, ..., sep, end, file, flush)
