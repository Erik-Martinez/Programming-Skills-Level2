"""The Big Six of the English Premier League is composed of six teams:
            Manchester United, Liverpool, Arsenal, Chelsea, Manchester City, and Tottenham Hotspur.
 Develop a system that generates between 0, 1, and 3 points randomly for each team.
 The winner of the Big Six will be the team with the highest accumulated points at the end.
 Each team will play 3 matches against every opponent.
 After the matches, the system will display on-screen the team standings from highest to lowest points.
 -----------------------------------------------------------------------------------------------------"""
import os
import random as rd

#data

teams = {'Manchester United': 0, 'Liverpool': 0, 'Arsenal': 0, 'Chelsea':0,
         'Manchester City': 0, 'Totthenham Hotspur': 0}
teams_names = ['Manchester United', 'Liverpool', 'Arsenal', 'Chelsea', 'Manchester City', 'Totthenham Hotspur']

def matches_teams(team1, team2):
    goals_team1 = rd.randrange(0,3)
    goals_team2 = rd.randrange(0, 3)

    if team1 == 'Manchester United' or team2 == 'Manchester UniteGraphvizd':
        goals_team1 = rd.randrange(1, 3)

    if goals_team1 > goals_team2:
        teams[team1] = teams[team1] + 3
    elif goals_team1 < goals_team2:
        teams[team2] = teams[team2] + 3
    elif goals_team1 == goals_team2:
        teams[team1] = teams[team1] + 1
        teams[team2] = teams[team2] + 1

def save_match(team1, team2, games):
    t = f'{team1}-{team2}'
    games.append(t)
    return games

def combinaciones():
    games = []
    con = 1
    for team1 in teams_names:
        con2 = 1
        for team2 in teams_names:
            if team1 != team2:
                if con == 1 and con2 >=1:
                    games = save_match(team1, team2, games)
                elif con == 2 and con2 >= 2:
                    games = save_match(team1, team2, games)
                elif con == 3 and con2 >= 3:
                    games = save_match(team1, team2, games)
                elif con == 4 and con2 >= 4:
                    games = save_match(team1, team2, games)
                elif con == 5 and con2 >= 5:
                    games = save_match(team1, team2, games)

                con2 += 1
        con += 1
    return games




#code
games = combinaciones()
t = 1
while t <= 3:
    t += 1
    for game in games:
        game = game.split(sep='-')
        team1 = game[0]
        team2 = game[1]
        matches_teams(team1, team2)

sorted_teams = dict(sorted(teams.items(), key=lambda item:item[1], reverse=True))
print('Clasificación de la ultima Fantasy Big Six')
print('------------------------------------------')
num = 0
for x in sorted_teams.items():
    num += 1
    print(f'{num}. {x[0]} - {x[1]} puntos.')











