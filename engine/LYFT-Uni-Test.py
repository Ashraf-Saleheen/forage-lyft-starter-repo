from abc import ABC, abstractmethod
from datetime import date


class RentalCar:
    def __init__(self, model, engine, battery, tires):
        self.model = model
        self.engine = engine
        self.battery = battery
        self.tires = tires


class Engine(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def needs_service(self, mileage, warning):
        pass


class CapuletEngine(Engine):
    def __init__(self, mileage):
        super().__init__("Capulet Engine")
        self.mileage = mileage

    def needs_service(self, mileage, warning):
        return mileage - self.mileage >= 30000


class WilloughbyEngine(Engine):
    def __init__(self, mileage):
        super().__init__("Willoughby Engine")
        self.mileage = mileage

    def needs_service(self, mileage, warning):
        return mileage - self.mileage >= 60000


class SternmanEngine(Engine):
    def __init__(self):
        super().__init__("Sternman Engine")

    def needs_service(self, mileage, warning):
        return warning


class Battery(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def needs_service(self, last_service):
        pass


class SpindlerBattery(Battery):
    def __init__(self, last_service):
        super().__init__("Spindler Battery")
        self.last_service = last_service

    def needs_service(self, last_service):
        return (date.today() - self.last_service).days >= 730


class NubbinBattery(Battery):
    def __init__(self, last_service):
        super().__init__("Nubbin Battery")
        self.last_service = last_service

    def needs_service(self, last_service):
        return (date.today() - self.last_service).days >= 1460


class Tires:
    def __init__(self, type, last_service):
        self.type = type
        self.last_service = last_service


car1 = RentalCar("Calliope", CapuletEngine(15000), SpindlerBattery(date.today()), Tires("Winter Tires", date.today()))
car2 = RentalCar("Glissade", WilloughbyEngine(20000), SpindlerBattery(date.today()),
                 Tires("Summer Tires", date.today()))
car3 = RentalCar("Palindrome", SternmanEngine(), SpindlerBattery(date.today()), Tires("All-season Tires", date.today()))
car4 = RentalCar("Rorschach", WilloughbyEngine(40000), NubbinBattery(date.today()),
                 Tires("All-season Tires", date.today()))
car5 = RentalCar("Thovex", CapuletEngine(5000), NubbinBattery(date.today()), Tires("Winter Tires", date.today()))

