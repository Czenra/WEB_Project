import os


def write_down_a_word(word):
    data_path = os.path.join(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data'), 'found_words.txt')
    with open(data_path, 'r+') as file:
        word = word[:-4]
        word = word + '\n'
        words = file.readlines()
        if word in words:
            return
        else:
            file.write(word)


def bring_up_the_list():
    data_path = os.path.join(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data'), 'found_words.txt')
    with open(data_path, 'r') as file:
        words = file.readlines()
        complete_words = []
        for w in words:
            w = w.strip('\n')
            complete_words.append(w)
    return complete_words
