"""
give a list of team, where team[i] is the # of people in the team
and a list of rooms, where room[i] is the capacity of room
if one team is not in the same room, the whole team will be unhappy
return the min number of unhappy people
"""

teams = [3, 3, 5, 1, 1, 2, 4]
rooms = [6, 7, 2, 1]
def minUnhappy(teams, rooms):

    out = sum(teams)
    teams.sort(reverse = True)

    def recursion(rooms, team_i, unhappy):
        nonlocal out, teams
        if unhappy >= out:
            return
        if team_i == len(teams):
            out = min(unhappy, out)
            return
        for i in range(len(rooms)):
            if rooms[i] >= teams[team_i]:
                rooms[i] -= teams[team_i]
                recursion(rooms, team_i + 1, unhappy)
                rooms[i] += teams[team_i]
        recursion(rooms, team_i + 1, unhappy + teams[team_i])
    recursion(rooms, 0, 0)

    return out
print(minUnhappy(teams, rooms))
