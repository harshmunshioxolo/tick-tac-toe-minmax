from visualization import terminal_visualisation

class State:
    """Class to initialize and maintain the state of the board
    """
    def __init__(self, start: str) -> None:
        self.state = 'N'*9
        self.start = start
    
    def check_terminating_condition(self):
        raise NotImplementedError()
    
    def check_winning_positions():
        raise NotImplementedError()
    
    def find_next_child(self):
        raise NotImplementedError()
    
    def next_best_move(self):
        # This is the minimax algorithm 
        raise NotImplementedError()
    
    

if __name__=="__main__":
    x = input(f"Welcome to tic-tac-toe. Select a player to start, H for human or C for computer: ")
    if str(x) != "H" or str(x) != "C":
        raise TypeError(f"Please select appropriate player")

    # Initialize the board
    board = State(x)
    terminal_visualisation(board.state)
