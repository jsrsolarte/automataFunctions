class Step:
    oldState: str
    newState: str
    input: str

    def __init__(self, oldState: str, newState: str, input: str) -> None:
        self.oldState = oldState
        self.newState = newState
        self.input = input