
def simple_resolution_solver(map_dictionary):
    for element in map_dictionary:
        if map_dictionary[element] == "?":
            this_cell = check_neighbors(map_dictionary, element)
            map_dictionary[element] = this_cell
    return map_dictionary


def check_neighbors(map_dictionary, element):
    print(element)
    neighbor_list = add_4_neighbors(map_dictionary, element)
    info_from_neighbors = []
    if "CLEAR" in neighbor_list:
        return "SAFE"
    if "" in neighbor_list:
        count = 0
        for i in neighbor_list:
            if i == "":
                count += 1
        if count >= 2:
            return "UNKNOWN"
    if element[0] > 1:
        info_from_neighbors.append(check_second_neighbor(map_dictionary, element, (element[0] - 1, element[1])))
    if element[0] < 4:
        info_from_neighbors.append(check_second_neighbor(map_dictionary, element, (element[0] + 1, element[1])))
    if element[1] > 1:
        info_from_neighbors.append(check_second_neighbor(map_dictionary, element, (element[0], element[1] - 1)))
    if element[1] < 4:
        info_from_neighbors.append(check_second_neighbor(map_dictionary, element, (element[0], element[1] + 1)))
    print("Info from neighbors: ", info_from_neighbors)
    if "MONSTER" in info_from_neighbors and "PIT" not in info_from_neighbors:
        return "MONSTER"
    elif "MONSTER" not in info_from_neighbors and "PIT" in info_from_neighbors:
        return "PIT"
    else:
        return "Broken..."


def check_second_neighbor(map_dictionary, parent_element, element):
    neighbor_list = add_4_neighbors(map_dictionary, element)
    print("Second element is", map_dictionary[element], neighbor_list)
    element_weather = map_dictionary[element]
    if element_weather not in neighbor_list:
        if element_weather == "WIND":
            return "PIT"
        elif element_weather == "STINKY":
            return "MONSTER"
    return ""


def add_4_neighbors(map_dictionary, element):
    neighbor_list = []
    if element[0] > 1:
        neighbor_list.append(map_dictionary[(element[0] - 1, element[1])])
    if element[0] < 4:
        neighbor_list.append(map_dictionary[(element[0] + 1, element[1])])
    if element[1] > 1:
        neighbor_list.append(map_dictionary[(element[0], element[1] - 1)])
    if element[1] < 4:
        neighbor_list.append(map_dictionary[(element[0], element[1] + 1)])
    return neighbor_list


if __name__ == '__main__':
    map_dictionary = {}
    map_dictionary[(1, 1)] = "CLEAR"
    map_dictionary[(1, 2)] = "WIND"
    map_dictionary[(1, 3)] = "?"
    map_dictionary[(1, 4)] = ""

    map_dictionary[(2, 1)] = "WIND"
    map_dictionary[(2, 2)] = "STINKY"
    map_dictionary[(2, 3)] = "?"
    map_dictionary[(2, 4)] = ""

    map_dictionary[(3, 1)] = "?"
    map_dictionary[(3, 2)] = "WIND"
    map_dictionary[(3, 3)] = "STINKY"
    map_dictionary[(3, 4)] = "?"

    map_dictionary[(4, 1)] = "?"
    map_dictionary[(4, 2)] = "CLEAR"
    map_dictionary[(4, 3)] = "?"
    map_dictionary[(4, 4)] = ""

    result = simple_resolution_solver(map_dictionary)
    print("Final result is: ")
    print(result)
