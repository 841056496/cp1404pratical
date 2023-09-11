from prac_09.car import Car
import random

class UnreliableCar(Car):
    """Specialised version of a Car that has a chance of failing to drive."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if a random number is less than its reliability."""
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
