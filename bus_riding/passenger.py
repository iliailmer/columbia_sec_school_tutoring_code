from bus import Bus


class Passenger:
    """This class describes a passenger."""

    def __init__(self, cash: float) -> None:
        """Initialize an instance of an object called Passenger.

        This method can be called as:
        p = Passenger(...)

        In `...` you must provide a the amount of money a
        passenger has in cash.
        """
        self.cash = cash

    def can_I_get_on_the_bus(self, b: Bus) -> bool:
        """This method checks if I, the passenger, can get on the bus b.

        Example:

        if p.can_I_get_on_the_bus(b):
            # if a passenger can get on, the bus will accept
            # them and they will pay the fare

            b.accept_passenger()
        """
        if self.cash > b.fare:
            self.cash -= b.fare
            return True
        else:
            return False
