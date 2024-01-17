"""3. Manchester United FC Player Management System:

As a developer for Manchester United FC, the executive management has tasked you with creating a
CRUD system for the current players, including the following information: Jersey number, position, age, height,
and other statistical data. Additionally, integrate the system from the previous level where it was possible to
compare two players and visualize their characteristics. You may find player information by searching on the internet.

Features:

Creates - Add new players to the system with their respective details.
Read - View the complete list of current players with their jersey number, position, age, height,
       and other statistical information.
Update - Modify player information as needed, such as position, age, or height.
Delete - Remove players from the system if they are no longer part of the team.
Compare Players - Utilize the comparison feature to analyze and contrast the characteristics of two players.
Visualize Characteristics - Display the statistical and physical attributes of each player for a comprehensive overview.
"""
import os

# data

dicc_player = {'number': None, 'name': None, 'position': None, 'age': None, 'height': None,
               'games_play': 0, 'goals': 0, 'pases':0, 'yellow': 0, 'red': 0, 'min': 0}
dicc_positions = {'gk': 'Portero', 'def': 'Denfensa', 'mid': 'Central', 'for': 'Delantero'}
dicc_keys = {'1': 'number', '2': 'name', '3': 'position', '4': 'age', '5': 'height', '6': 'games_play', '7': 'goals',
             '8': 'pases', '9': 'yellow', '10': 'red', '11': 'min'}
data_player = {
    '27': {'number': 27, 'name': 'Mary Earps', 'position': 'gk', 'age': 30, 'height': 171,
         'games_play': 18, 'goals': 0, 'pases': 21, 'yellow': 0, 'red': 0, 'min': 1620},
    '8': {'number': 8, 'name': 'Irene Guerrero Sanmartin', 'position': 'mid', 'age': 27, 'height': 168,
        'games_play': 2, 'goals': 0, 'pases': 1, 'yellow': 0, 'red': 0, 'min': 32},
    '9': {'number': 9, 'name': 'Melvine Malard', 'position': 'for', 'age': 23, 'height': 171,
        'games_play': 15, 'goals': 7, 'pases':2, 'yellow': 2, 'red': 0, 'min': 657}
}
menu_mod = """\
+----+---------------------------------+
| 1  | Número                          |
+----+---------------------------------+
| 2  | Nombre                          |
+----+---------------------------------+
| 3  | Posición                        |
+----+---------------------------------+
| 4  | Edad                            |
+----+---------------------------------+
| 5  | Altura                          |
+----+---------------------------------+
| 6  | Num. de juegos de la temporada  |
+----+---------------------------------+
| 7  | Num. de goles de la temporada   |
+----+---------------------------------+
| 8  | Num. de pases de la temporada   |
+----+---------------------------------+
| 9  | Num. de tarjetas amarillas      |
+----+---------------------------------+
| 10 | Num. de tarjetas rojas          |
+----+---------------------------------+
| 11 | Minútos jugados en la temporada |
+----+---------------------------------+\
"""
menu_gen = """\
+---+--------------------------------+
| 1 | Añadir un jugador              |
+---+--------------------------------+
| 2 | Visualizar todos los jugadores |
+---+--------------------------------+
| 3 | Modificar datos de jugador     |
+---+--------------------------------+
| 4 | Eliminar a un jugador          |
+---+--------------------------------+
| 5 | Comparar dos jugadores         |
+---+--------------------------------+
| 6 | Visualizar caracteristicas     |
+---+--------------------------------+
| S | Salir                          |
+---+--------------------------------+\
"""

# funtions

def create():
    new_player = dicc_player
    while True:
        os.system('cls')
        print(' ###### AÑADIR NUEVO MIEMBRO DEL EQUIPO ######')
        print('----------------------------------------------')
        num = input('Numero de camiseta: ')

        if num not in list(data_player.keys()):
            new_player['number'] = int(num)
            new_player['name'] = input('Nombre y apellidos: ')
            new_player['age'] = int(input('Edad: '))
            new_player['height'] = int(input('Altura: '))

            while True:
                os.system('cls')
                print('@@@@@ DATOS ESTADISTICOS Y DEPORTIVOS @@@@@')
                print('-------------------------------------------')
                for x in dicc_positions.items():
                    print(f'{x[0]} - {x[1]}')
                pos =input('Posición en la que juega: ')
                if pos in list(dicc_positions):
                    new_player['games_play'] = int(input('Partidos jugados esta temporada: '))
                    new_player['goals'] = int(input('Goles marcados esta temporada: '))
                    new_player['pases'] = int(input('Pases hechos esta temporada: '))
                    new_player['yellow'] = int(input('Tarjetas amarillas: '))
                    new_player['red'] = int(input('Tarjetas rojas: '))
                    new_player['min'] = int(input('Total de minútos jugados esta temporada: '))

                    while True:
                        os.system('cls')
                        print(f'+----------------------------------------+\n'
                              f'Numero: {new_player['number']}\n'
                              f'Nombre: {new_player['name']}\n'
                              f'Edad: {new_player['age']}\n'
                              f'Altura: {new_player['height']}\n'
                              f'Núm. de juegos: {new_player['games_play']}\n'
                              f'Núm. de goles: {new_player['pases']}\n'
                              f'Tarjetas amarrillas: {new_player['yellow']}\n'
                              f'Tarjetas rojas: {new_player['red']}\n'
                              f'Minutos jugados: {new_player['min']}\n'
                              f'+----------------------------------------+'
                              )
                        ans = input('Confirmar la incorporación (Si/No): ')
                        ans = ans.lower()
                        if ans == 'si' or ans == 's':
                            data_player[str(num)] = new_player
                            return

                        elif ans == 'no' or ans == 'n':
                           return

                        else:
                            os.system('cls')
                            print('No entiendo tu respuesta.')
                            input('Pulsa enter para continuar.')

                else:
                    os.system('cls')
                    print('No entiendo tu respuesta.')
                    input('Pulsa enter para continuar.')

        else:
            os.system('cls')
            print('Ese número ya esta en uso.')
            input('Pulsa enter para continuar.')
