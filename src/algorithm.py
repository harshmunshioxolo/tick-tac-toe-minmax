from visualization import terminal_visualisation

class State:
    """Class to initialize and maintain the state of the board
    """
    def __init__(self, start: str) -> None:
        self.state = 'N'*9
        self.start = start
        self.score = 0
    
    def check_terminating_condition(self):
        if 'N' in self.state:
            return False
        else:
            return True
    
    def check_winning_positions(self, player: str):
        if player == "maxi":
            score = 10
        else:
            score = -10
        # check winning positions in case it is achieved before the state is complete
        # 1. check horizonal positions
        # sample = 'N N N N N N N N N'
        print(self.state)
        if (self.state[0] == self.state[1] and self.state[1] == self.state[2] and self.state[0] != 'N' and self.state[2] != 'N'):
            return score
        elif (self.state[3] == self.state[4] and self.state[4] == self.state[5] and self.state[3] != 'N' and self.state[5] != 'N'):
            return score
        elif (self.state[6] == self.state[7] and self.state[7] == self.state[8] and self.state[6] != 'N' and self.state[8] != 'N'):
            return score
        
        # 2. check vertical positions
        if (self.state[0] == self.state[3] and self.state[3] == self.state[6] and self.state[0] != 'N' and self.state[3] != 'N'):
            return score
        elif (self.state[1] == self.state[4] and self.state[4] == self.state[7] and self.state[1] != 'N' and self.state[7] != 'N'):
            return score 
        elif (self.state[2] == self.state[5] and self.state[5] == self.state[8] and self.state[2] != 'N' and self.state[8] != 'N'):
            return score
        
        # 3. Check diagonals
        if (self.state[0] == self.state[4] and self.state[4] == self.state[8] and self.state[0] != 'N' and self.state[8] != 'N'):
            return 10
        elif (self.state[2] == self.state[4] and self.state[4] == self.state[6] and self.state[2] != 'N' and self.state[6] != 'N'):
            return 10
        
        # 4. if not anything
        return 0


    
    def find_next_children(self, player: str):
        s = list(self.state)
        children = []
        for i in range(9):
            if s[i] == 'N':
                if player == "mini":
                    s[i] = "O"
                elif player == "maxi":
                    s[i] = "X"
                children.append("".join(s))
                s[i] = "N"
        
        return children
    
    def next_best_move(self, player: str):
        # This is the minimax algorithm
        if player == "maxi":
            # maximize the score
            pass
        
        else:
            # check if board is either full or someone has won
            score = []
            tree = []
            close = []
            while(not self.check_terminating_condition()):
                tree = self.find_next_children("mini")
                for child in tree:
                    # check if the children have hit the winning condition
                    self.state = child
                    # expand the child if winning position is not true
                    if (not self.check_winning_positions("mini")):
                        children = self.find_next_children("mini")
                        for c in children:
                            tree.append(c)
                    else:
                        # this means there is a terminal condition
                        return close[-1]
    

if __name__=="__main__":
    x = input(f"Welcome to tic-tac-toe. Select a player to start, H for human or C for computer: ")
    # if str(x) != "H" or str(x) != "C":
    #     raise TypeError(f"Please select appropriate player")

    # Initialize the board
    board = State(x)
    if x == "H":
        x = input(f"Input your move as [x+y] coordinate: ")
        # [i,j] ==> The index for the string will be i+j
        s = list(board.state)
        s[int(x)] = "X"
        board.state = "".join(s)

        # compute the next best move
        while (not board.check_terminating_condition()):
            next_move = board.next_best_move("mini")
            terminal_visualisation(next_move)

            x = input(f"Your next move?: ")
            # [i,j] ==> The index for the string will be i+j
            s = list(board.state)
            s[int(x)] = "X"
            board.state = "".join(s)