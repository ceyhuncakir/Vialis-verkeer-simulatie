import unittest
import sys
from os.path import dirname, abspath, os
sys.path.append(os.path.join(dirname(dirname(__file__)) + '/src'))
from road import Road
from traffic_light import TrafficLight

class RoadUnitTest(unittest.TestCase):
    def test_road_traffic_light(self):
        traffic_light = TrafficLight(100, "N", 10, 10, 10, "None", "False")
        road = Road((350, 350), True, "start", "32", "N", ["gate_01"], "False")
        road.set_traffic_light(traffic_light)
        self.assertTrue(traffic_light == road.get_traffic_light())

    def test_occupied_road(self):
        road = Road((350, 350), True, "start", "32", "N", ["gate_01"], "False")
        road.set_occupied(True)
        self.assertTrue(True == road.is_occupied())

    def test_road_crossing_point(self):
        road = Road((350, 350), True, "start", "32", "N", ["gate_01"], "False")
        road.set_crossing("32")
        self.assertTrue("32" == road.get_crossing())

    def test_get_road_sensor(self):
        road = Road((350, 350), True, "start", "32", "N", ["gate_01"], "False")
        self.assertTrue(True == road.get_sensor())

    def test_road_id(self):
        road = Road((350, 350), True, "start", "32", "N", ["gate_01"], "False")
        self.assertTrue("32" == road.get_road_id())

    def test_get_busslane(self):
        road = Road((350, 350), True, "start", "32", "N", ["gate_01"], "False")
        self.assertTrue("False" == road.get_busslane())

    def test_road_position(self):
        road = Road((350, 350), True, "start", "32", "N", ["gate_01"], "False")
        self.assertTrue((350, 350) == road.get_position())

if __name__ == "__main__":
    unittest.main(verbosity=2)