def view_player():
    os.system('cls')
    for new_player in list(data_player.values()):
        print(f'+----------------------------------------+\n'
              f'Numero: {new_player['number']}\n'
              f'Nombre: {new_player['name']}\n'
              f'Edad: {new_player['age']}\n'
              f'Altura: {new_player['height']}\n'
              f'Núm. de juegos: {new_player['games_play']}\n'
              f'Núm. de goles: {new_player['pases']}\n'
              f'Tarjetas amarrillas: {new_player['yellow']}\n'
              f'Tarjetas rojas: {new_player['red']}\n'
              f'Minutos jugados: {new_player['min']}')
def modify_player():

    while True:
        num_jer = input('Número de jugador: ')

        if num_jer in list(data_player.keys()):
            for x in data_player.items():
                if x[0] == num_jer:
                    player = x[1]
                    break

            while True:
                os.system('cls')
                print(menu_mod)
                ans = input('Que dato quieres modificar: ')

                if ans in list(dicc_keys.keys()):
                    os.system('cls')
                    print(f'El valor actual es: {player[dicc_keys[ans]]}\n'
                          f'--------------------------------------------')
                    new = input('Cual es el nuevo valor (salir): ')
                    new = new.lower()
                    if new == 'salir' or new == 's':
                        return
                    else:
                        player[dicc_keys[ans]] = new
                        data_player[num_jer] = player
                        return


                else:
                    os.system('cls')
                    print('No entiendo tu respuesta.')
                    input('Pulsa enter para continuar.')






        else:
            os.system('cls')
            print('No hay ningun jugador con ese numero.')
            input('Pulsa enter para continuar.')
            return
def delete_player():

    while True:
        os.system('cls')
        num = input('Número del jugador que quieres eliminar (salir): ')

        if num in list(data_player.keys()):
            player = data_player[num]
            conf = input(f'Seguro que quieres eliminar a {player['name']} de forma permanente (Si/No): ')
            conf = conf.lower()

            if conf == 'si' or conf == 's':
                del data_player[num]
                return
            elif conf == 'no' or conf == 'n':
                return
            else:
                os.system('cls')
                print('No entiendo tu respuesta.')
                input('Pulsa enter para continuar.')
        elif num == 'salir' or num == 's':
            return
        else:
            os.system('cls')
            print('No entiendo tu respuesta o no hay un jugador con ese número.')
            input('Pulsa enter para continuar.')
def compare_player():
    while True:
        os.system('cls')
        player1 = input('Núm. Jugador 1: ')
        player2 = input('Núm. Jugador 2: ')

        if player1 in list(data_player.keys()) and player2 in list(data_player.keys()):
            os.system('cls')
            new_player = data_player[player1]
            print(f'+----------------------------------------+\n'
                  f'Numero: {new_player['number']}\n'
                  f'Nombre: {new_player['name']}\n'
                  f'Edad: {new_player['age']}\n'
                  f'Altura: {new_player['height']}\n'
                  f'Núm. de juegos: {new_player['games_play']}\n'
                  f'Núm. de goles: {new_player['pases']}\n'
                  f'Tarjetas amarrillas: {new_player['yellow']}\n'
                  f'Tarjetas rojas: {new_player['red']}\n'
                  f'Minutos jugados: {new_player['min']}')
            new_player = data_player[player2]
            print(f'+----------------------------------------+\n'
                  f'Numero: {new_player['number']}\n'
                  f'Nombre: {new_player['name']}\n'
                  f'Edad: {new_player['age']}\n'
                  f'Altura: {new_player['height']}\n'
                  f'Núm. de juegos: {new_player['games_play']}\n'
                  f'Núm. de goles: {new_player['pases']}\n'
                  f'Tarjetas amarrillas: {new_player['yellow']}\n'
                  f'Tarjetas rojas: {new_player['red']}\n'
                  f'Minutos jugados: {new_player['min']}')

        else:
            os.system('cls')
            print('No entiendo tu respuesta.')
            input('Pulsa enter para continuar.')
def visualize():
    os.system('cls')
    player1 = input('Núm. Jugador: ')
    os.system('cls')
    new_player = data_player[player1]
    print(f'+----------------------------------------+\n'
          f'Numero: {new_player['number']}\n'
          f'Nombre: {new_player['name']}\n'
          f'Edad: {new_player['age']}\n'
          f'Altura: {new_player['height']}\n'
          f'Núm. de juegos: {new_player['games_play']}\n'
          f'Núm. de goles: {new_player['pases']}\n'
          f'Tarjetas amarrillas: {new_player['yellow']}\n'
          f'Tarjetas rojas: {new_player['red']}\n'
          f'Minutos jugados: {new_player['min']}')
    return

#code
while True:
    os.system('cls')
    print('# Manchester United FC Player Management System #')
    print(menu_gen)
    sel = input('Seleciona: ')
    sel = sel.lower()

    if sel == '1':
        create()
    elif sel == '2':
        view_player()
    elif sel == '3':
        modify_player()
    elif sel == '4':
        delete_player()
    elif sel == '5':
        compare_player()
    elif sel == '6':
        visualize()
    elif sel == 's':
        exit()
    else:
        os.system('cls')
        print('No entiendo tu respuesta.')
        input('Pulsa enter para continuar.')