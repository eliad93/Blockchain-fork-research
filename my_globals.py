global_forks_count = 0


def reset_globals():
    global global_forks_count
    global_forks_count = 0


def inc_forks_count():
    global global_forks_count
    global_forks_count += 1


def get_global_forks_count():
    return global_forks_count
