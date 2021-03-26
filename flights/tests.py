from django.test import TestCase

# Create your tests here.
from .models import Airport,Flight,Passenger

class FlightTestcase(TestCase):
    def setup(self):
        a1=Airport.objects.create(code="aaa",city="ahmdbad")
        a2=Airport.objects.create(code="bbb",city="bangalore")
        Flight.objects.create(origin=a1,destination=a2,duration=100)
        Flight.objects.create(origin=a1,destination=a1,duration=200)
        Flight.objects.create(origin=a1,destination=a2,duration=-100)
    def test_departures_count(self):
        a=Airport.objects.get(code="aaa")
        self.assertEqual(a.departures.count(),3)
    def test_arrivals_count(self):
        a=Airport.objects.get(code="aaa")
        self.assertEqual(a.arrivals.count(),1)
    def test_valid_flight(self):
        a=Airport.objects.get(code="aaa")
        b=Airport.objects.get(code="bbb")
        f=Flight.objects.get(origin=a1,destination=a2,duration=100)
        self.assertTrue(is_valid_flight())
    def test_invalid_flight_destination(self):
        a1 = Airport.objects.get(code="aaa")
        f = Flight.objects.get(origin=a1, destination=a1)
        self.assertFalse(f.is_valid_flight())
    def test_invalid_flight_duration(self):
        a1 = Airport.objects.get(code="aaa")
        a2 = Airport.objects.get(code="bbb")
        f = Flight.objects.get(origin=a1, destination=a2, duration=-100)
        self.assertFalse(f.is_valid_flight())
