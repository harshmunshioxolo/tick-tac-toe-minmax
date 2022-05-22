def terminal_visualisation(state: str) -> None:
    # split the state
    # a sample state would be of the form [N*9]

    # A super naive approach but works for now
    board = ""
    for i in range(9):
        if (i+1)%3 == 0:
            if state[i] == 'N':
                board += "  |\n"
            else:
                board += f" {state[i]}|\n"
        else:
            if state[i] == 'N':
                board += "  | "
            else:
                board += f" {state[i]}| "
    
    print(board)

terminal_visualisation("XNNXXNNN0")