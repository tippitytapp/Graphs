from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player("Name",world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# player's graph of rooms and their directions
graph = dict()
traversal_path = []
reverse_path = []
visited_rooms = set()


def populate_graph_with_exits(room):
    ''' Populate graph with exits set to ? '''
    graph[room.id] = dict()
    exits = room.get_exits()
    for exit in exits:
        graph[room.id][exit] = '?'


def get_opposite(cardinal_direction):
    ''' Returns the opposite cardinal direction '''
    opposite = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
    return opposite.get(cardinal_direction)


def bfs(room):
    ''' Moves player over reverse_path. '''
    for move in reverse_path[::-1]:
        player.travel(move)
        traversal_path.append(move)
        reverse_path.pop(-1)
        if '?' in graph[player.current_room.id].values():
            # print(f'Graph at end of BFS. {graph}')
            return


def dfs(room, cardinal_directions):
    ''' Builds the graph and adds to the traversal and reverse paths '''
    previous_room_id = player.current_room.id
    cardinal_direction = cardinal_directions.pop(0)
    player.travel(cardinal_direction)
    in_room_id = player.current_room.id
    in_room = player.current_room
    traversal_path.append(cardinal_direction)
    opposite = get_opposite(cardinal_direction)
    reverse_path.append(opposite)
    if in_room_id not in graph:
        populate_graph_with_exits(in_room)
        graph[previous_room_id][cardinal_direction] = in_room_id
        graph[in_room_id][opposite] = previous_room_id
    else:
        graph[previous_room_id][cardinal_direction] = in_room_id


while len(graph) < len(room_graph):
    in_room = player.current_room
    if in_room.id not in graph:
        populate_graph_with_exits(in_room)
    unexplored_exits = []
    for cardinal_direction, room in graph[in_room.id].items():
        if room == '?':
            unexplored_exits.append(cardinal_direction)
    if len(unexplored_exits) > 0:
        dfs(in_room, unexplored_exits)
    else:
        if len(reverse_path) > 0:
            bfs(in_room)
        else:
            exits = in_room.get_exits()
            choice = random.choice(exits)
            player.travel(choice)



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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
