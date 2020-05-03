import pandas as pd

features = ["hair", "feathers", "eggs", "milk", "airborne",
    "aquatic", "predator", "toothed", "backbone", "breathes", "venomous",
    "fins", "legs", "tail", "domestic", "catsize"]

zoo_data = pd.read_csv("zoo.data",
    header = None,
    names = ["name"] + features + ["type"])


if __name__ == '__main__':
    print(zoo_data)