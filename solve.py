import re


def check_letters(w, letters_to_IN, letter_to_EX):
    for li in letters_to_IN:
        if li not in w:
            return False
    for le in letter_to_EX:
        if le in w:
            return False
    return True


def solve_wordle(word_list, l_ex, l_pattern, y_pattern):

    if l_ex == '' and l_pattern.count('') == 5 and y_pattern.count('') == 5:
        return 'Please enter some information!'

    pattern = ''
    for i in range(5):
        if l_pattern[i] != '':
            pattern += '[' + l_pattern[i] + ']'
        elif y_pattern[i] != '':
            pattern += '[^' + y_pattern[i] + ']'
        else:
            pattern += '.'
    pattern = pattern.lower()

    solution = ''

    l_in_clean = ''.join(l_pattern).lower() + ''.join(y_pattern).lower()
    l_ex_clean = l_ex.lower()

    for w in word_list:
        w = w.lower()
        if check_letters(w, l_in_clean, l_ex_clean):
            if re.fullmatch(pattern, w):
                solution = solution + w + '<br>'

    if solution == '':
        return 'Sorry! We could not find a solution.'

    return solution
