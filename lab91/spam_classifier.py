"""This algorithm detects spam email from ham email. It is based on Bayes classifier."""

import os
import pathlib


def read_directory(dirn):
    cont_l = []
    for fn in os.listdir(dirn):
        with open(os.path.join(dirn, fn), encoding="latin-1") as f:
            words = [w.strip()
                for w in f.read().replace("\n", " ").split(" ")
                    if not stopword(w)
            ]
            cont_l.append(words)
    return cont_l


def stopword(wstr):
    w = wstr.strip()
    if len(w) < 4:
        return True
    return False


if __name__ == '__main__':
    ham_l = read_directory(os.path.join("enron6", "ham"))
    spam_l = read_directory(os.path.join("enron6", "spam"))

    print(len(ham_l), "ham messages")  # meaning, these are not spam
    print(len(spam_l), "spam messages")