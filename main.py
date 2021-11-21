"""The Mediator class."""
class ControlTower(object):

    def displayAction(self, flight, action):
        print(f"Air traffic controller's communication to {flight}: {action}")

"""A class whose instances want to communicate with each other."""
class Flight(object):

    def __init__(self, flight_name):
        self.flight_name = flight_name
        self.control_tower = ControlTower()

    def Operation(self, action):
        self.control_tower.displayAction(self, action)

    def __str__(self):
        return self.flight_name

"""The main method"""
if __name__ == "__main__":
    mh370 = Flight('MH370')  # first flight object
    flight16 = Flight('Flight 16')  # second flight object
    flight1549 = Flight('Flight 1549')  # third flight object

    mh370.Operation("Flight MH370, I need you outside of Bravo; do you copy?")
    flight16.Operation("Are you still unable to lower the landing gear due to a hydraulic system failure?")
    flight1549.Operation("You are clear to land on Runway 31 at LaGuardia Airport.")
