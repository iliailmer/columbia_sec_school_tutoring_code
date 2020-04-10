from bus import Bus
from passenger import Passenger


if __name__ == "__main__":
    input("Let's look at a simple example: a bus and a passenger\n" +
          "Press Enter to continue...")

    b = Bus(2.75, 10)
    p = Passenger(5.5)

    input(f"Bus fare is ${b.fare} and the Passenger has ${p.cash}\n" +
          f"Press Enter to continue...")

    if p.can_I_get_on_the_bus(b):
        b.accept_passenger()
        print(f"Passenger accepted! He now has ${p.cash} left!\n")
    else:
        print(f"The passenger could not get on!" +
              f"He only had ${p.cash}, :(")

    input("Let's look at another example: a bus with 3 stops\n" +
          "Press Enter to continue...")

    # each number here is a distance to the
    # hypothetical stop from the start
    # here could be an exercise to improve it: make a class BusStop
    # that would have n passengers and be x miles away from the bus
    stops = [i for i in range(1, 3)]
    b = Bus(2.75, 10)
    p = Passenger(5.5)

    input(f"Bus fare is ${b.fare} and the Passenger has ${p.cash}\n" +
          f"Press Enter to continue...")
    input(f"\nWe want the passenger to get on at the 1st stop " +
          f"and get off at the 3rd stop.\n" +
          f"Press Enter to continue...")

    for stop in stops:
        # make bus go to the next stop
        # this could be an exercise:
        # how to make the bus travel to the next stop
        b.go(stop - b.distance_travelled)

        if b.distance_travelled == 1:
            input(f"\nBus is at stop 1!\n" +
                  f"Press Enter to continue...")

        if b.distance_travelled == stops[-1]:
            input(f"\nBus is at stop 3!\nPassenger getting out!\n" +
                  f"Press Enter to continue...")
            b.let_out_passenger()

        if p.can_I_get_on_the_bus(b):
            input(f"\n'Oh, boy! It's my bus!" +
                  "'Let's see if I can get on it...'\n" +
                  f"Press Enter to continue...")
            b.accept_passenger()

            input(f"'\nI made it! The bus now has" +
                  f" {b.passenger_count} passenger(s)!'\n" +
                  f"Press Enter to continue...")
