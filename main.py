from src import Index


origin = (-6.8096036,39.2854829)
destination = (-6.867255,39.310245)

single_target = (-6.7870493, 39.2044721)  # Ubungo Maji, Dar Es Salaam, Tanzania
point_target = (-6.82186645, 39.301757704855774) # Ferry Terminal, Dar Es Salaam, Tanzania



# bearings = Index().get_bearing(origin, destination)
# print("Bearings: ",bearings)



# distance = Index().get_euclidean_distance(origin, destination)
# print("Distance: ",distance)

# distance = Index().get_great_circle_distance(origin, destination)
# print("Great Circle Distance: ",distance)

# coordinates = Index().geocode("Ubungo Maji, Dar Es Salaam, Tanzania")
# print("Coordinates: ",coordinates)


# graph = Index().get_graph("Ubungo Maji, Dar Es Salaam, Tanzania", "drive")
# print("Graph: ",graph)


# distance = Index().get_road_distance("Ubungo Maji, Dar Es Salaam, Tanzania", "Ferry Terminal, Dar Es Salaam, Tanzania", 'drive')
# print("Road Distance: ",distance)

distance = Index().get_road_distance(origin, destination, mode='drive', weight='time')
print("Road Distance: ",distance)