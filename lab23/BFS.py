from queue import Queue


def minu_otsing(kaart, start):

    frontier = Queue()
    frontier.put(start)
    visited_coords = {}

    while not frontier.empty():
        current = frontier.get()
        current_x = current[0]
        current_y = current[1]
        print(current_x, current_y)

        print(kaart[current_x][current_y])
        if kaart[current_x][current_y] == "D":
            print("Jõudsin lõppsihtkohta")
            break

        if check_conditions(current_x + 1, current_y, kaart, visited_coords):
            frontier.put((current_x + 1, current_y))

        if check_conditions(current_x - 1, current_y, kaart, visited_coords):
            frontier.put((current_x - 1, current_y))

        if check_conditions(current_x, current_y - 1, kaart, visited_coords):
            frontier.put((current_x, current_y - 1))

        if check_conditions(current_x, current_y + 1, kaart, visited_coords):
            frontier.put((current_x, current_y + 1))

        visited_coords[current_x] = current_y


def check_conditions(current_x, current_y, kaart, visited_coords):
    return current_x <= len(kaart) - 1 and current_y <= len(kaart[0]) - 1\
           and current_x not in list(visited_coords.keys()) and current_y not in list(visited_coords.values())\
           and current_x >= 0 and current_y >= 0


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
    minu_otsing(lava_map1, (start_row, start_col))
