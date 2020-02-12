from queue import Queue, PriorityQueue


def greedy_search(kaart, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    diamond_coordinates = ()
    iteration_count = 0

    while not frontier.empty():
        _, current = frontier.get()
        current_x = current[0]
        current_y = current[1]
        print(current_x, current_y)
        print(kaart[current_x][current_y])
        if kaart[current_x][current_y] == "D":
            diamond_coordinates = current
            break

        neighbor_list = find_neighbors(current_x, current_y)
        for neighbor in neighbor_list:
            if check_conditions(neighbor, kaart, came_from):
                priority = h(neighbor, goal)
                frontier.put((priority, neighbor))
                came_from[neighbor] = current

        iteration_count += 1
    print("Iterated " + str(iteration_count) + " times.")
    return get_path(came_from, diamond_coordinates)


def h(neighbor, goal):
    return abs(neighbor[0] - goal[0]) + abs(neighbor[1] - goal[1])


def get_path(came_from, diamond_coordinates):
    path = [diamond_coordinates, came_from[diamond_coordinates]]
    while came_from[diamond_coordinates] is not None:
        diamond_coordinates = came_from[diamond_coordinates]
        path.append(diamond_coordinates)
    return path


def find_neighbors(current_x, current_y):
    return [(current_x + 1, current_y), (current_x - 1, current_y),
            (current_x, current_y + 1), (current_x, current_y - 1)]


def check_conditions(current, kaart, came_from):
    current_x = current[0]
    current_y = current[1]
    if current not in came_from and current_x <= len(kaart) - 1 and current_y <= len(kaart[0]) - 1 and current_x >= 0 and current_y >= 0:
        return kaart[current_x][current_y] != "*"
    else:
        return False


def read_big_map(filename):
    with open(filename) as f:
        map_data = [l.strip() for l in f.readlines() if len(l) > 1]
    return map_data


if __name__ == "__main__":
    lava_map = [
        "      **               **      ",
        "     ***     D        ***      ",
        "     ***                       ",
        "                      *****    ",
        "           ****      ********  ",
        "           ***          *******",
        " **                      ******",
        "*****             ****     *** ",
        "*****              **          ",
        "***                            ",
        "              **         ******",
        "**            ***       *******",
        "***                      ***** ",
        "                               ",
        "                s              ",
    ]
    start_position = (14, 16)
    goal_position = (1, 13)
    # lava_map = read_big_map("cave900x900")
    # start_row, start_col = 2, 2
    print(greedy_search(lava_map, start_position, goal_position))
