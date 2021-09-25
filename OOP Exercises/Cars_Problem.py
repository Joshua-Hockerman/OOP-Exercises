import Cars_Class as cc

fast_car = cc.Cars("Miata", "Mazda")

n = 5

i = 0

while i < n:
    fast_car.accelerate()
    print(
        "Woah! That fast car is going " + str(fast_car.get_speed()) + " miles per hour!"
    )
    i += 1

i = 0

while i < n:
    fast_car.brake()
    print(
        "Woah! That fast car is going " + str(fast_car.get_speed()) + " miles per hour!"
    )
    i += 1
