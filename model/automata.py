import json
from typing import List

from model.state import State
from model.transicion import Transicion


class Automata:
    type: int
    states: List[State]
    inputs: List[str]
    transicions: List[Transicion]

    def __init__(self, type: int, states: List[State], inputs: List[str], transicions: List[Transicion]) -> None:
        self.type = type
        self.states = states
        self.inputs = inputs
        self.transicions = transicions

    def to_JSON(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    