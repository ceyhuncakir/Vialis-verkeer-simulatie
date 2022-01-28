class Road:
    def __init__(self, position, has_sensor, crossing_point, road_id, heading, gates, busslane):

        """
        Road class initializer to create an Road whithin a map

        Parameters:
            position (tuple): a tuple of position for the road
            has_sensor (bool): a bool if the road has a sensor
            crossing_point (str): a string if a road is crossing
            road_id (str): a road id for the road
            heading (str): a heading for the string
            gates (list): a list of gates for the road
            busslane (str): a string which indicates if the road is a busslane
        """

        self.road_id = road_id
        self.position = position  # x, y
        self.connections = {}
        self.has_sensor = has_sensor
        self.occupied = False
        self.crossing_point = crossing_point
        self.traffic_light = None
        self.heading = heading
        self.crossing = None
        self.gates = gates
        self.busslane = busslane

    def set_traffic_light(self, traffic_light):

        """

        this functions sets the traffic light for the road

        Parameters:
            traffic_light (object): traffic light object to set it for the road


        """

        self.traffic_light = traffic_light

    def get_traffic_light(self):

        """

        this function gets the traffic light of an road

        Returns:
            returns the traffic light object of the road

        """

        return self.traffic_light

    def set_occupied(self, is_occupied):

        """

        this functions set the occupation of an road

        Parameters:
            is_occupied (bool): sets the occupation to a boolean
        """

        self.occupied = is_occupied

    def is_occupied(self):

        """

        this function returns a bool for the occupation of a road

        Returns:
            returns the occupation of a road
        """

        return self.occupied

    def get_crossing_point(self):

        """

        this functions gets the crossing point of road


        Returns:
            returns the crossing_point of a road
        """

        return self.crossing_point

    def add_connections(self, gate, node):

        """

        this function adds the connection of a specific gate to a road

        Parameters:
            gate (str): a string that is contained with the gate
            node (object): a object node so there is a connection between a gate and a node
        """

        self.connections[gate] = node

    def get_connections(self, key):

        """

        this functions gets the connections of a key

        Parameters:
            key (str): a string which holds the key (gate) to get all the connections for it
        """

        return self.connections[key]

    def get_sensor(self):

        """

        this functions returns the sensor of the road

        Returns:
            returns a boolean which indicates if a road has a sensor
        """

        return self.has_sensor

    def get_position(self):

        """

        this functions gets the position of a road

        Returns:
            returns the position of the road in a tuple
        """

        return self.position

    def get_road_id(self):

        """

        this functions gets the road id

        Returns:
            returns the road id of the road
        """

        return self.road_id

    def get_heading(self):

        """

        this functions gets the heading of a road

        Returns:
            returns the heading of the road
        """

        return self.heading

    def get_crossing(self):

        """

        this functions gets the crossing of a road

        Returns:
            returns the crossing of the road
        """

        return self.crossing

    def set_crossing(self, crossing):

        """

        this functions sets the crossing of the road

        Parameters:
            crossing (str): sets the crossing of the road
        """

        self.crossing = crossing

    def get_gates(self):

        """

        this function gets the gates of the road

        Returns:
            returns the amount of gates on a road
        """

        return self.gates

    def get_busslane(self):

        """

        this function gets a boolean if the road is busslane 

        Returns:
            returns a boolean which indicates if the road is a busslane or not
        """

        return self.busslane
