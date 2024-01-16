""" The lottery system produces results consisting of 4 digits + 1 letter, e.g., 0345F.
    Develop a lottery ticket purchase system with the following features:
Users can choose from the following tickets:
...
-Users can buy a minimum of 1 and a maximum of 2 tickets.
-Payment is accepted in cash, and each ticket costs 1 USD.
-After choosing tickets and quantity, the system prompts the user to pay in cash or by bank card.
-This system only accepts 1 USD and 5 USD bills. The user must choose the bill to use for payment,
    and the system should return the change if applicable.
-After payment, the ticket is issued.
-The user returns to the main menu to play the lottery.
-The lottery system generates 1 random ticket code.
 -----------------------------------------------------------------------------------------------------"""
import random as rd
import os
#data
dicc_alpha = {}
letras = [chr(i) for i in range(ord('A'), ord('Z')+1)]
for i, letra in enumerate(letras):
    dicc_alpha[i+1] = letra

tickes_user = {'ticket1': None, 'ticket2': None}

dicc_tickets = {1: '5678B', 2: '9876C', 3: '2345D', 4: '6789E', 5: '3456F', 6: '8765G',
                7: '4321H', 8: '7890J', 9: '5432K', 10: '2109L', 11: '8765M', 12: '1357N',
                13: '2468P', 14: '6543Q', 15: '7891R', 16: '3579S', 17: '9821T', 18: '4682U',
                19: '5763V', 20: '1234A'}

menu_tickets = """\
+----+-------+----+-------+
| 1  | 5678B | 11 | 8765M |
+----+-------+----+-------+
| 2  | 9876C | 12 | 1357N |
+----+-------+----+-------+
| 3  | 2345D | 13 | 2468P |
+----+-------+----+-------+
| 4  | 6789E | 14 | 6543Q |
+----+-------+----+-------+
| 5  | 3456F | 15 | 7891R |
+----+-------+----+-------+
| 6  | 8765G | 16 | 3579S |
+----+-------+----+-------+
| 7  | 4321H | 17 | 9821T |
+----+-------+----+-------+
| 8  | 7890J | 18 | 4682U |
+----+-------+----+-------+
| 9  | 5432K | 19 | 5763V |
+----+-------+----+-------+
| 10 | 2109L | 20 | 1234A |
+----+-------+----+-------+\
"""

# funtions

def win_number():
    num ='{:04d}'.format(rd.randint(0,9999))
    num_letter =  dicc_alpha[rd.randint(1,26)]
    num_win = num + num_letter
    return num_win

def buy_ticket():
    while True:
        if tickes_user['ticket1'] == None or tickes_user['ticket2'] == None:
            os.system('cls')
            print(menu_tickets)
            ticket = input('Cual de los tickets quieres comprar: ')
            if ticket in [str(x) for x in range(1, 21)]:
                if tickes_user['ticket1'] == None:
                    tickes_user['ticket1'] = dicc_tickets[int(ticket)]
                else:
                    tickes_user['ticket2'] = dicc_tickets[int(ticket)]
            else:
                os.system('cls')
                print('No te he entendido.')
                input('Pulsa enter para continuar')
                continue
        else:
            os.system('cls')
            print('Ya tienes el número maximo de tickets que es posible comprar.')
            input('Pulsa enter para continuar.')

        os.system('cls')
        more = input('Te gustaria comprar otro ticket? (Si/NO)')
        more = more.lower()

        if more == 'no' or more == 'n':
            break

    while True:

        os.system('cls')
        print('Perfecto. Nuestro sistema solo acepta pagos de 1 USD (1) o de 5 USD (2).')
        money = input('Con que te gustaria pagar: ')

        if money in ['1', '2']:
            if money == '1' and tickes_user['ticket2'] == None:
                change = 0
                return change
            elif money == '1' and tickes_user['ticket2'] != None:
                os.system('cls')
                print('El dinero no es suficiente.')
                input('Pulsa enter para continuar')
            elif money == '2' and tickes_user['ticket2'] == None:
                change = 4
                return change
            elif money == '2' and tickes_user['ticket2'] != None:
                change = 4
                return change
        else:
            os.system('cls')
            print('No te he entendido.')
            input('Pulsa enter para continuar')


def cheek_winner(num_win):
    os.system('cls')
    print(f'El ticket premiado es el {num_win}')
    if num_win in tickes_user.items():
        print('Enhorabuena uno de tus tickets ha sido premiado :)')
    else:
        print('Ninguno de tus tickets ha sido premiado :(')

change = buy_ticket()
os.system('cls')
print(f'La vuelta de tu compra es de {change} USD.')
input('Pulsa enter para continuar')
num_win = win_number()
cheek_winner(num_win)




