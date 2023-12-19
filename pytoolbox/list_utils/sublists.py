def create_sublists(input_list, sublist_size):
    num_sublists = len(input_list) // sublist_size

    if len(input_list) % sublist_size != 0:
        num_sublists += 1

    sublists = [[] for _ in range(num_sublists)]

    for i, element in enumerate(input_list):
        sublists[i % num_sublists].append(element)

    return sublists
