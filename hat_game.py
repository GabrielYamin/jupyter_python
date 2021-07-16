import numpy as np
# EX4
def hat_game(N):
    """conducts a Hat game as explained in the jupyter document"""
    # False -> on lap, True -> on head
    people = np.full(N, False)
    modulo = 1
    for i in range(N):
        for j in range(N):
            if (j+1) % modulo == 0:
                people[j] = not people[j]
        modulo += 1
    return (np.array(np.nonzero(people)[0])+1).tolist()
