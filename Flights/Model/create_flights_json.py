import json
import constants as const

"""
This class is responsible for saving the flight data in the Json files.
"""

class CreateJson:
    def __init__(self, all_flights, flight_type):
        self._all_flights = all_flights
        self._flight_type = flight_type

        if str(self._flight_type) == "arrival":
            for flight in self._all_flights:
                self.write_arrival_to_json(flight)

        elif str(self._flight_type) == "depart":
            for flight in self._all_flights:
                self.write_depart_to_json(flight)

    def write_arrival_to_json(self, flight):
        json_obj_style = {
            "Airline": flight.get_airline().lower(),
            "Flight_Num": flight.get_flight_num(),
            "Came_From": flight.get_came_from(),
            "Terminal": flight.get_terminal(),
            "Schedule_Time": flight.get_schedule_time(),
            "Update_Time": flight.get_updated_time(),
            "Status": flight.get_status()
        }
        json_object = json.dumps(json_obj_style)
        dir_path = const.FLIGHTS_ARRIVAL_JSONS_PATH
        self.create_file(dir_path, flight.get_flight_num(), json_object)

    def write_depart_to_json(self, flight):
        json_obj_style = {
            "Airline": flight.get_airline().lower(),
            "Flight_Num": flight.get_flight_num(),
            "Came_To": flight.get_came_to(),
            "Terminal": flight.get_terminal(),
            "Schedule_Time": flight.get_schedule_time(),
            "Update_Time": flight.get_updated_time(),
            "Status": flight.get_status()
        }
        json_object = json.dumps(json_obj_style)
        path = const.FLIGHTS_DEPART_JSONS_PATH
        self.create_file(path, flight.get_flight_num(), json_object)

    def create_file(self, path, flight_num, json_object):
        file_name = flight_num + ".json"
        file_full_path = path + file_name
        try:
            with open(file_full_path, "w") as outfile:
                outfile.write(json_object)
        except:
            print("Can't open file")
            pass
