def return_full_name(first_name, last_name):
    return f"{first_name} {last_name}"


def is_valid_card_number(card_number):
    return (sum(list(map(int, [char for char in card_number])))) % 7 == 0


class Ticket:
    ticket_full_name: str
    ticket_dest: str
    ticket_card: str

    def __init__(self, ticket_full_name, ticket_dest, ticket_card=None):
        self.ticket_full_name = ticket_full_name
        self.ticket_dest = ticket_dest
        self.ticket_card = ticket_card

    @property
    def ticket_price(self):
        if not self.ticket_card:
            return sum(list(map(ord, [char for char in self.ticket_dest]))) / 100
        else:
            return sum(list(map(ord, [char for char in self.ticket_dest]))) / 100 * 0.5


class Passenger:
    full_name: str
    disc_cards_list: list
    tickets_list: list
    total_cost: float

    def __init__(self, full_name):
        self.full_name = full_name
        self.disc_cards_list = []
        self.tickets_list = []

    def add_disc_card(self, card_number):
        if card_number not in self.disc_cards_list and is_valid_card_number(card_number):
            self.disc_cards_list.append(card_number)

    def add_ticket(self, ticket):
        self.tickets_list.append(ticket)

    @property
    def total_cost(self):
        return sum([ticket.ticket_price for ticket in self.tickets_list])

    def print_passenger(self):
        sorted_tickets_list = sorted(self.tickets_list, key=lambda t: -t.ticket_price)
        if len(self.tickets_list) > 0:
            print(f"{self.full_name}:")
            for ticket in sorted_tickets_list:
                print(f"--{ticket.ticket_dest}: {ticket.ticket_price:.2f}lv", end="")
                if ticket.ticket_card:
                    print(f" (using card {ticket.ticket_card})")
                else:
                    print()
            print(f"total: {self.total_cost:.2f}lv")


passengers_list = []

n = int(input())
for i in range(n):
    first_name, last_name, card_number = input().split()
    full_name = return_full_name(first_name, last_name)
    if full_name not in [psg.full_name for psg in passengers_list]:
        passenger = Passenger(full_name)
        passenger.add_disc_card(card_number)
        passengers_list.append(passenger)
    else:  # <- note that one passenger may have multiple valid cards
        this_passenger = [psg for psg in passengers_list if psg.full_name == full_name][0]
        this_passenger.add_disc_card(card_number)

while True:
    str_line = input()
    if str_line == "time to leave!":
        sorted_list_of_passengers = sorted(passengers_list, key=lambda psg: -psg.total_cost)
        for psg in sorted_list_of_passengers:
            psg.print_passenger()
        break

    command, first_name, last_name, destination, card_number = str_line.split()
    full_name = return_full_name(first_name, last_name)
    if full_name not in [psg.full_name for psg in passengers_list]:
        passenger = Passenger(full_name)
        passengers_list.append(passenger)

    passenger_to_travel = [psg for psg in passengers_list if psg.full_name == full_name][0]

    ticket_without_discount = Ticket(full_name, destination)
    ticket_with_discount = Ticket(full_name, destination, card_number)

    """Check if the card belongs to someone else"""
    is_someone_else_card = False
    other_passengers_list = [psg for psg in passengers_list if psg.full_name != full_name]
    # list of lists of discount cards for all the other passengers, e.g. [['630534'], ['094859', '328994', '774154']]
    nested_list_of_cards = [psg.disc_cards_list for psg in other_passengers_list]
    # flattened list of all other passengers' cards, e.g. ['630534', '094859', '328994', '774154']
    flat_list_others_cards_numbers = [item for disc_cards_list in nested_list_of_cards for item in disc_cards_list]
    if card_number in flat_list_others_cards_numbers:
        is_someone_else_card = True

    if not is_valid_card_number(card_number):
        print(f"card {card_number} is not valid!")
        passenger_to_travel.add_ticket(ticket_without_discount)
    else:
        if is_someone_else_card:
            print(f"card {card_number} already exists for another passenger!")
            passenger_to_travel.add_ticket(ticket_without_discount)
        else:
            if card_number not in passenger_to_travel.disc_cards_list:
                print(f"issuing card {card_number}")
                passenger_to_travel.add_disc_card(card_number)
            passenger_to_travel.add_ticket(ticket_with_discount)