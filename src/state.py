class State:
    def __init__(self, parent: str, value: str) -> None:
        """A data structure to keep a track of parent node and children
        The first node will have no parent because it is the parent itself.

        Args:
            parent (str): In our case a string that represents the board state
        """
        self.parent = parent
        self.value = value
        self.children = None