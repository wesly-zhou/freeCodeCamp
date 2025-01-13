# This program employs the core concepts of a Markov Chain to make a prediction.
# The last five moves of the opponent are used to predict the next move of the
# opponent, although transition probabilities are not explicitly calculated.

def player(prev_play, opponent_history=[], play_order={}):
    """
    A player function returning the next move to play.
    An argument describing the last play of the opponent is given.
    """
    # Append a the previous play to the opponent's history
    # An empty string is given at the start of the game
    opponent_history.append(prev_play)

    # Predict a random play until enough plays have been made for a prediction
    prediction = "S"

    if len(opponent_history) > 4:
        last_five = "".join(opponent_history[-5:])
        # Update the frequency of the sequence of the opponent's last five moves
        play_order[last_five] = play_order.get(last_five, 0) + 1

        # Define a list with the three sequences the opponent could create with
        # each of the three possible plays
        potential_plays = ["".join(opponent_history[-4:] + [move]) for move in "RPS"]

        # Update a dictionary with each of the potential sequences and their frequencies
        sub_order = {
            seq: play_order[seq] for seq in potential_plays if seq in play_order
        }

        # Update the prediction to be the move that generates the most likely sequence
        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]