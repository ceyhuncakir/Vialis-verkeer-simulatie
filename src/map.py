from road import Road
from traffic_light import TrafficLight
from traffic_light_controller import TrafficLightController


def direction(heading):

    """

    this function returns the direction of the given get_heading

    parameters:
        heading (str): a string representing the direction

    returns:
        Returns a tuple representing the direction

    """

    N = (0, -2)
    E = (2, 0)
    S = (0, 2)
    W = (-2, 0)

    if heading == "N":
        return N
    elif heading == "E":
        return E
    elif heading == "S":
        return S
    elif heading == "W":
        return W


def create_roads(amount, position, traffic_lights_controller, traffic_lights, id, compass, gate, busslane):

    """

    this function creates the roads on the map

    Parameters:
        amount (int): the amount of roads that will be create_roads
        position (tuple): a tuple of x y coordinates
        traffic_lights_controller (TrafficLightController):
        traffic_lights (traffic_light):
        id (int): unique road id
        compass ():
        gate (gate):
        busslane (bool): a boolean wich decides whether or not the road will be a busslane

    Returns:
        The list of the roads

    """

    road_list = []

    heading = direction(compass)

    for i in range(amount):
        # verandert dit met de amount - 20 zodat je de laatse stuk kan pakken van de road

        # dit is waar de auto de object van de traffic light krijgt
        if i == amount - 40:
            road_list.append(Road(position, False, "start", id, compass, gate, busslane))
            position = [position[0] + heading[0], position[1] + heading[1]]
            continue

        # dit is waar de auto stopt
        elif i == amount - 3:
            road_list.append(Road(position, True, "end", id, compass, gate, busslane))
            position = [position[0] + heading[0], position[1] + heading[1]]
            for y in range(len(traffic_lights)):
                if road_list[i].get_road_id() == traffic_lights[y][0].get_road_id():
                    traffic_lights_controller.add_lus_connections(traffic_lights[y][0], [road_list[i]])
            continue

        road_list.append(Road(position, False, False, id, compass, gate, busslane))
        position = [position[0] + heading[0], position[1] + heading[1]]

    for i in range(len(road_list) - 1):
        for y in range(0, len(gate)):
            road_list[i].add_connections(gate[y], road_list[i + 1])

    return road_list


