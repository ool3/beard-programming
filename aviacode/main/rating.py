def count(p_time, e_time, p_mem, e_mem):
    if p_mem is None:
        p_mem = 99

    reting = 1

    reting_tablle = {1: "E", 2: "D", 3: "C", 4: "B", 5: "A"}

    if float(p_time) <= e_time:
        reting += 2
    elif float(p_time) <= (e_time * 0.75):
        reting += 1

    if float(p_mem) >= e_mem:
        reting += 2
    elif float(p_mem) >= (e_mem * 0.75):
        reting += 1

    return reting_tablle[reting]
