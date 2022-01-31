from typing import List

from comunes.model.input import Input


class Transicion:
    state: int
    inputs: List[Input]

    def __init__(self, state: int, inputs: List[Input]) -> None:
        self.state = state
        self.inputs = inputs