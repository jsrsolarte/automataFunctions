import json
from typing import List

from comunes.model.step import Step


class RecognizeRow:
    accepted: bool
    steps: List[Step]

    def __init__(self, accepted: bool, steps: List[Step]) -> None:
        self.accepted = accepted
        self.steps = steps

    def to_JSON(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

