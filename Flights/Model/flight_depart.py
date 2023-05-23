class FlightDepart:

    def __init__(self,
                 airline="",
                 flight_num="",
                 came_to="",
                 terminal="",
                 schedule_time="",
                 updated_time="",
                 status=""):
        self._airline = airline
        self._flight_num = flight_num
        self._came_to = came_to
        self._terminal = terminal
        self._schedule_time = schedule_time
        self._updated_time = updated_time
        self._status = status

    def get_airline(self):
        return self._airline

    def set_airline(self, airline):
        self._airline = airline

    def get_flight_num(self):
        return self._flight_num

    def set_flight_num(self, flight_num):
        self._flight_num = flight_num

    def get_came_to(self):
        return self._came_to

    def set_came_to(self, came_to):
        self._came_to = came_to

    def get_terminal(self):
        return self._terminal

    def set_terminal(self, terminal):
        self._terminal = terminal

    def get_schedule_time(self):
        return self._schedule_time

    def set_schedule_time(self, schedule_time):
        self._schedule_time = schedule_time

    def get_updated_time(self):
        return self._updated_time

    def set_updated_time(self, updated_time):
        self._updated_time = updated_time

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status
