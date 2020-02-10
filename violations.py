import time

def violation(ARG): 
    if ARG:
        return 0
    else:
        if ARG > 0:
            if ARG == 1:
                return 1
            elif ARG == 2:
                return 2
            elif ARG == 3:
                return 3
            elif ARG == 4:
                return 4
            else:
                return 5
        else:
            if ARG == -1:
                return -1
            elif ARG == -2:
                return -2
            elif ARG == -3:
                return -3
            elif ARG == -4:
                return -4
            else:
                return -5
