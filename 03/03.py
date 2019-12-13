from read_file import read_line1, read_line2


# Create an object with coordinates for each step
def populate_grid(moving_input):
    coordinates_all = {}

    # Set the current position
    x = 0
    y = 0

    # Counter for each time the position moves
    step = 0

    # Loop through all the directions given by the file
    for move in moving_input:
        direction = move[0]
        distance = int(move[1:])

        # Pick in which direction to move
        move_x = 0
        move_y = 0
        if direction == "L":
            move_x = -1
        if direction == "R":
            move_x = 1
        if direction == "D":
            move_y = -1
        if direction == "U":
            move_y = 1

        # Do the actual movement
        for _ in range(0, distance):
            x += move_x
            y += move_y

            step += 1

            if (x,y) not in coordinates_all:
                coordinates_all[(x,y)] = step

    return coordinates_all


# Get the coordinate grids for each line
line_1 = populate_grid(read_line1("input.txt"))
line_2 = populate_grid(read_line2("input.txt"))

# Get the intersections for both sets with &
intersections = list(set(line_1.keys()) & set(line_2.keys())) #set & = overlap between two lists
print(intersections)


def get_shortest():
    distances = []
    for intersection in intersections:
        #Sum
        dist = abs(intersection[0]) + abs(intersection[1])
        distances.append(dist)
    return min(distances)


def get_fewest():
    #get values
    combined_steps = [line_1[i] + line_2[i] for i in intersections]
    return min(combined_steps)
