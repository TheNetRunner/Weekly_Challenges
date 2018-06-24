from pymorse import MorseCodeBook

MORSECODELIST = MorseCodeBook.international_list


# Uses the sequence_char function to convert a list of sequences strings
def sequence_string(a_sequence_list):
    completed_string = ""
    for sequence in a_sequence_list:
        completed_string += sequence_char(sequence)
    return completed_string


# Uses the char_sequence function to convert a whole string
def string_sequence(a_string):
    string_list = list(a_string)
    code_list = []
    for char in string_list:
        code_list.append(char_sequence(char))
    return code_list


# This function takes a character in a string and converts it to morse code
def char_sequence(a_char):
    for item in MORSECODELIST:
        if item['Char'] == a_char.upper():
            return item['Sequence']


#  This function takes a sequence string in dits (*) and dahs (-) and converts it to a char
def sequence_char(a_sequence):
    for item in MORSECODELIST:
        if item['Sequence'] == a_sequence.lower():
            return item['Char']

