def decoder (message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    punctuation = "!'?,. "
    translated_message = ''
    for letters in message:
        if letters in punctuation:
            translated_message += letters
        else:
            letter_value = alphabet.find(letters)
            translated_message += alphabet[(letter_value + offset)%26]
    return translated_message


def coder (message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    punctuation = "!'?,. "
    translated_message = ''
    for letters in message:
        if letters in punctuation:
            translated_message += letters
        else:
            letter_value = alphabet.find(letters)
            translated_message += alphabet[(letter_value - offset)%26]

    return translated_message
