import os

from src.team import Team
import datetime


def test_team_creation():
    players = ['gianni', 'pinotto']
    coach = 'mario vignati'

    team = Team(players=players, coach=coach)
    assert team.players == players and team.coach == coach


def test_team_read():
    team = Team.read("C:\\Users\\IT013960\\Projects\\fantasy_basket\\tests\\dummy_team.json")
    assert team.players == [
        "jordan micheal",
        "james lebron",
        "bird larry",
        "curry steph"
    ]
    assert team.coach == "messina ettore"


def test_team_write():
    filename = str(datetime.datetime.now().timestamp()).replace('.', '') + '.json'
    players = ['gianni', 'pinotto']
    coach = 'mario vignati'
    Team(players=players, coach=coach).write(filename)
    team = Team.read(filename)
    os.remove(filename)
    assert team.players == players and team.coach == coach
