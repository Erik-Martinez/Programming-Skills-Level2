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

dicc_seats = {'1': [str(x) for x in range(1, vip_boxes)], '2': [str(x) for x in range(vip_boxes+1, vip_seats)],
              '3': [str(x) for x in range(vip_seats+1, seats)]}

dicc_price = {'1': 1000, '2': 500, '3': 90}

selled_seats = list(random.sample(range(1, 74320), 1000))
selled_seats = [str(x) for x in selled_seats]

menu_type_seat = """\
+---+---------------------------------+
| 1 | Boxes VIP (£1000 por asiento)   |
+---+---------------------------------+
| 2 | Asientos VIP (£500 por asiento) |
+---+---------------------------------+
| 3 | Asiento normal (£90 por asiento)|
+---+---------------------------------+\
"""
dicc_type_seat = {'1': 'Box VIP', '2': 'Asientos VIP', '3': 'Asiento normal'}
dicc_num_seat = {'1': f'1-{vip_boxes}', '2': f'{vip_boxes+1}-{vip_seats}', '3': f'{vip_seats+1}-{seats}'}

client_data = {'morenito19':{'password': 'abrete', 'membership': True, 'seats':[]},
               'juan':{'password': '1234', 'membership': False, 'seats':[]}}

#var
info_tickets = []
total_price = 0

# funtions
def login():
    attemps = 0
    while attemps < 3:
        os.system('cls')
        print("Modo test: juan - 1234")
        print('-------------------------')
        user = input("Nombre de usuario: ")
        if user in client_data.keys():
            password = input("Contraseña: ")
            if client_data[user]['password'] == password:
                os.system("cls")
                print('Claves aceptadas.')
                input('Pulsa enter para continuar.')
                return user
            else:
                os.system("cls")
                attemps += 1
                print(f"La contraseña no es correcta.\n"
                      f"Te quedan {3 - attemps} intentos.")
                input('Pulsa enter para continuar.')
        else:
            os.system("cls")
            attemps += 1
            print(f"{user} no esta registrado en nuestro sistema.\n"
                  f"Te quedan {3-attemps} intentos.")
            input('Pulsa enter para continuar.')

    print('Has superado el numero de intentos maximos.')
    exit()
def membership(user):
    if client_data[user]['membership'] == True:
        os.system('cls')
        print('Bienvenido miembro del club. Recuerda que tienes un 15% de descuento\n'
              'en tus comprar y puedes comprar hasta 10 asientos.')
    else:
        while True:
            os.system('cls')
            print('Bienvenido. Aparece en nuestra base de datos que no eres miembro del club.\n')
            ans = input('Confirmas esta infromación (Si/No): ')
            ans = ans.lower()

            if ans == 'si' or ans == 's':
                print('Entendido. Ser miembro da recompensas exclusivas como descuentos y la \n'
                      'posibilidad de comprar más asientos. Puedes hacerte miembro en el \n'
                      'estadio.')
                input('Pulsa enter para continuar.')
                return
            elif ans == 'no' or ans == 'n':
                print('Entendido, ya hemos cambiado la información. Se te aplicaran los\n'
                      'descuentos y la posibilidad de comprar hasta 10 asientos.')
                client_data[user]['membership'] = True
                input('Pulsa enter para continuar.')
                return
            else:
                os.system('cls')
                print('No entiendo tu respuesta.')
                input('Pulsa enter para continuar.')
def select_sit(user, info_tickets, total_price):
    while True:
        os.system('cls')
        print(menu_type_seat)
        ans = input('Que tipo de asiento quieres: ')

        if ans in ['1', '2', '3']:
            price = dicc_price[ans]
            total_tickets = 0
            os.system('cls')
            seat = None

            while True:
                if seat != 'continuar':
                    os.system('cls')
                    seat = input(f'Numero de {dicc_type_seat[ans]} que quieres adquirir [entre {dicc_num_seat[ans]}] (continuar): ')

                if seat in dicc_seats[ans]:
                    if seat not in selled_seats:
                        if client_data[user]['membership'] == True:
                            num_tickets = len(client_data[user]['seats'])
                            if num_tickets < 10:
                                selled_seats.append(int(seat))
                                client_data[user]['seats'].append(int(seat))
                                selled_seats.append(int(seat))
                                info_tickets.append(f'Número: {seat} {dicc_type_seat[ans]}')
                                total_tickets += 1
                            else:
                                os.system('cls')
                                print('Has alcanzado el número maximo de tickets.')
                                input('Pulsa enter para continuar.')
                                max_tickets = True
                                seat = 'continuar'
                        else:
                            num_tickets = len(client_data[user]['seats'])
                            if num_tickets < 3:
                                selled_seats.append(int(seat))
                                client_data[user]['seats'].append(int(seat))
                                selled_seats.append(int(seat))
                                info_tickets.append(f'Número: {seat} {dicc_type_seat[ans]}')
                                total_tickets += 1
                            else:
                                os.system('cls')
                                print('Has alcanzado el número maximo de tickets.')
                                input('Pulsa enter para continuar.')
                                max_tickets = True
                                seat = 'continuar'
                    else:
                        os.system('cls')
                        print('Ese asiento ya esta reservado.')
                        input('Pulsa enter para continuar.')

                elif seat.lower() == 'continuar' or seat.lower() == 'c' and max_tickets == False:
                    while True:
                        os.system('cls')
                        ans = input('Quieres comprar más asientos de otro tipo (Si/No): ')
                        total_price += price * total_tickets
                        ans = ans.lower()

                        if ans == 'si' or ans == 's':
                            total_price, info_tickets = select_sit(user, info_tickets, total_price)
                            return total_price, info_tickets
                        elif ans == 'no' or ans == 'n':
                            return total_price, info_tickets
                        else:
                            os.system('cls')
                            print('No entiendo tu respuesta.')
                            input('Pulsa enter para continuar.')
                elif seat.lower() == 'continuar' or seat.lower() == 'c' and max_tickets == True:
                    total_price += price * num_tickets
                    ans = ans.lower()
                    return total_price, info_tickets
                else:
                    os.system('cls')
                    print('Ese asiento no esta disponible.')
                    input('Pulsa enter para continuar.')
        else:
            os.system('cls')
            print('No entiendo tu respuesta.')
            input('Pulsa enter para continuar.')
def summarize_tickets(user, info_tickets, total_price):
    while True:
        os.system('cls')
        if client_data[user]['membership'] == True:
            total_price = total_price - (total_price*0.15)

        print('####### RESUMEN PEDIDO #######')
        print('------------------------------')
        for x in info_tickets:
            print(x)
        print('------------------------------')
        print(f'TOTAL: £{total_price}')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        ans = input('Confirmar compra (Si/No): ')
        ans = ans.lower()

        if ans == 'si' or ans == 's':
            os.system('cls')
            print('Pedido realizado. Disfruta de tus asientos!')
            input('Pulsa enter para continuar.')
            exit()
        elif ans == 'no' or ans == 'n':
            os.system('cls')
            print('Pedido cancelado. Esperamos verte proto!')
            input('Pulsa enter para continuar.')
            exit()
        else:
            os.system('cls')
            print('No entiendo tu respuesta.')
            input('Pulsa enter para continuar.')


#code
user = login()
membership(user)
total_price, info_tickets = select_sit(user, info_tickets, total_price)
summarize_tickets(user, info_tickets, total_price)

