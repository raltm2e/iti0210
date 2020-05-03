import math
import pandas as pd

features = ["hair", "feathers", "eggs", "milk", "airborne",
    "aquatic", "predator", "toothed", "backbone", "breathes", "venomous",
    "fins", "legs", "tail", "domestic", "catsize"]

zoo_data = pd.read_csv("zoo.data",
    header = None,
    names = ["name"] + features + ["type"])


def get_samples_by_parameter(parameter, cur_type, value):
    for key, val in zoo_data.groupby([parameter, "type"]).size().items():
        if key == (value, cur_type):
            return val


def calculate_entropy(features, zoo_data):
    for feature in features:
        N = zoo_data[feature].size
        H = 0
        for key, val in zoo_data.groupby([feature]).size().items():
            Hi = 0
            Ni = val
            for key1, val1 in zoo_data.groupby(["type"]).size().items():
                Nij = get_samples_by_parameter(feature, key1, key)
                if Nij:
                    Pij = Nij / Ni
                    Hi -= Pij * math.log2(Pij)
            H += (Ni * Hi) / N
        print(feature + ' entropy = %.4f' % H)


if __name__ == '__main__':
    calculate_entropy(features, zoo_data)
