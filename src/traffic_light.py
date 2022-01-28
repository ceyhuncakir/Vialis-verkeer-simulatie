class TrafficLight:
    def __init__(self, road_id, heading, red_time, green_time, orange_time, neighbour, busslane):

        """
        TrafficLight class initializer to create an trafficlight whithin a map

        Parameters:
            road_id (str): an id for a road
            heading (str): a heading for a road
            red_time (int): an integer for the red time
            green_time (int): an integer for the green time
            orange_time (int): an integer for the orange time
            neighbour (str): an neighbour id for a road
            busslane (bool): a boolean which indicates if its a busslane trafficlight
        """

        self.road_id = road_id
        self.fase = (255, 0, 0)
        self.position = None
        self.red_time = red_time
        self.green_time = green_time
        self.orange_time = orange_time
        self.timer = self.red_time
        self.is_activated = False
        self.done = False
        self.heading = heading
        self.neighbour = neighbour
        self.busslane = busslane

    def set_fase(self, fase):

        """

        this function sets the fase for the traffic light

        Parameters:
            fase (tuple): a tuple with color which is for the fase

        """

        self.fase = fase

    def set_position(self, position):

        """

        this function sets the position cordinates of the traffic light

        Parameters:
            position (tuple): an tuple with x y cordinates for the traffic_light

        """

        self.position = position

    def get_fase(self):

        """

        this functions gets the traffic light fase

        Returns:
            the fase which the traffic_light is at

        """

        return self.fase

    def get_road_id(self):

        """

        this function gets the road id of the traffic light

        Returns:
            the traffic_light id

        """

        return self.road_id

    def get_position(self):

        """

        this function gets the position cordinates of the traffic light

        Returns:
            the position which the traffic light is at

        """

        return self.position

    def is_done(self):

        """

        this function return the state of done

        Returns:
            the state done which says that the cycle whithin the traffic_light is done

        """

        return self.done

    def is_active(self):

        """

        this function returns the activated state

        Returns:
            returns a boolean

        """

        return self.is_activated

    def set_activated(self, is_activated):

        """

        this function can either set the traffic light to activated or not activated

        Parameters:
            is_activated (bool): a boolean which indicates if the traffic_light should be activated or not

        """

        self.is_activated = is_activated

    def step(self):

        """

        this function runs the cycle process of the traffic light and changes the lights to the corresponding fase

        """

        if self.fase == (255, 0, 0) and self.is_activated:
            if self.done:
                self.done = False


            self.change_lights((0, 255, 0), self.green_time)

        elif self.fase == (0, 255, 0):
            self.change_lights((255, 165, 0), self.orange_time)

        elif self.fase == (255, 165, 0):
            self.change_lights((255, 0, 0), self.red_time)

    def change_lights(self, colour, time):

        """

        this functions changes the light of the traffic light based on the color parameter and time parameter

        Parameters:
            colour (tuple): a tuple, within a tuple there is a set of colours which indicates the color of the traffic light
            time (int): a integer on how long a specific colour should be a active for

        """

        self.timer -= 1
        if self.timer <= 0:
            self.fase = colour
            self.timer = time
            self.set_activated(False)
            if colour == (255, 0, 0):
                self.done = True

    def get_heading(self):

        """

        this functions returns the heading of the traffic light

        Returns:
            returns the heading of the traffic light

        """

        return self.heading

    def get_neighbour(self):

        """

        this functions returns a string which indicates in which group is belongs too

        Returns:
            returns a string which indicates in which neighbour group it belongs too

        """

        return self.neighbour

    def get_buss_lane(self):

        """

        this function returns a boolean that can tell if the traffic light is a busslane traffic light or not

        Returns:
            returns a boolean if the traffic light is a busslane or not

        """

        return self.busslane
