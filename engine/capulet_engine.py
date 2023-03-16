from abc import ABC

from car import Car


class CapuletEngine(Car, ABC):
    def __init__(self, mileage):
        super().__init__("CapuletEngine")
        self.mileage = mileage
        
    def needs_serviced(self,mileage,warning):
        return mileage - self.mileage > 30000
