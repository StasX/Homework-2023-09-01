cars = []

first_car = {"manufacturer": "Opel",
             "model": "Astra", "year": 2007, "color": "Black"}
second_car = {"manufacturer": "BMW",
              "model": "M4", "year": 2023, "color": "Red"}
third_car = {"manufacturer": "Mercedes-Benz",
             "model": "W 113 SL", "year": 1970, "color": "White"}

cars = [first_car, second_car, third_car]

for car in cars:
    print(car)

print("--------------------")

for car in cars:
    for key, value in car.items():
        print(f"{key}:", value)
    print("...")
