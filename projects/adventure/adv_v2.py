from graph import Graph
from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork_modified.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

###############################################################################################################

graph = Graph()

for room in world.rooms:

    graph.add_vertex(room)

for room in world.rooms:
 
    if world.rooms[room].n_to:

        graph.add_edge(room,world.rooms[room].n_to.id)

    if world.rooms[room].w_to:

        graph.add_edge(room,world.rooms[room].w_to.id)

    if world.rooms[room].s_to:

        graph.add_edge(room,world.rooms[room].s_to.id)

    if world.rooms[room].e_to:

        graph.add_edge(room,world.rooms[room].e_to.id)

order_of_visits = graph.dft_modified(0)

print('$$$$$$$$$$$$$$$$$$')
print(order_of_visits)
print(len(order_of_visits))
print('$$$$$$$$$$$$$$$$$$')

# print(room_graph)

# traversal_path = []

# for i in range(len(order_of_visits)-1):

#     for key, value in room_graph[order_of_visits[i]][1].items():

#         if value == order_of_visits[i+1]:

#             traversal_path.append(key)

# print(traversal_path)


###############################################################################################################

print('##########################################################')

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# traversal_path = []



'''

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


# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
'''