from prac_09.unreliable_car import UnreliableCar

def main():
    my_car = UnreliableCar("Ford Pinto", 100, 50)

    distance_driven = my_car.drive(40)
    print(f"Car drove {distance_driven}km")

    print(my_car)

if __name__ == "__main__":
    main()