class Map:
    def __init__(self, configuration):


        """
        Map class initializer to create an map

        Parameters:
            configuration (object): an configuration object which helds information

        """

        self.gates = [f"gate_0{x}" for x in range(configuration.get_gates())]
        self.roads = []
        self.agents = []
        self.traffic_lights = []
        self.tick_rate = configuration.get_tick_rate()
        self.red_time = configuration.get_red_time()
        self.green_time = configuration.get_green_time()
        self.orange_time = configuration.get_orange_time()
        self.map = self.get_crossing_map(configuration.get_crossing_type())
        self.traffic_light_controller = TrafficLightController(configuration)

    def setup_map(self):

        """
        this function setups everything like traffic lights map lane connections and traffic light crossing
        """

        self.create_traffic_lights()
        self.create_map()

        self.connect_traffic_light_with_crossing()
        self.create_lane_connections()

    def create_traffic_lights(self):

        """
        this functions creates the traffic lights.
        """

        self.south_id = 100
        self.north_id = 200
        self.east_id = 300
        self.west_id = 400

        for item in self.map:

            if len(item[2]) > 1:
                if item[0] == "S":
                    self.traffic_lights.append([TrafficLight(str(self.south_id), "S", self.red_time,
                                                             self.green_time, self.orange_time, item[4], item[5]), item])
                    self.south_id += 1
                elif item[0] == "N":
                    self.traffic_lights.append([TrafficLight(str(self.north_id), "N", self.red_time,
                                                             self.green_time, self.orange_time, item[4], item[5]), item])
                    self.north_id += 1
                elif item[0] == "E":
                    self.traffic_lights.append([TrafficLight(str(self.east_id), "E", self.red_time,
                                                             self.green_time, self.orange_time, item[4], item[5]), item])
                    self.east_id += 1
                elif item[0] == "W":
                    self.traffic_lights.append([TrafficLight(str(self.west_id), "W", self.red_time,
                                                             self.green_time, self.orange_time, item[4], item[5]), item])
                    self.west_id += 1

    def create_map(self):

        """
        this function creates the road by getting the road structure from map. based on this information it builds out the roads.
        """

        for i in range(len(self.map)):

            if len(self.map[i][2]) > 1:

                if self.map[i][0] == "S":
                    for traffic_light in range(len(self.traffic_lights)):
                        if self.map[i] == self.traffic_lights[traffic_light][1]:
                            self.roads.append(
                                create_roads(self.map[i][3], self.map[i][1], self.traffic_light_controller,
                                             self.traffic_lights, self.traffic_lights[traffic_light][0].get_road_id(),
                                             self.map[i][0],
                                             self.map[i][2], self.map[i][5]))
                elif self.map[i][0] == "N":
                    for traffic_light in range(len(self.traffic_lights)):
                        if self.map[i] == self.traffic_lights[traffic_light][1]:
                            self.roads.append(
                                create_roads(self.map[i][3], self.map[i][1], self.traffic_light_controller,
                                             self.traffic_lights, self.traffic_lights[traffic_light][0].get_road_id(),
                                             self.map[i][0],
                                             self.map[i][2], self.map[i][5]))
                elif self.map[i][0] == "E":
                    for traffic_light in range(len(self.traffic_lights)):
                        if self.map[i] == self.traffic_lights[traffic_light][1]:
                            self.roads.append(
                                create_roads(self.map[i][3], self.map[i][1], self.traffic_light_controller,
                                             self.traffic_lights, self.traffic_lights[traffic_light][0].get_road_id(),
                                             self.map[i][0],
                                             self.map[i][2], self.map[i][5]))
                elif self.map[i][0] == "W":
                    for traffic_light in range(len(self.traffic_lights)):
                        if self.map[i] == self.traffic_lights[traffic_light][1]:
                            self.roads.append(
                                create_roads(self.map[i][3], self.map[i][1], self.traffic_light_controller,
                                             self.traffic_lights, self.traffic_lights[traffic_light][0].get_road_id(),
                                             self.map[i][0],
                                             self.map[i][2], self.map[i][5]))
            else:
                self.roads.append(create_roads(self.map[i][3], self.map[i][1], self.traffic_light_controller,
                                               self.traffic_lights, "0", self.map[i][0],
                                               self.map[i][2], self.map[i][5]))

    def get_crossing_map(self, crossing):

        """

        this functions gets the road structure for the map. the user can build there own road structure by adding the direction positions gates etc.


        Parameters:
            crossing (str): the crossing the user selects

        Returns:
            returns the created map that the used has implemented
        """

        if crossing == "T":
            return [["E", (980, 500), [self.gates[1]], 480, "None", "False"],
                    ["W", (918, 500), [self.gates[0]], 480, "None", "False"],
                    ["S", (940, 0), [self.gates[1], self.gates[0]], 240, "None", "False"]]  # first gate = self
        elif crossing == "X":
            return [["S", (940, 600), [self.gates[0]], 240, "None", "False"],
                    ["S", (900, 600), [self.gates[15]], 240, "None", "False"],
                    ["N", (980, 471), [self.gates[1]], 237, "None", "False"],  # afslag naar north
                    ["E", (1030, 550), [self.gates[2]], 455, "None", "False"],
                    ["W", (867, 510), [self.gates[3]], 435, "None", "False"],
                    ["N", (980, 1080), [self.gates[1], self.gates[3], self.gates[2]], 240, "voorgaandeweg_02", "False"],  # stoplicht naar north
                    ["S", (940, 0), [self.gates[0], self.gates[3], self.gates[2]], 236, "voorgaandeweg_02", "False"],
                    ["S", (900, 0), [self.gates[15], self.gates[15]], 236, "None", "True"],
                    # stoplicht naar south # afslag naar east
                    ["E", (0, 550), [self.gates[2], self.gates[1], self.gates[0]], 435, "None", "False"],
                    ["W", (1920, 510), [self.gates[3], self.gates[1], self.gates[0]], 446, "None", "False"]
                    ]  # first gate = self
        elif crossing == "T2":
            return [["N", (980, 471), [self.gates[0]], 240, "None", "False"],
                    ["E", (1030, 550), [self.gates[2]], 480, "None", "False"],
                    ["W", (918, 510), [self.gates[3]], 480, "None", "False"],
                    ["S", (940, 0), [self.gates[3], self.gates[2]], 236, "None", "False"],
                    ["E", (0, 550), [self.gates[2], self.gates[0]], 460, "None", "False"],
                    ["W", (1920, 510), [self.gates[3], self.gates[0]], 446, "None", "False"]]  # first gate = self
        else:
            raise ValueError("no valid crossing")

    def create_lane_connections(self):

        """
        this function creates the lane connection from one end of the lane to the beginning of another lane
        """

        juiste_wegen = []
        onjuiste_wegen = []

        for road in self.roads:

            if not road[-40].get_traffic_light():
                juiste_wegen.append(road)
            else:
                onjuiste_wegen.append(road)

        for weg in juiste_wegen:
            for stoplichten in range(len(onjuiste_wegen)):

                if weg[0].get_gates()[0] in onjuiste_wegen[stoplichten][0].get_gates():
                    onjuiste_wegen[stoplichten][-1].add_connections(weg[0].get_gates()[0], weg[0])


    def connect_traffic_light_with_crossing(self):

        """
        this function connects the traffic light with the road and sets the traffic light position to the position of the connected road
        """

        for i in range(len(self.roads)):
            for y in range(len(self.traffic_lights)):
                if self.traffic_lights[y][0].get_road_id() == self.roads[i][len(self.roads[i]) - 40].get_road_id():
                    self.roads[i][len(self.roads[i]) - 40].set_traffic_light(self.traffic_lights[y][0])

                    # traffic light position
                    self.traffic_lights[y][0].set_position(
                        (self.roads[i][len(self.roads[i]) - 1].get_position()[0],
                         self.roads[i][len(self.roads[i]) - 1].get_position()[1]))

    def get_roads(self):

        """
        this functions gets the roads that are avaiable within a list

        Returns:
            returns a list with roads
        """

        return self.roads

    def get_traffic_controller(self):

        """
        this function gets the traffic light controller

        Returns the traffic light controller
        """

        return self.traffic_light_controller

    def get_traffic_lights(self):

        """
        this function gets a list with avaiable traffic lights within

        Returns a list with the traffic lights
        """

        return self.traffic_lights
