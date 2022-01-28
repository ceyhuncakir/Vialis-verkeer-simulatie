import pygame
from pygame.locals import *
import time
from env import Environment
import random

class Simulation:
    def __init__(self, configuration):


        """
        TrafficLight class initializer to create an trafficlight whithin a map

        Parameters:
            configuration (object): configuration object which holds information for the simulation
        """

        pygame.init()
        screen_size = pygame.display.Info()
        self.screen = pygame.display.set_mode((screen_size.current_w, screen_size.current_h))
        self.tick_rate = configuration.get_tick_rate()
        self.screen.fill((192, 207, 169))
        self.start = time.time()
        self.env = Environment(configuration, (screen_size.current_w, screen_size.current_h))
        self.agent_spawn_rate = configuration.get_agent_spawn_rate()
        self.get_allow_busses = configuration.get_allow_busses()
        self.kill_total = []

    def run_simulation(self):

        """

        Returns:
            The amount of time the simulation has been running for, the car flow time, the bus flow time, further more is this the function that runs and draws the cars for the simulation
        """

        self.env.setup()
        grey = (169, 169, 169)
        count = 0
        agent_width = 10
        agent_height = 12
        agent_x_offset = 8
        agent_y_offset = 10
        roads = self.env.get_map().get_roads()
        agents = self.env.get_agents()
        traffic_lights = self.env.get_map().get_traffic_lights()
        traffic_light_controller = self.env.get_map().get_traffic_controller()

        active_agents = []
        while True:

            self.screen.fill((192, 207, 169))

            for event in pygame.event.get():

                if event.type == QUIT:
                    pygame.quit()

            for index in range(len(roads)):

                for road in roads[index]:

                    position = road.get_position()

                    if road.get_heading() == "N" or road.get_heading() == "S":
                        self.draw_rect(grey, position, 25, 10)

                    elif road.get_heading() == "E" or road.get_heading() == "W":
                        self.draw_rect(grey, position, 10, 25)

            for index in range(len(traffic_lights)):

                position = traffic_lights[index][0].get_position()

                if traffic_lights[index][0].get_heading() == "N" or traffic_lights[index][0].get_heading() == "S":
                    self.draw_rect(traffic_lights[index][0].get_fase(), position, 25, 10)

                elif traffic_lights[index][0].get_heading() == "E" or traffic_lights[index][0].get_heading() == "W":
                    self.draw_rect(traffic_lights[index][0].get_fase(), position, 10, 25)

            traffic_light_controller.get_connection_data()
            kill = []

            if agents and (count % random.randint(self.agent_spawn_rate, self.agent_spawn_rate + 15) == 0 or count == 0):
                active_agents.append(agents[0])
                agents.pop(0)

            for agent in active_agents:

                if agent.is_alive():
                    agent.step_to_next_node()
                    if agent.get_current_node().get_heading() == "N":
                        self.draw_rect(agent.get_color(), agent.get_current_node().get_position(), agent_width,
                                       agent_height, agent_x_offset, agent_y_offset)
                    elif agent.get_current_node().get_heading() == "S":
                        self.draw_rect(agent.get_color(), agent.get_current_node().get_position(), agent_width,
                                       agent_height, agent_x_offset, -agent_y_offset)

                    elif agent.get_current_node().get_heading() == "E":
                        self.draw_rect(agent.get_color(), agent.get_current_node().get_position(), agent_height,
                                       agent_width, -agent_y_offset, agent_x_offset)
                    else:
                        self.draw_rect(agent.get_color(), agent.get_current_node().get_position(), agent_height,
                                       agent_width, agent_y_offset, agent_x_offset)

                else:
                    kill.append([agent, time.time() - agent.get_time()])
                    self.kill_total.append([agent, time.time() - agent.get_time()])


            for agent in kill:
                active_agents.remove(agent[0])
                self.draw_rect(grey, agent[0].get_current_node().get_position(), 10, 25)


            pygame.display.update()
            time.sleep(self.tick_rate)
            count += 1

            if len(active_agents) == 0:

                average_time_car = 0

                average_time_busses = 0

                amount_of_cars = 0

                amount_of_busses = 0

                for i in self.kill_total:

                    if i[0].get_kind() == "auto":
                        amount_of_cars += 1
                        average_time_car += i[1]

                    if self.get_allow_busses:
                        if i[0].get_kind() == "bus":
                            amount_of_busses += 1
                            average_time_busses += i[1]

                try:
                    return time.time() - self.start, average_time_car / amount_of_cars, average_time_busses / amount_of_busses
                except ZeroDivisionError:
                    return time.time() - self.start, average_time_car / amount_of_cars, "Nan"

    def draw_rect(self, color, position, width, height, offset_x=0, offset_y=0, padding=0):

        """

        this function draws the shape of the rectangle

        Parameters
            color: (tuple) tuple with color set
            position: (tuple) a tuple with x y cordinates
            width: (int) an integer that gives the width of a rectangle
            height: (int) an integer that gives the height of a rectangle
            offset_x: (int) an integer that gives the offset x of a rectangle
            offset_y: (int)  an integer that gives the offset y of a rectangle
            padding: (int) an integer that gives the padding of the rectangle
        """

        pygame.draw.rect(self.screen, color, pygame.Rect(position[0] + offset_x,
                                                         position[1] + offset_y,
                                                         width,
                                                         height), padding)
