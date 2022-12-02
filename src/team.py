from __future__ import annotations

import json
from typing import List, Optional

from src.data import Data


class Team:
    def __init__(
        self,
        players: List[str],
        coach: str
    ):
        self.players = players
        self.coach = coach

    def is_valid(self, data: Data) -> bool:
        return False

    def write(self, filename: str) -> None:
        json.dump(
            {
                "players": self.players,
                "coach": self.coach
            },
            open(filename, 'w')
        )

    @staticmethod
    def read(filename: str) -> Team:
        source = json.load(open(filename, 'r'))
        players = source["players"]
        coach = source["coach"]
        return Team(players=players, coach=coach)

    def __str__(self) -> str:
        spacing = "\t"
        return (
            "players:"
            + "\n".join([spacing + p for p in self.players])
            + f"coach: {self.coach}"
        )

