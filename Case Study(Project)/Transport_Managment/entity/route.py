# entity/route.py
class Route:
    def __init__(self, RouteID=None, StartDestination=None, EndDestination=None, Distance=None):
        self.RouteID = RouteID
        self.StartDestination = StartDestination
        self.EndDestination = EndDestination
        self.Distance = Distance

    def __str__(self):
        return (f"RouteID: {self.RouteID}, From: {self.StartDestination} To: {self.EndDestination}, "
                f"Distance: {self.Distance}")
