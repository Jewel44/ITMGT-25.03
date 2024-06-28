'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    from_member_dict = social_graph[from_member]["following"]
    to_member_dict = social_graph[to_member]["following"]

    if to_member in from_member_dict and from_member in to_member_dict:
        return "friends"
    elif from_member in to_member_dict: 
        return "followed by"
    elif to_member in from_member_dict: 
        return "follower"      
    else:
        return "no relationship"

def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    winner = False
    
    # horizontal line
    for horizontal in range(len(board)):
        if board[horizontal] == list(("X" * len(board))):
            winner = True
            return "X" 
        elif board[horizontal] == list(("O" * len(board))):
            winner = True
            return "O"
        else:
            continue

    # diagonal line
    if winner == False:
        if len(set(board[i][i] for i in range(len(board)))) == 1:
            winner = True
            return board[0][0]
        elif len(set(board[i][len(board)-i-1] for i in range(len(board)))) == 1:
            winner = True
            return board[0][len(board) - 1]

    # vertical line
    if winner == False:
        ctr = 0
        while winner == False:
            if len(set(board[i][ctr] for i in range(len(board)))) == 1 and set(board[i][ctr] for i in range(len(board))) != {""}:
                winner = True
                return board[0][ctr]
                break
            if winner == False:
                ctr += 1
            if ctr == len(board):
                break
                       
    # no winner
    if winner == False:
        return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    time_ctr = 0
    keys_list = list(route_map.keys())
    end = False

    while end == False:
        for i in range(len(keys_list)):
            keys_list_items = keys_list[0:len(route_map)][i]
            
            if keys_list_items[0] == first_stop:
                if keys_list_items[1] == second_stop:
                    time_ctr += route_map[keys_list_items]["travel_time_mins"]
                    end = True
                else: # if above code is still false
                    first_stop = keys_list_items[1]
                    time_ctr += route_map[keys_list_items]["travel_time_mins"]
        if end == True:
            break
        
    return time_ctr