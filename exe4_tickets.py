"""4. Old Trafford Stadium

The executive management of Manchester United FC aims to implement a ticket sales system for the team's matches
at Old Trafford Stadium. Develop a ticket purchase system with the following features:

Membership Discount:
    -Users with a Manchester United membership card receive a 15% discount on their total purchase.
Seating Capacity and Distribution:
    -The total seating capacity at Old Trafford is 74,310.
    -5% for VIP boxes, 15% for VIP seats, and 80% for general seating.
Seat Selection:
    -Seats are identified by a ticket number from 1 to 74,310.
    -Users can choose their seats.
    -The first seats correspond to VIP boxes, the next to the VIP area,
     and the rest to general seating (considering the percentages).
Ticket Purchase Limits:
    -Users with a membership card can buy up to 10 tickets, while non-members can purchase up to 3 tickets.
Seat Availability Validation:
    -The system must validate if a seat has already been sold to another user and offer a nearby seat if necessary.
Seat Costs:
    -VIP boxes: £1000 per seat.
    -VIP seats: £500 per seat.
    -General seating: £90 per seat.
System Workflow:
    Login. -> Confirm membership status. -> Select seats. -> Make payment. -> Generate and issue tickets.
Remaining Seat Display:
    -The system should display the number of available seats after each purchase.
-----------------------------------------------------------------------------------------------------------------"""
import os
import random

#data
seats = 74310
vip_boxes = int(seats * 0.05)
vip_seats = int(seats * 0.15)

dicc_seats = {'1': range(1, vip_boxes), '2': range(vip_boxes+1, vip_seats),
              '3': range(vip_seats+1, seats)}

dicc_price = {'1': 1000, '2': 500, '3': 90}

selled_seats = list(random.sample(range(1, 74320), 1000))

menu_type_seat = """\
+---+---------------------------------+
| 1 | Boxes VIP (£1000 por asiento)   |
+---+---------------------------------+
| 2 | Asientos VIP (£500 por asiento) |
+---+---------------------------------+
| 3 | Asiento normal (£90 por asiento)|
+---+---------------------------------+\
"""

client_data = {'morenito19':{'password': 'abrete', 'seats':[]},
               'juan':{'password': '1234', 'seats':[]}}

def select_sit(user):
    while True:
        os.system('cls')
        print(menu_type_seat)
        ans = input('Que tipo de asiento quieres: ')

        if ans in ['1', '2', '3']:
            price = dicc_price[ans]
            os.system('cls')

            while True:
                seat = input('Numero de asiento que quieres adquirir (continuar): ')

                if int(seat) in dicc_seats[ans]:
                    if int(seat) not in selled_seats:
                        selled_seats.append(int(seat))
                        client_data[user]['seats'].append(int(seat))
                        print(client_data)


                else:
                    break






        else:
            os.system('cls')
            print('No entiendo tu respuesta.')
            input('Pulsa enter para continuar.')


user = 'juan'
select_sit(user)