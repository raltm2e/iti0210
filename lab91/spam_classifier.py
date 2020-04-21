"""This algorithm detects spam email from ham email. It is based on Bayes classifier."""

import os


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
    """Function checks if word is not shorter than 4 characters."""
    w = wstr.strip()
    if len(w) < 4:
        return True
    return False


def count_directory_words(directory_messages):
    words = []
    for message in directory_messages:
        for word in message:
            words.append(word)
    return len(words), len(set(words))


def train_function(ham_l, spam_l):
    ham_words = count_directory_words(ham_l)
    ham_word_amount = ham_words[0]
    ham_unique_word_amount = ham_words[1]

    spam_words = count_directory_words(spam_l)
    spam_word_amount = spam_words[0]
    spam_unique_word_amount = spam_words[1]
    print(spam_word_amount, spam_unique_word_amount)


if __name__ == '__main__':
    ham_letters = read_directory(os.path.join("enron6", "ham"))
    spam_letters = read_directory(os.path.join("enron6", "spam"))
    print(len(ham_letters), "ham messages")
    print(len(spam_letters), "spam messages")

    train_function(ham_letters, spam_letters)
