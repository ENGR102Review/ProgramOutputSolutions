# a string which contains both lower and upper case letters.
# notice the extra letter 'a' at the end of each alphabet. This is to make shifting easier.
caesar_alphabet = 'abcdefghijklmnopqrstuvwxyzaABCDEFGHIJKLMNOPQRSTUVWXYZA'


def caesar_cipher(original_string):
    """
    Returns the caesar cipher for a given string
    """
    # make a new string that is empty at first
    new_string = ''
    # go through each individual character in the original string
    for character in original_string:
        # check if the character is not alphabetic. 
        # If not, append the character as-is and move on to the next character in the string
        if character not in caesar_alphabet:
            new_string += character
            continue
        # at this point, the character is known to be alphabetic
        # find the index in the alphabet string corresponding to the letter
        alphabet_index = caesar_alphabet.index(character)
        # find the letter one position higher in the alphabet from the current letter
        shifted_letter = caesar_alphabet[alphabet_index + 1]
        # append the shifted letter to the string
        new_string += shifted_letter
    return new_string
