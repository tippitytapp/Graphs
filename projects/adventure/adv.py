from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
anti_trav = {'n' : 's', 's' : 'n', 'e' : 'w', 'w' : 'e' }
anti_trav_path = []
maze = dict()
# im assuming this should be visted rooms because thats what the test says?
visited_rooms = set()
unknown_paths = list()
# use the room method of get exits to build the current room exits
def get_room_exits(room):
    # this makes each room in the maze into a dictionary to hold directions
    maze[room.id] = {}
    # this calls the get_exits method from the rooms class
    exits = room.get_exits()
    # for each direction in the exits, pre-populate with a '?'
    for direction in exits:
        maze[room.id][direction] ='?'
    # return maze
    return maze

# print(get_room_exits(player.current_room))

while len(maze) < len(room_graph):
    cur_room = player.current_room
    if cur_room not in maze:
        get_room_exits(cur_room)
        # print(get_room_exits(cur_room))
    for direction, destination in maze[cur_room.id].items():
        if destination == '?':
            unknown_paths.append(direction)
            # print('uknown', unknown_paths)
    if len(unknown_paths) > 0:
        prev_room = player.current_room.id
        new_dir = unknown_paths.pop(0)
        player.travel(new_dir)
        new_room = player.current_room
        traversal_path.append(new_dir)
        pathback = anti_trav.get(new_dir)
        anti_trav_path.append(pathback)
        if new_room.id not in maze:
            get_room_exits(new_room)
            maze[prev_room][new_dir] = new_room.id
            maze[new_room.id][pathback] = prev_room
        else:
            maze[prev_room][new_dir] = new_room.id
    elif len(anti_trav_path) > 0:
        for untravdir in anti_trav_path[::-1]:
            player.travel(untravdir)
            anti_trav_path.pop(-1)
            



# TRAVERSAL TEST

visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
'''
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
        '''