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
    """Get all words as list in either spam or ham training folder."""
    words = []
    for message in directory_messages:
        for word in message:
            words.append(word)
    return words


def train_function(ham_l, spam_l):
    """Gets data based on spam and ham messages."""
    ham_word_data = count_directory_words(ham_l)
    spam_word_data = count_directory_words(spam_l)
    return ham_word_data, spam_word_data


def read_message(message_file):
    """Read message from a txt file. Return all words as list."""
    words = []
    f = open(message_file, "r")
    for line in f:
        for word in line.split():
            if not stopword(word):
                words.append(word)
    return words


def count_words(word, words):
    """Count occurrence of same words in a message's words list."""
    same_words_in_message = 0
    for element in words:
        if element == word:
            same_words_in_message += 1
    return same_words_in_message


def calculate_word_probability(word, data_words):
    same_word_count = count_words(word, data_words)
    data_word_count = len(data_words)
    data_unique_word_count = len(set(data_words))
    return (same_word_count + 1) / (data_word_count + data_unique_word_count)


def get_message_probability(message_words, data_words):
    message_probability = 0.0
    for word in message_words:
        message_probability += calculate_word_probability(word, data_words)
    return message_probability


def classify_message(message_words, ham_l, spam_l):
    """Calculates if message is spam or ham based on probability comparison. Uses data from training messages."""
    data_ham_words, data_spam_words = train_function(ham_l, spam_l)
    message_unique_words = set(message_words)
    message_ham_words, message_spam_words = [], []
    for word in message_unique_words:
        if word in data_ham_words:
            message_ham_words.append(word)
        if word in data_spam_words:
            message_spam_words.append(word)
    probability_ham = ((len(ham_l)) / (len(ham_l) + len(spam_l))) + get_message_probability(message_ham_words, data_ham_words)
    probability_spam = ((len(spam_l)) / (len(ham_l) + len(spam_l))) + get_message_probability(message_spam_words, data_spam_words)
    print(probability_ham, probability_spam)
    if probability_ham > probability_spam:
        return "This letter is ham."
    else:
        return "This letter is spam."


if __name__ == '__main__':
    ham_letters = read_directory(os.path.join("enron6", "ham"))
    spam_letters = read_directory(os.path.join("enron6", "spam"))
    print(len(ham_letters), "ham messages")
    print(len(spam_letters), "spam messages")
    message1_words = read_message("message1.txt")
    message2_words = read_message("message2.txt")

    print(classify_message(message1_words, ham_letters, spam_letters))
    print(classify_message(message2_words, ham_letters, spam_letters))
