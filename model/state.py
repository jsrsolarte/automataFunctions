class State:
    name: str
    acceptance: bool

    def __init__(self, name: int, acceptance: bool) -> None:
        self.name = name
        self.acceptance = acceptance