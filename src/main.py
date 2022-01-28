from configuration import Configuration
from simulation import Simulation
import argparse
import random


class GUI:
    def __init__(self, tick_rate, gates, agent_spawn_amount, agent_spawn_rate, crossing_type, iterations, red_time,
                 green_time, orange_time, spawn_direction, allow_busses, amount_bus, bus_lane_priority):

        """

        GUI class initializer to create an GUI whithin a map

        Parameters:
            tick_rate (float) a float with a amount
            gates (list) a list with gates
            agent_spawn_amount (list) a list with agent spawn amounts
            agent_spawn_rate (list) a list with agent spawn rates
            crossing_type (list) a list with crossing types
            iterations (int) a int with the amount of iterations
            red_time (list) a list with red times
            green_time (list) a list with green times
            orange_time (list) a list with orange times
            spawn_direction (list(dict)) a list with spawn direction with the amounts
            allow_busses (list) a list with boolean for allowing busses
            amount_bus (list(dict)) a list with busses that has a dict with the amount
            bus_lane_priority (list) a list with booleans to allow priority
        """

        self.tick_rate = tick_rate
        self.gates = gates
        self.agent_spawn_amount = agent_spawn_amount
        self.agent_spawn_rate = agent_spawn_rate
        self.crossing_type = crossing_type
        self.iterations = iterations
        self.red_time = red_time
        self.green_time = green_time
        self.orange_time = orange_time
        self.spawn_direction = spawn_direction
        self.allow_busses = allow_busses
        self.amount_bus = amount_bus
        self.bus_lane_priority = bus_lane_priority

    def start_simulation(self):

        """
        this function starts the simulation in batches and prints out the output of each batch
        """

        times = []
        for x in range(self.iterations):
            configuration = Configuration(self.tick_rate, self.gates, self.spawn_direction[x],
                                          self.agent_spawn_rate[x],
                                          self.crossing_type[x], self.red_time[x], self.green_time[x],
                                          self.orange_time[x], self.allow_busses[x], self.amount_bus[x], self.bus_lane_priority[x])
            simulation = Simulation(configuration)
            total, average_car_flow_time, average_bus_flow_time = simulation.run_simulation()
            times.append(total)
            print(f"Batch {x + 1}: Total time: {total} seconds\t Average car flow time: {average_car_flow_time}      Average bus flow time: {average_bus_flow_time}")


if __name__ == "__main__":


    """
    all the arguments that are avaiable for the user
    """

    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-tr', '--tick_rate', help='The amount of ticks of the simulation', type=float, default=0.01)
    parser.add_argument('-m', '--map', help='The map the simulation will play in', nargs="*", type=str,
                        default=["X", "X", "X", "T2"])

    parser.add_argument('-sd', '--spawn_direction',
                        help='The spawn rate which the agents spawn within the simulation', type=int, default=[{"N": 10, "S": 10, "E": 10}, {"N": 10, "S": 10, "E": 10}, {"N": 10, "S": 10, "E": 10}, {"S": 10, "E": 10, "W": 10}])

    parser.add_argument('-asr', '--agent_spawn_rate',
                        help='The spawn rate which the agents spawn within the simulation', nargs="*", type=int,
                        default=[10, 30, 30, 30])
    parser.add_argument('-rt', '--red_time',
                        help='The spawn rate which the agents spawn within the simulation', nargs="*", type=int,
                        default=[205, 205, 205, 205])
    parser.add_argument('-gt', '--green_time',
                        help='The spawn rate which the agents spawn within the simulation', nargs="*", type=int,
                        default=[120, 120, 120, 120])
    parser.add_argument('-ot', '--orange_time',
                        help='The spawn rate which the agents spawn within the simulation', nargs="*", type=int,
                        default=[50, 50, 50, 50])
    parser.add_argument('-it', '--iterations',
                        help='The spawn rate which the agents spawn within the simulation', type=int, default=4)

    parser.add_argument('-ab', '--allow_busses',
                        help='The spawn rate which the agents spawn within the simulation', nargs="*", type=bool, default=[True, True, True, False])

    parser.add_argument('-amb', '--amount_bus',
                        help='The spawn rate which the agents spawn within the simulation', nargs="*", type=dict, default=[{"B": 5}, {"B": 5}, {"B": 5}, {"B": 5}])

    parser.add_argument('-blp', '--bus_lane_priority',
                        help='The spawn rate which the agents spawn within the simulation', nargs="*", type=bool, default=[False, True, False, False])

    args = parser.parse_args()
    gui = GUI(args.tick_rate, 100, args.spawn_direction, args.agent_spawn_rate,
              args.map, args.iterations, args.red_time, args.green_time, args.orange_time, args.spawn_direction, args.allow_busses, args.amount_bus, args.bus_lane_priority)
    gui.start_simulation()
