from queue import PriorityQueue


def astar(kaart, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    diamond_coordinates = ()
    cost_so_far = {start: 0}
    iteration_count = 0

    while not frontier.empty():
        _, current = frontier.get()
        current_x = current[0]
        current_y = current[1]
        print(current_x, current_y)
        if kaart[current_x][current_y] == "D":
            diamond_coordinates = current
            break

        neighbor_list = find_neighbors(current_x, current_y)
        new_cost = cost_so_far[current] + 1
        for neighbor in neighbor_list:
            if check_conditions(neighbor, kaart, came_from):
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + h(neighbor, goal)  # g(n) + h(n)
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
    # lava_map = [
    #     "      **               **      ",
    #     "     ***     D        ***      ",
    #     "     ***                       ",
    #     "                      *****    ",
    #     "           ****      ********  ",
    #     "           ***          *******",
    #     " **                      ******",
    #     "*****             ****     *** ",
    #     "*****              **          ",
    #     "***                            ",
    #     "              **         ******",
    #     "**            ***       *******",
    #     "***                      ***** ",
    #     "                               ",
    #     "                s              ",
    # ]
    # start_position = (14, 16)
    # goal_position = (1, 13)
    lava_map = read_big_map("cave900x900")
    start_position = (2, 2)
    goal_position = (898, 895)
    path = astar(lava_map, start_position, goal_position)
    print(path)
    print("Path length is: " + str(len(path)))
