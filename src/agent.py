import random

def get_mass_spread(average):
    # return een random floating point nummer met normaalverdeling
    return random.normalvariate(average, 500)


class Agent:
    def __init__(self, x, y, kind, start_node, destination, screen_size, direction, color, time):

        """
        Agent class initializer to create an Agent whithin a map

        Parameters:
        position (list): position of the agent
        kind (str): agent kind (for example: car or bus)
        is_moving (bool): is the agent moving (True) or standing still (False)
        alive (bool): is the agent alive
        current_node (Node): the node the agent is occupying at the momenteel
        destination (str): a string with the destination gate
        speed (int): current speed of the Agent
        speed_limit (int): highest possible speed for the Agent
        mass (float): mass of the Agent
        traffic_light_sight (trafficlight): traffic light ahead of the Agent (if in sight)
        color (list): list of color values for the agent
        screen_width (int): width of the screen according to pygame
        screen_height (int): height of the screen according to pygame
        direction (str): direction the agent is heading in
        time (time): the spawn time of the agent
        """
        self.position = [x, y]
        self.kind = kind
        self.is_moving = False
        self.alive = True
        self.current_node = start_node
        self.current_node.set_occupied(True)
        self.destination = destination
        self.speed = 0
        self.speed_limit = 50
        self.mass = self.get_mass()
        self.traffic_light_sight = None
        self.color = color
        self.screen_width = screen_size[0]
        self.screen_height = screen_size[1]
        self.direction = direction
        self.time = time

    def get_mass(self):

        """

        this function gets the mass for the Agent

        Returns:
            The mass of the Agent (depending if it is a car or a bus)

        """

        if self.kind == "auto":
            return get_mass_spread(1293.0)  # average car mass based on most frequent used cars

        elif self.kind == "bus":
            return get_mass_spread(11925.0)  # average ariva bus mass based on

    def set_current_node(self, current_node):

        """

        this function sets the current_node of the Agent and sets the node.set_occupied to True

        Parameters:
            current_node (node): the node the Agent is currently on

        """

        self.current_node = current_node
        self.current_node.set_occupied(True)

    def get_current_node(self):

        """

        this function gets the current_node of the Agent

        Returns:
            The current_node of the Agent

        """

        return self.current_node

    def get_position(self):

        """

        this function gets the position of the Agent

        Returns:
            The position of the Agent (tuple with x y coordinates)

        """

        return self.position

    def step_to_next_node(self):

        """

        this function checks if the Agent can continue to the next Node

        First it checks if the Agent has entered a 'start' node AND
        doesnt currently see a traffic light, if these conditions are met,
        then set the traffic_light_sight to the upcoming traffic light.

        if the above conditions are not met (so either the Agent is not in a 'start' node,
        or it already sees a traffic light), then it checks if the Agent is at the end of a road,
        and if it sees a traffic light, then depending on the current fase of the traffic light,
        the Agent either breaks (if light is red),
        keeps driving (if light is green)
        or checks the check_brake() function (if light is orange)

        if none of the above conditions are met, then the Agent just keeps driving

        """

        if self.current_node.get_crossing_point() == "start" and not self.traffic_light_sight:
            self.traffic_light_sight = self.current_node.get_traffic_light()

        elif self.current_node.get_crossing_point() == "end" and self.traffic_light_sight:
            if self.traffic_light_sight.get_fase() == (255, 0, 0):
                if self.speed > 0:
                    self.brake()
                return
            elif self.traffic_light_sight.get_fase() == (0, 255, 0):
                self.drive()
                self.traffic_light_sight = None
                return
            elif self.traffic_light_sight.get_fase() == (255, 95, 21):
                if self.speed > 0:
                    self.check_brake()
                return

        self.drive()

    def drive(self):

        """

        out_of_north, out_of_east, out_of_south, out_of_west are booleans
        that are updated while the Agent is driving (they each check if the car is driving out of the map,
        depending on direction and position),

        if one of the conditions are True,
        then the should_be_killed parameter will be set to True

        then it check if the should_be_killed bool is True, if so,
        then set the current node to unoccupied and 'kill' the agent

        if should_be_killed is False, then check if the car is not moving, if so,
        set the speed to 0 and is_moving to True

        then start a loop of 8 iterations which checks if the next 8 nodes are occupied or not,
        if 1 of the nodes is occupied then return, else get the next node

        then set the current node to unoccupied, and set the next node as the current node
        then set the position of the Agent as the position of the new current nodes

        then check if the Agents speed is below the speed_limit,
        then check if the speed is below 0
        if its below 0, then reset the speed to 0,
        lastly increase the speed based on the mass of the Agent

        """

        out_of_north = self.get_current_node().get_heading() == "N" and self.position[1] <= 16
        out_of_east = self.get_current_node().get_heading() == "E" and self.position[0] >= self.screen_width - 16
        out_of_south = self.get_current_node().get_heading() == "S" and self.position[1] >= self.screen_height - 16
        out_of_west = self.get_current_node().get_heading() == "W" and self.position[0] <= 16
        should_be_killed = out_of_north or out_of_east or out_of_south or out_of_west

        if should_be_killed:
            self.current_node.set_occupied(False)
            self.alive = False
            return
        else:

            if not self.is_moving:
                self.speed = 0
                self.is_moving = True
            node = self.current_node
            for x in range(8):
                try:
                    if node.get_connections(self.destination).is_occupied():

                        return
                    else:
                        node = node.get_connections(self.destination)
                except KeyError:
                    break

            self.current_node.set_occupied(False)
            self.set_current_node(self.current_node.get_connections(self.destination))
            self.position = self.current_node.get_position()
            if self.speed < self.speed_limit:
                if self.speed < 0:
                    self.speed = 0

                self.speed += 0.5 * self.mass * 0.0055


    def check_brake(self):

        """

        this function checks if the Agent is still able to break in time, if so,
        then activate the brake() function of the Agent, otherwise keep driving

        this function is called when the Agent encounters an orange traffic light

        """

        distance = 50
        if distance <= 50:
            self.brake()
        else:
            self.drive()

    def brake(self):

        """

        this function decreases the speed of the Agent, based on the current speed,
        and the mass of the Agent

        """

        if self.speed > 0:
            self.speed -= 1 * self.mass * 0.008
            if self.speed <= 0:
                self.speed = 0
                self.is_moving = False

    def is_alive(self):

        """

        this function gets the is_alive attribute of the Agent

        Returns:
            A bool that represents if the agent is alive (True), or not (False)

        """

        return self.alive

    def get_color(self):

        """

        this function gets the color of the Agent

        Returns:
            The color of the Agent (list with rgb color values)

        """

        return self.color

    def get_direction(self):

        """

        this function gets the direction of the Agent

        Returns:
            The direction of the Agent (String that represents direction (for example: 'N' for north))

        """

        return self.direction

    def get_time(self):

        """

        this function gets the time of the Agent

        Returns:
            The time of the Agent (time value of when the Agent.is_alive was set to True)

        """

        return self.time

    def get_kind(self):

        """

        this function gets the kind of the Agent

        Returns:
            The kind of the Agent (String value (for example: 'auto' or 'bus'))

        """

        return self.kind
