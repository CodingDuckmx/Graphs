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
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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
print('$$$$$$$$$$$$$$$$$$')

# print(world.rooms[order_of_visits[1]].get_room_in_direction('n').id)


'''
'''
def find_traversal_path(order_of_visits,world):

    traversal_path = []
    # move_backwards = {'n':'s','w':'e','s':'n','e':'w'}

    # Iterate through the vertices in order to search for them in that order.

    # Set i to zero, to place us at the begining of the path.

    current_room = world.rooms[order_of_visits[0]]

    j = 1

    while j < len(order_of_visits):
 
        # print(current_room.id)
        
        searched_room = world.rooms[order_of_visits[j]]
        # print(searched_room.id)
        directions = current_room.get_exits()

        founded = False

        # print(directions)

        for direction in directions:

            # print(current_room.get_room_in_direction(direction))

            if current_room.get_room_in_direction(direction):

                if current_room.get_room_in_direction(direction).id == searched_room.id:

                    traversal_path.append(direction)
                    current_room = current_room.get_room_in_direction(direction)
                    founded = True
                    j += 1
        
        if not founded:

            temp_path = graph.dfs_recursive(current_room.id,searched_room.id,visited = [], path = [])

            # print(temp_path)

            if temp_path:

                k = 1

                while current_room.id != searched_room.id and k < len(temp_path):

                    temp_searched_room = world.rooms[temp_path[k]]
                    directions = current_room.get_exits()

                    for direction in directions:

                        # print(current_room.get_room_in_direction(direction))

                        if current_room.get_room_in_direction(direction):

                            if current_room.get_room_in_direction(direction).id == temp_searched_room.id:

                                traversal_path.append(direction)
                                current_room = current_room.get_room_in_direction(direction)

                    k += 1

            j += 1



  

    '''
    For each vertex, i'll look for the neighbors, if the next needed vertex is in the neighbors,
    go for it, if not, go back until you can see the next needed vertex in the neigbors.
    '''

    return traversal_path







###############################################################################################################

print('##########################################################')

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = find_traversal_path(order_of_visits,world)





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

