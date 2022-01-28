from agent import Agent
from map import Map
from random import choice
import random
import time


class Environment:
    def __init__(self, configuration, screen_size):

        """
        Enviroment class initializer to create an enviroment whithin a map

        Parameters:
            configuration (object): a configuration object that holds information
            screen_size (tuple): a tuple that holds the screensize
        """

        self.agents = []
        self.screen_size = screen_size
        self.map = Map(configuration)
        self.red_time = configuration.get_red_time()
        self.green_time = configuration.get_green_time()
        self.orange_time = configuration.get_orange_time()
        self.spawn_direction = configuration.get_spawn_direction()
        self.allow_busses = configuration.get_allow_busses()
        self.amount_bus = configuration.get_amount_bus()

    def setup(self):

        """
        this function setups the map and the agents for the simulation
        """

        self.map.setup_map()
        self.create_agents()

    def create_agents(self):

        """
        To create the cars, it will keep looping through the spawn_direction dictionary to look for more cars to add to the self.agent list, each time a car is added to self.agent list, it decreases the amount of the counter from the given direction by 1, this keeps going untill all the counters reach 0.

        For each car it also predetermines the road it will spawn in, and adds the corresponding gates, it will only set the road if it is not a buslane

        If we allow busses to spawn, then add the amount of busses we want to the list, they will be inserted into the list at random indexes, also with a predetermined road it will spawn on, which can only be a buslane
        """

        spawn_roads = []

        for road in self.map.get_roads():
            if road[-40].get_traffic_light():
                spawn_roads.append(road)
            else:
                continue


        while sum(self.spawn_direction.values()) > 0:

            for key, value in self.spawn_direction.items():

                if value <= 0:
                    continue
                else:

                    spawn_road_direction = []

                    gate = []

                    for road in range(len(spawn_roads)):
                        if spawn_roads[road][0].get_heading() == key:
                            spawn_road_direction.append(spawn_roads[road])

                    spawn_road = choice(spawn_road_direction)

                    for i in range(0, len(spawn_road[0].get_gates())):
                        gate.append(spawn_road[0].get_gates()[i])


                    if spawn_road[0].get_busslane() == "False":
                        self.agents.append(
                            Agent(spawn_road[0].get_position()[0], spawn_road[0].get_position()[0], "auto", spawn_road[0],
                                    choice(gate), self.screen_size, key, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), time.time()))

                    self.spawn_direction[key] -= 1

        if self.allow_busses == True:
            for key, value in self.amount_bus.items():
                if value <= 0:
                    continue
                else:

                    bus_lane = []

                    for i in range(len(spawn_roads)):
                        if spawn_roads[i][0].get_busslane() == "True":
                            bus_lane.append(spawn_roads[i])

                    for i in range(value):
                        self.agents.insert(random.randint(0, len(self.agents)), Agent(bus_lane[0][0].get_position()[0], bus_lane[0][0].get_position()[0], "bus", bus_lane[0][0],
                              choice(bus_lane[0][0].get_gates()), self.screen_size, "None", (30, 144,255), time.time()))


        return self.agents

    def get_agents(self):

        """
        this function gets the agents that are being created

        Returns:
            returns all the agents that are created
        """

        return self.agents

    def get_map(self):

        """
        this function gets the map that is available

        Returns:
            returns the map
        """

        return self.map
