from queue import Queue


def minu_otsing(kaart, start):
    frontier = Queue()
    frontier.put(start)
    came_from = {start: None}
    diamond_coordinates = ()

    while not frontier.empty():
        current = frontier.get()
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
                frontier.put(neighbor)
                came_from[neighbor] = current
    return get_path(came_from, diamond_coordinates)


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


if __name__ == "__main__":
    lava_map1 = [
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
    start_row = 14
    start_col = 16
    print(minu_otsing(lava_map1, (start_row, start_col)))
