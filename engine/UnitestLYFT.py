import unittest
from datetime import date, timedelta
from rental_car import RentalCar, CapuletEngine, WilloughbyEngine, SternmanEngine, SpindlerBattery, NubbinBattery, Tires


class TestRentalCar(unittest.TestCase):
    def setUp(self):
        self.car1 = RentalCar("Calliope", CapuletEngine(15000), SpindlerBattery(date.today()),
                              Tires("Winter Tires", date.today()))
        self.car2 = RentalCar("Glissade", WilloughbyEngine(20000), SpindlerBattery(date.today()),
                              Tires("Summer Tires", date.today()))
        self.car3 = RentalCar("Palindrome", SternmanEngine(), SpindlerBattery(date.today()),
                              Tires("All-season Tires", date.today()))
        self.car4 = RentalCar("Rorschach", WilloughbyEngine(40000), NubbinBattery(date.today()),
                              Tires("All-season Tires", date.today()))
        self.car5 = RentalCar("Thovex", CapuletEngine(5000), NubbinBattery(date.today()),
                              Tires("Winter Tires", date.today()))

    def test_engine_needs_service(self):
        self.assertTrue(self.car1.engine.needs_service(50000, False))
        self.assertFalse(self.car1.engine.needs_service(20000, False))
        self.assertTrue(self.car2.engine.needs_service(80000, False))
        self.assertFalse(self.car2.engine.needs_service(10000, False))
        self.assertFalse(self.car3.engine.needs_service(10000, True))
        self.assertTrue(self.car4.engine.needs_service(100000, False))
        self.assertFalse(self.car4.engine.needs_service(20000, False))
        self.assertTrue(self.car5.engine.needs_service(30000, False))
        self.assertFalse(self.car5.engine.needs_service(1000, False))

    def test_battery_needs_service(self):
        self.assertTrue(self.car1.battery.needs_service(date.today() - timedelta(days=731)))
        self.assertFalse(self.car1.battery.needs_service(date.today() - timedelta(days=365)))
        self.assertTrue(self.car2.battery.needs_service(date.today() - timedelta(days=1461)))
        self.assertFalse(self.car2.battery.needs_service(date.today() - timedelta(days=730)))
        self.assertTrue(self.car4.battery.needs_service(date.today() - timedelta(days=1461)))
        self.assertFalse(self.car4.battery.needs_service(date.today() - timedelta(days=730)))
        self.assertTrue(self.car5.battery.needs_service(date.today() - timedelta(days=731)))
        self.assertFalse(self.car5.battery.needs_service(date.today() - timedelta(days=365)))

    def test_tires(self):
        self.assertEqual(self.car1.tires.type, "Winter Tires")
        self.assertEqual(self.car2.tires.type, "Summer Tires")
        self.assertEqual(self.car3.tires.type, "All-season Tires")
        self.assertEqual(self.car4.tires.type, "All-season Tires")
        self.assertEqual(self.car5.tires.type, "Winter Tires")


if __name__ == '__main__':
    unittest.main()
