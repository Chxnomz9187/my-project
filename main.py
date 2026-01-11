from cinema import CinemaSystem, Cinema, CinemaHall
from user import Person, Admin


def main():
    cinema_system = CinemaSystem()
    cinema_central = Cinema("Central World", "Central World", 15)
    cinema_system.add_cinema(cinema_central)
    cinema_system.show_cinema()
    cinema_central.add_halls(CinemaHall("Hall1", "nf First Class Cinema", 90))
    cinema_central.add_halls(CinemaHall("Hall2", "nf First Class Cinema", 90))
    cinema_central.add_halls(CinemaHall("Hall3", "MX4D", 90))
    cinema_central.add_halls(CinemaHall("Hall4", "ZIGMA CINESTADIUM", 90))
    cinema_central.add_halls(CinemaHall("Hall5", "Bed Cinema", 90))
    cinema_central.add_halls(CinemaHall("Hall6", "Mastercard Cinema", 90))
    cinema_central.add_halls(CinemaHall("Hall7", "Standard Cinema", 90))
    cinema_central.add_halls(CinemaHall("Hall8", "Standard Cinema", 90))
    cinema_central.add_halls(CinemaHall("Hall9", "Standard Cinema", 90))

    admin = Admin("Admin", "admin@abc.com", "081-234-5678")
    print(admin)


if __name__ == "__main__":
    main()
