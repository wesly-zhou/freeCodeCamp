# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 2:
        guess = opponent_history[-2]

    return guess
