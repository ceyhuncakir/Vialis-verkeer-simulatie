class Configuration:
    def __init__(self, tick_rate, gates, spawn_direction, agent_spawn_rate, crossing_type, red_time, green_time,
                 orange_time, allow_busses, amount_bus, bus_lane_priority):

        """

        Configuration class initializer to create an Configuration whithin a map

        Parameters:
            tick_rate (float) a float with a amount
            gates (list) a list with gates
            spawn_direction (list(dict)) a list with spawn direction with the amounts
            agent_spawn_rate (list) a list with agent spawn rates
            crossing_type (list) a list with crossing types
            red_time (list) a list with red times
            green_time (list) a list with green times
            orange_time (list) a list with orange times
            allow_busses (list) a list with boolean for allowing busses
            amount_bus (list(dict)) a list with busses that has a dict with the amount
            bus_lane_priority (list) a list with booleans to allow priority

        """
        self.tick_rate = tick_rate
        self.gates = gates
        self.agent_spawn_rate = agent_spawn_rate
        self.crossing_type = crossing_type
        self.red_time = red_time
        self.green_time = green_time
        self.orange_time = orange_time
        self.spawn_direction = spawn_direction
        self.allow_busses = allow_busses
        self.amount_bus = amount_bus
        self.bus_lane_priority = bus_lane_priority

    def get_tick_rate(self):

        """

        this functions get the tick rate of the simulation

        Returns:
            returns the tick rate of the simulation
        """

        return self.tick_rate

    def get_gates(self):

        """

        this functions get the gates

        Returns:
            return the gates that are available
        """

        return self.gates

    def get_agent_spawn_rate(self):

        """

        this functions get the agent spawn rate

        Returns:
            returns the agent spawn rate
        """

        return self.agent_spawn_rate

    def get_crossing_type(self):

        """

        this function gets the crossing type

        Returns:
            returns the crossing type
        """

        return self.crossing_type

    def get_red_time(self):

        """

        this functions gets the red time

        Returns:
            returns the red time
        """

        return self.red_time

    def get_green_time(self):

        """

        this functions get the green time

        Returns:
            returns the green time
        """

        return self.green_time

    def get_orange_time(self):

        """

        this functions get the orange time

        Returns:
            returns the orange time
        """

        return self.orange_time

    def get_spawn_direction(self):

        """

        this function gets the spawn direction

        Returns:
            returns the spawn direction
        """

        return self.spawn_direction

    def get_allow_busses(self):


        """

        this functions gets the list of boolean if a specific simulation is allow for busses

        Returns:
            returns the allow busses boolean
        """

        return self.allow_busses

    def get_amount_bus(self):

        """

        this busses gets the amount of busses

        Returns:
            returns the amount of busses
        """

        return self.amount_bus

    def get_bus_lane_priority(self):

        """

        this functions get the bus lane priority

        Returns:
            returns the bus lane priority
        """

        return self.bus_lane_priority
