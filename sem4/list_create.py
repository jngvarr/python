def create_intlist(n):
    import random
    n_to_n_list = list()
    for i in range(n):
        n_to_n_list.append(random.randint(-n, n))
    return n_to_n_list

def create_doublelist(n):
    import random
    n_to_n_list = list()
    for i in range(n):
        n_to_n_list.append(round(random.uniform(0, n),2))
    return n_to_n_list
