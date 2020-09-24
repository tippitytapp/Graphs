from utils import Queue, Graph


def earliest_ancestor(ancestors, starting_node):
    # init a variable to hold whether or not the node has an ancestor
    has_ancestor = False
    # loop through the ancestor pairs
    for ancestor in ancestors:
        # if the second ancestor of the pair is equal to the starting node
        if ancestor[1] == starting_node:
            # set has ancestor to true
            has_ancestor = True
    # if there is no ancestor
    if has_ancestor is False:
        # return -1 
        return -1
    # initialize an empty queue for the BFS
    queue = Queue()
    # enqueue the starting node
    queue.enqueue([starting_node])
    # initiate an array to hold values with no lineage
    nolineage = []
    # while you have a queue
    while queue.size() > 0:
        # set path equal to the node popped off the queue
        path = queue.dequeue()
        # the vertex you wil search is the last in the path list
        vertex = path[-1]
        # initialize a variable to hold whether or not you found new ancestors
        found_new_ancestor = False
        # loop through the  ancestors
        for ancestor in ancestors:
            # if the ancestor is the vertex
            if ancestor[1] == vertex:
                # change the face FNA to true
                found_new_ancestor = True
                # create a copy of the existing path
                new_path = list(path)
                # add the 1st ancestor to the path
                new_path.append(ancestor[0])
                # add the new path to the queue
                queue.enqueue(new_path)
        # if you found no new ancestors
        if found_new_ancestor == False:
            # add that path to the storage for no lineage
            nolineage.append(path)
            # then continue
            continue
    # initialize length at 0
    length = 0
    # initialize a visited storage
    visited = []
    # loop through the storage of no ancestors found
    for vertex in nolineage:
        # if the length of the vertex/path is larger than the length
        if len(vertex) > length:
            # visited is an empy array
            visited = []
            # set length to the length of the vertex/path
            length = len(vertex)
            # add the last node in the vertex/path to the visited array
            visited.append(vertex[-1])
            # then continue
            continue
        # if the length of the vertex/path is the same as the length
        elif len(vertex) == length:
            # add the last element of the vertex/path to the visited array
            visited.append(vertex[-1])
    # earliest ancestor is the the visited last
    earliest_ancestor = min(visited)
    # return the earliest ancestor
    return earliest_ancestor



