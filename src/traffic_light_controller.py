class TrafficLightController:
    def __init__(self, configuration):


        """

        trafficlight controller class initializer to create an traffic light controller within a map

        Parameters:
            configuration (object): an configuration object that holds information

        """

        self.lus_connections = {}
        self.timer = {}
        self.active_traffic_lights = []

        self.bus_lane_priority = configuration.get_bus_lane_priority()

    def add_lus_connections(self, key, node):

        """

        this functions creates a lus connection between an traffic light and a road

        Parameters:
            key (object): a traffic light object
            node (object): a road object

        """

        self.lus_connections[key] = node

    def get_lus_connections(self, key):

        """

        this functions gets the connection between a traffic light conntroller and a road

        Parameters:
            key (object): an traffic light object

        Returns:
            returns the lus connections with the desired key

        """
        return self.lus_connections[key]

    def get_connection_data(self):

        """
        this functions checks all the traffic lights and decides which traffic light should be activated first based on the amount of time an agent has been waiting for each traffic light        
        """

        for key, value in self.lus_connections.items():

            if key.get_buss_lane() == "True":
                if value[0].is_occupied():
                    if key not in self.active_traffic_lights:
                        if self.bus_lane_priority == "True":
                            self.active_traffic_lights.insert(0, key)
                        else:
                            self.active_traffic_lights.append(key)

            if value[0].is_occupied():
                if key not in self.active_traffic_lights:
                    self.active_traffic_lights.append(key)


        if self.active_traffic_lights:

            current_light = self.active_traffic_lights[0]

            if len(self.active_traffic_lights) > 0:

                for i in range(1, len(self.active_traffic_lights)):

                    try:
                        if current_light.get_neighbour() == "None" or self.active_traffic_lights[i].get_neighbour() == "None":
                            continue
                        else:

                            if current_light.get_neighbour() == self.active_traffic_lights[i].get_neighbour():

                                self.active_traffic_lights[i].set_activated(True)
                                if self.active_traffic_lights[i].is_done():
                                    self.active_traffic_lights[i].step()
                                    self.active_traffic_lights[i].set_activated(False)
                                    self.active_traffic_lights.pop(self.active_traffic_lights.index(self.active_traffic_lights[i]))
                                if self.active_traffic_lights[i].is_active():
                                    self.active_traffic_lights[i].step()


                    except IndexError:
                        continue

                current_light.set_activated(True)
                if current_light.is_done():
                    current_light.step()
                    current_light.set_activated(False)
                    self.active_traffic_lights.pop(self.active_traffic_lights.index(current_light))
                if current_light.is_active():
                    current_light.step()
