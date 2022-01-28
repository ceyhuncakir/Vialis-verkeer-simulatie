import unittest
import sys
from os.path import dirname, abspath, os
sys.path.append(os.path.join(dirname(dirname(__file__)) + '/src'))
from traffic_light import TrafficLight


class TrafficLightUnitTests(unittest.TestCase):
    def test_traffic_light_fase(self):
        traffic_light = TrafficLight(100, "N", 10, 10, 10, "None", "False")
        traffic_light.set_fase((255, 0, 0))
        self.assertTrue((255, 0, 0) == traffic_light.get_fase())

    def test_traffic_light_position(self):
        traffic_light = TrafficLight(100, "N", 10, 10, 10, "None", "False")
        traffic_light.set_position((255, 255))
        self.assertTrue((255, 255) == traffic_light.get_position())

    def test_get_traffic_light_heading(self):
        traffic_light = TrafficLight(100, "N", 10, 10, 10, "None", "False")
        self.assertTrue("N" == traffic_light.get_heading())

    def test_get_traffic_light_busslane(self):
        traffic_light = TrafficLight(100, "N", 10, 10, 10, "None", "True")
        self.assertTrue("True" == traffic_light.get_buss_lane())

    def test_get_traffic_light_neighbour(self):
        traffic_light = TrafficLight(100, "N", 10, 10, 10, "weg_01", "False")
        self.assertTrue("weg_01" == traffic_light.get_neighbour())

    def test_set_traffic_light_activated(self):
        traffic_light = TrafficLight(100, "N", 10, 10, 10, "weg_01", "False")
        traffic_light.set_activated(True)
        self.assertTrue(True == traffic_light.is_active())

    def test_traffic_light_step(self):
        traffic_light = TrafficLight(100, "N", 10, 10, 10, "weg_01", "False")
        traffic_light = TrafficLight(100, "N", 10, 10, 10, "weg_01", "False")
        traffic_light.set_activated(True)
        if traffic_light.is_done():
            traffic_light.step()
            traffic_light.set_activated(False)
        if traffic_light.is_active():
            traffic_light.step()

        self.assertTrue(True == traffic_light.is_active())


if __name__ == "__main__":
    unittest.main(verbosity=2)
