class Bus:
    """Class the describes a Bus Object."""

    def __init__(self, fare: float, capacity: int) -> None:
        """Initialize an instance of an object called Bus.

        This method can be called as:
        b = Bus(...)

        In `...` you must provide a value of the trip fare and
        the bus' capacity.
        """
        self.fare = fare
        self.distance_travelled = 0.0
        self.capacity = capacity
        self.passenger_count = 0

    def go(self, distance: float) -> None:
        """Travel a distance (from one stop to another).

        This method can be called as:
        b.go(...)

        In `...` you must provide a distance to the next stop.
        """
        self.distance_travelled += distance

    def accept_passenger(self):
        """Accept a passenger.

        If the bus has enough capacity, then
        the passenger count must increase by 1.

        Example:

            b.accept_passenger()
        """
        if self.capacity > self.passenger_count:
            self.passenger_count += 1

    def let_out_passenger(self):
        """On each stop, let a passenger out.

        Example:

        b.let_out_passenger()
        """
        pass
