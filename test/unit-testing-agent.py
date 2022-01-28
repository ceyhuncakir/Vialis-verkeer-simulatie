import unittest
import sys
from os.path import dirname, abspath, os
sys.path.append(os.path.join(dirname(dirname(__file__)) + '/src'))
from agent import Agent, get_mass_spread
from road import Road
import random
import time


class AgentUnitTests(unittest.TestCase):
    def test_agent_spawn(self):
        road_1 = Road([0, 0], False, "end", "32", "N", "gate_01", "False")
        auto_agent = Agent(road_1.get_position()[0], road_1.get_position()[1], "auto", road_1, "gate_01", (1920, 1080),"N", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), time.time())
        self.assertTrue(type(auto_agent) == Agent)

    def test_agent_get_position(self):
        road_1 = Road([0, 0], False, "end", "32", "N", "gate_01", "False")
        auto_1 = Agent(road_1.get_position()[0], road_1.get_position()[1], "auto", road_1, "gate_01", (1920, 1080),"N", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), time.time())
        self.assertTrue(auto_1.get_position() == [0, 0])

    def test_current_node(self):
        road_1 = Road([0, 0], False, "end", "32", "N", "gate_01", "False")
        auto_1 = Agent(road_1.get_position()[0], road_1.get_position()[1], "auto", road_1, "gate_01", (1920, 1080),"N", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), time.time())
        self.assertTrue(road_1 == auto_1.get_current_node())


if __name__ == "__main__":
    unittest.main(verbosity=2)
